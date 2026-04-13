"""Interactive chat API and WebSocket routes."""

from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException, Query, Request, Response, WebSocket, WebSocketDisconnect, status
from sqlalchemy.orm import Session

from app.auth.dependencies import get_auth_service, get_ws_ticket_service, require_session_principal
from app.auth.schemas import WSTicketResponse, WebChatSessionResponse
from app.auth.services import AuthService, WSTicketService
from app.chat.schemas import ChatTurnRequest
from app.chat.service import ChatRuntimeService
from app.core.config import Settings, get_settings
from app.persistence.db import get_db_session, get_session_factory
from app.tenancy.cache import get_state_store
from app.tenancy.models import SessionPrincipal
from app.tenancy.services import TenantAccessError

router = APIRouter(prefix="/v1/chat", tags=["chat"])


def _set_chat_session_cookie(response: Response, settings: Settings, token: str) -> None:
    response.set_cookie(
        key=settings.chat_session_cookie_name,
        value=token,
        max_age=settings.session_ttl_seconds,
        httponly=True,
        samesite="strict",
        secure=settings.web_cookie_secure,
        path="/",
    )


def _clear_chat_session_cookie(response: Response, settings: Settings) -> None:
    response.delete_cookie(
        key=settings.chat_session_cookie_name,
        httponly=True,
        samesite="strict",
        secure=settings.web_cookie_secure,
        path="/",
    )


@router.post("/web/session", response_model=WebChatSessionResponse)
async def start_web_chat_session(
    request: Request,
    response: Response,
    auth_service: AuthService = Depends(get_auth_service),
    settings: Settings = Depends(get_settings),
) -> WebChatSessionResponse:
    try:
        session_context = await auth_service.start_web_chat_session(origin=request.headers.get("origin"))
    except TenantAccessError as exc:
        raise HTTPException(status_code=exc.status_code, detail=str(exc)) from exc

    _set_chat_session_cookie(response, settings, session_context.access_token)
    return WebChatSessionResponse(
        session_id=session_context.session_id,
        display_name=session_context.display_name,
        expires_in=session_context.expires_in,
    )


@router.post("/ws-ticket", response_model=WSTicketResponse)
async def issue_ws_ticket(
    request: Request,
    principal: SessionPrincipal = Depends(require_session_principal),
    ws_ticket_service: WSTicketService = Depends(get_ws_ticket_service),
) -> WSTicketResponse:
    origin = request.headers.get("origin")
    if principal.tenant.allowed_origins and origin and origin not in principal.tenant.allowed_origins:
        raise HTTPException(status_code=403, detail="Origine non autorizzata per il tenant.")
    return await ws_ticket_service.issue_ticket(principal)


@router.post("/session/{session_id}/close", status_code=status.HTTP_204_NO_CONTENT)
async def close_session(
    session_id: str,
    response: Response,
    principal: SessionPrincipal = Depends(require_session_principal),
    session: Session = Depends(get_db_session),
    settings: Settings = Depends(get_settings),
):
    if principal.session_id != session_id:
        raise HTTPException(status_code=403, detail="Sessione non coerente con il token.")
    runtime = ChatRuntimeService(session=session, settings=settings, state_store=get_state_store(settings))
    await runtime.close_session(principal)
    _clear_chat_session_cookie(response, settings)
    return None


@router.websocket("/ws")
async def chat_ws(
    websocket: WebSocket,
    ticket: str = Query(..., min_length=8),
):
    settings = get_settings()
    state_store = get_state_store(settings)
    session = get_session_factory()()
    ticket_service = WSTicketService(session=session, settings=settings, state_store=state_store)
    accepted = False

    try:
        principal = await ticket_service.consume_ticket(ticket)
        origin = websocket.headers.get("origin")
        if principal.tenant.allowed_origins and origin and origin not in principal.tenant.allowed_origins:
            raise TenantAccessError("Origine WebSocket non autorizzata per il tenant.", reason_code="origin_forbidden", status_code=403)
        await websocket.accept()
        accepted = True
        runtime = ChatRuntimeService(session=session, settings=settings, state_store=state_store)
        ready_usage = runtime.record_ws_connect(principal)
        await websocket.send_json({"type": "ready", "session_id": principal.session_id, "usage": ready_usage.model_dump()})

        while True:
            payload = ChatTurnRequest.model_validate(await websocket.receive_json())
            response = await runtime.handle_turn(principal, payload)
            await websocket.send_json(response.model_dump(mode="json"))
    except WebSocketDisconnect:
        return
    except TenantAccessError as exc:
        if accepted:
            await websocket.send_json({"type": "error", "detail": str(exc), "reason_code": exc.reason_code})
            await websocket.close(code=status.WS_1008_POLICY_VIOLATION)
        else:
            await websocket.close(code=status.WS_1008_POLICY_VIOLATION, reason=str(exc))
    except Exception:
        if accepted:
            await websocket.send_json({"type": "error", "detail": "Errore interno durante l'elaborazione della chat."})
            await websocket.close(code=status.WS_1011_INTERNAL_ERROR)
        else:
            await websocket.close(code=status.WS_1011_INTERNAL_ERROR, reason="Errore interno.")
    finally:
        session.close()
