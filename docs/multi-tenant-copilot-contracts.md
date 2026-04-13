# Multi-Tenant ERP Copilot Contracts

## JWT Claims

### ERP bootstrap JWT

- `iss`: tenant issuer
- `aud`: `rag-doc-bootstrap`
- `tid`: tenant id
- `sub`: ERP user id
- `jti`: unique token id
- `iat`: issued-at timestamp
- `exp`: short-lived expiry
- `roles`: ERP roles
- `mask_id`: current ERP mask identifier
- `mask_permissions`: permissions such as `chat:use`
- `company_code`: optional tenant company code

### Session JWT

- `iss`: `rag-doc-api`
- `aud`: `rag-doc-api`
- `tid`: tenant id
- `sub`: ERP user id
- `sid`: chat session id
- `roles`: ERP roles
- `mask_id`: current ERP mask identifier
- `mask_permissions`: permissions such as `chat:use`
- `exp`: short-lived expiry

## Redis Keys

- `auth:bootstrap:jti:{jti}`: replay guard
- `chat:wsticket:{token}`: single-use WebSocket ticket
- `chat:memory:{tenant_id}:{user_ref_hash}:{session_id}`: ephemeral conversation history
- `rate:tenant:{tenant_id}:{window}`: tenant burst counter
- `rate:user:{tenant_id}:{user_ref_hash}:{window}`: per-user burst counter

## WebSocket Protocol

### Client to server

```json
{
  "type": "user_message",
  "message": "Come registro una prima nota?",
  "screen_context": {},
  "retrieval_options": {}
}
```

### Server to client

```json
{
  "type": "final",
  "answer": "string",
  "steps": ["string"],
  "citations": [],
  "follow_up_question": null,
  "confidence": 0.0,
  "answer_mode": "grounded",
  "inference_notice": null,
  "usage": {
    "messages_in": 1,
    "messages_out": 1,
    "prompt_tokens": 0,
    "completion_tokens": 0
  }
}
```

## Persistence Rules

- Postgres is the source of truth for tenants, licenses, sessions, usage, and audit.
- Redis is used only for ephemeral runtime state.
- No raw chat transcript is persisted outside Redis by default.
- Persistent rows store `user_ref_hash`, not raw ERP user identifiers.
