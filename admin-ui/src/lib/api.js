function buildUrl(baseUrl, path) {
  const normalizedBase = (baseUrl || '').trim().replace(/\/+$/, '')
  return normalizedBase ? `${normalizedBase}${path}` : path
}

async function parseResponse(response) {
  if (response.status === 204) {
    return null
  }

  const contentType = response.headers.get('content-type') || ''
  if (contentType.includes('application/json')) {
    return response.json()
  }

  return response.text()
}

async function request(baseUrl, path, { method = 'GET', body } = {}) {
  const response = await fetch(buildUrl(baseUrl, path), {
    method,
    credentials: 'same-origin',
    headers: {
      ...(body !== undefined ? { 'Content-Type': 'application/json' } : {}),
    },
    body: body !== undefined ? JSON.stringify(body) : undefined,
  })

  const payload = await parseResponse(response)
  if (!response.ok) {
    const detail =
      (payload && typeof payload === 'object' && 'detail' in payload && payload.detail) ||
      (typeof payload === 'string' ? payload : null) ||
      `Richiesta non riuscita (${response.status})`
    const error = new Error(detail)
    error.status = response.status
    error.payload = payload
    throw error
  }

  return payload
}

export function fetchHealth(baseUrl) {
  return request(baseUrl, '/health')
}

export function loginAdmin(baseUrl, payload) {
  return request(baseUrl, '/v1/admin-auth/login', { method: 'POST', body: payload })
}

export function fetchAdminMe(baseUrl) {
  return request(baseUrl, '/v1/admin-auth/me')
}

export function logoutAdmin(baseUrl) {
  return request(baseUrl, '/v1/admin-auth/logout', { method: 'POST' })
}

export function runIngestion(baseUrl, payload) {
  return request(baseUrl, '/ingest', { method: 'POST', body: payload })
}

export function startWebChatSession(baseUrl) {
  return request(baseUrl, '/v1/chat/web/session', { method: 'POST' })
}

export function issueWsTicket(baseUrl) {
  return request(baseUrl, '/v1/chat/ws-ticket', { method: 'POST' })
}

export function closeChatSession(baseUrl, sessionId) {
  return request(baseUrl, `/v1/chat/session/${sessionId}/close`, { method: 'POST' })
}

export function createWebSocketUrl(baseUrl, path) {
  const normalizedBase = (baseUrl || '').trim().replace(/\/+$/, '')
  const normalizedPath = path.startsWith('/') ? path : `/${path}`

  if (!normalizedBase) {
    const protocol = window.location.protocol === 'https:' ? 'wss:' : 'ws:'
    return `${protocol}//${window.location.host}${normalizedPath}`
  }

  const target = new URL(normalizedBase, window.location.origin)
  target.protocol = target.protocol === 'https:' ? 'wss:' : 'ws:'
  target.pathname = `${target.pathname.replace(/\/+$/, '')}${normalizedPath}`
  target.search = ''
  target.hash = ''
  return target.toString()
}

export function fetchTenants(baseUrl) {
  return request(baseUrl, '/v1/admin/tenants')
}

export function createTenant(baseUrl, payload) {
  return request(baseUrl, '/v1/admin/tenants', { method: 'POST', body: payload })
}

export function updateTenant(baseUrl, tenantId, payload) {
  return request(baseUrl, `/v1/admin/tenants/${tenantId}`, { method: 'PATCH', body: payload })
}

export function updateTenantLicense(baseUrl, tenantId, payload) {
  return request(baseUrl, `/v1/admin/tenants/${tenantId}/license`, { method: 'PATCH', body: payload })
}

export function rotateTenantKey(baseUrl, tenantId, payload) {
  return request(baseUrl, `/v1/admin/tenants/${tenantId}/keys/rotate`, { method: 'POST', body: payload })
}

export function suspendTenant(baseUrl, tenantId) {
  return request(baseUrl, `/v1/admin/tenants/${tenantId}/suspend`, { method: 'POST' })
}

export function activateTenant(baseUrl, tenantId) {
  return request(baseUrl, `/v1/admin/tenants/${tenantId}/activate`, { method: 'POST' })
}

export function fetchTenantUsage(baseUrl, tenantId, days) {
  return request(baseUrl, `/v1/admin/tenants/${tenantId}/usage?days=${days}`)
}
