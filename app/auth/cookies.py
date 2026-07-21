"""Cookie helpers shared by all browser authentication routes."""

from fastapi import Response

from app.core.config import Settings

ADMIN_REFRESH_PATH = "/v1/admin-auth"
CHAT_REFRESH_PATH = "/v1/chat-auth"


def set_admin_auth_cookies(response: Response, settings: Settings, *, access_token: str, refresh_token: str) -> None:
    _set_cookie(response, settings, settings.admin_session_cookie_name, access_token, settings.admin_session_ttl_seconds)
    _set_cookie(
        response,
        settings,
        settings.admin_refresh_cookie_name,
        refresh_token,
        settings.admin_refresh_ttl_seconds,
        path=ADMIN_REFRESH_PATH,
    )


def clear_admin_auth_cookies(response: Response, settings: Settings) -> None:
    _clear_cookie(response, settings, settings.admin_session_cookie_name)
    _clear_cookie(response, settings, settings.admin_refresh_cookie_name, path=ADMIN_REFRESH_PATH)


def set_chat_auth_cookies(response: Response, settings: Settings, *, access_token: str, refresh_token: str) -> None:
    _set_cookie(response, settings, settings.chat_session_cookie_name, access_token, settings.session_ttl_seconds)
    _set_cookie(
        response,
        settings,
        settings.chat_refresh_cookie_name,
        refresh_token,
        settings.refresh_ttl_seconds,
        path=CHAT_REFRESH_PATH,
    )


def clear_chat_auth_cookies(response: Response, settings: Settings) -> None:
    _clear_cookie(response, settings, settings.chat_session_cookie_name)
    _clear_cookie(response, settings, settings.chat_refresh_cookie_name, path=CHAT_REFRESH_PATH)


def _set_cookie(
    response: Response,
    settings: Settings,
    name: str,
    value: str,
    max_age: int,
    *,
    path: str = "/",
) -> None:
    response.set_cookie(
        key=name,
        value=value,
        max_age=max_age,
        httponly=True,
        samesite="strict",
        secure=settings.web_cookie_secure,
        path=path,
    )


def _clear_cookie(response: Response, settings: Settings, name: str, *, path: str = "/") -> None:
    response.delete_cookie(
        key=name,
        httponly=True,
        samesite="strict",
        secure=settings.web_cookie_secure,
        path=path,
    )
