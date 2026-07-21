function buildUrl(baseUrl, path) {
  const normalizedBase = (baseUrl || "").trim().replace(/\/+$/, "");
  return normalizedBase ? `${normalizedBase}${path}` : path;
}

async function parseResponse(response) {
  if (response.status === 204) {
    return null;
  }

  const contentType = response.headers.get("content-type") || "";
  if (contentType.includes("application/json")) {
    return response.json();
  }

  return response.text();
}

function extractErrorInfo(payload) {
  if (payload && typeof payload === "object") {
    const reasonCode =
      typeof payload.reason_code === "string" ? payload.reason_code : "";

    if ("detail" in payload) {
      const detail = payload.detail;
      if (typeof detail === "string" && detail.trim()) {
        return { message: detail, reasonCode };
      }
      if (detail && typeof detail === "object") {
        const detailReasonCode =
          typeof detail.reason_code === "string"
            ? detail.reason_code
            : reasonCode;
        const message =
          (typeof detail.message === "string" && detail.message.trim()) ||
          (typeof detail.detail === "string" && detail.detail.trim()) ||
          JSON.stringify(detail);
        return { message, reasonCode: detailReasonCode };
      }
    }
  }

  if (typeof payload === "string" && payload.trim()) {
    return { message: payload, reasonCode: "" };
  }

  return { message: "", reasonCode: "" };
}

const refreshRequests = {
  admin: null,
  chat: null,
};

function authScopeForPath(path) {
  if (path === "/v1/admin-auth/me" || path.startsWith("/v1/admin/")) {
    return "admin";
  }
  if (
    path === "/v1/chat-auth/me" ||
    path === "/v1/chat/ws-ticket" ||
    path.startsWith("/v1/chat/session/")
  ) {
    return "chat";
  }
  return null;
}

function fetchOptions({ method, body }) {
  return {
    method,
    credentials: "same-origin",
    headers: {
      ...(body !== undefined ? { "Content-Type": "application/json" } : {}),
    },
    body: body !== undefined ? JSON.stringify(body) : undefined,
  };
}

async function refreshAuthentication(baseUrl, scope) {
  if (!refreshRequests[scope]) {
    const path = `/v1/${scope === "admin" ? "admin-auth" : "chat-auth"}/refresh`;
    refreshRequests[scope] = fetch(buildUrl(baseUrl, path), {
      method: "POST",
      credentials: "same-origin",
    })
      .then((response) => response.ok)
      .catch(() => false)
      .finally(() => {
        refreshRequests[scope] = null;
      });
  }
  return refreshRequests[scope];
}

async function request(baseUrl, path, { method = "GET", body } = {}) {
  const url = buildUrl(baseUrl, path);
  const options = fetchOptions({ method, body });
  let response = await fetch(url, options);

  const authScope = authScopeForPath(path);
  if (response.status === 401 && authScope) {
    const refreshed = await refreshAuthentication(baseUrl, authScope);
    if (refreshed) {
      response = await fetch(url, options);
    }
  }

  const payload = await parseResponse(response);
  if (!response.ok) {
    const errorInfo = extractErrorInfo(payload);
    const error = new Error(
      errorInfo.message || `Richiesta non riuscita (${response.status})`,
    );
    error.status = response.status;
    error.payload = payload;
    error.reasonCode =
      response.headers.get("x-reason-code") || errorInfo.reasonCode || "";
    throw error;
  }

  return payload;
}

export function fetchHealth(baseUrl) {
  return request(baseUrl, "/health");
}

export function loginAdmin(baseUrl, payload) {
  return request(baseUrl, "/v1/admin-auth/login", {
    method: "POST",
    body: payload,
  });
}

export function loginChat(baseUrl, payload) {
  return request(baseUrl, "/v1/chat-auth/login", {
    method: "POST",
    body: payload,
  });
}

export function fetchAdminMe(baseUrl) {
  return request(baseUrl, "/v1/admin-auth/me");
}

export function fetchChatMe(baseUrl) {
  return request(baseUrl, "/v1/chat-auth/me");
}

export function logoutAdmin(baseUrl) {
  return request(baseUrl, "/v1/admin-auth/logout", { method: "POST" });
}

export function logoutChat(baseUrl) {
  return request(baseUrl, "/v1/chat-auth/logout", { method: "POST" });
}

export function runIngestion(baseUrl, payload) {
  return request(baseUrl, "/ingest", { method: "POST", body: payload });
}

export function startWebChatSession(baseUrl) {
  return request(baseUrl, "/v1/chat/web/session", { method: "POST" });
}

export function issueWsTicket(baseUrl) {
  return request(baseUrl, "/v1/chat/ws-ticket", { method: "POST" });
}

export function closeChatSession(baseUrl, sessionId) {
  return request(baseUrl, `/v1/chat/session/${sessionId}/close`, {
    method: "POST",
  });
}

export function createWebSocketUrl(baseUrl, path) {
  const normalizedBase = (baseUrl || "").trim().replace(/\/+$/, "");
  const normalizedPath = path.startsWith("/") ? path : `/${path}`;

  if (!normalizedBase) {
    const protocol = window.location.protocol === "https:" ? "wss:" : "ws:";
    return `${protocol}//${window.location.host}${normalizedPath}`;
  }

  const target = new URL(normalizedBase, window.location.origin);
  target.protocol = target.protocol === "https:" ? "wss:" : "ws:";
  target.pathname = `${target.pathname.replace(/\/+$/, "")}${normalizedPath}`;
  target.search = "";
  target.hash = "";
  return target.toString();
}

export function fetchTenants(baseUrl) {
  return request(baseUrl, "/v1/admin/tenants");
}

export function fetchModelSettings(baseUrl) {
  return request(baseUrl, "/v1/admin/model-settings");
}

export function updateModelSettings(baseUrl, payload) {
  return request(baseUrl, "/v1/admin/model-settings", {
    method: "PUT",
    body: payload,
  });
}

export function createTenant(baseUrl, payload) {
  return request(baseUrl, "/v1/admin/tenants", {
    method: "POST",
    body: payload,
  });
}

export function updateTenant(baseUrl, tenantId, payload) {
  return request(baseUrl, `/v1/admin/tenants/${tenantId}`, {
    method: "PATCH",
    body: payload,
  });
}

export function updateTenantLicense(baseUrl, tenantId, payload) {
  return request(baseUrl, `/v1/admin/tenants/${tenantId}/license`, {
    method: "PATCH",
    body: payload,
  });
}

export function rotateTenantKey(baseUrl, tenantId, payload) {
  return request(baseUrl, `/v1/admin/tenants/${tenantId}/keys/rotate`, {
    method: "POST",
    body: payload,
  });
}

export function suspendTenant(baseUrl, tenantId) {
  return request(baseUrl, `/v1/admin/tenants/${tenantId}/suspend`, {
    method: "POST",
  });
}

export function activateTenant(baseUrl, tenantId) {
  return request(baseUrl, `/v1/admin/tenants/${tenantId}/activate`, {
    method: "POST",
  });
}

export function fetchTenantUsage(baseUrl, tenantId, days) {
  return request(baseUrl, `/v1/admin/tenants/${tenantId}/usage?days=${days}`);
}

export function fetchTenantUsers(baseUrl, tenantId) {
  return request(baseUrl, `/v1/admin/tenants/${tenantId}/users`);
}

export function createTenantUser(baseUrl, tenantId, payload) {
  return request(baseUrl, `/v1/admin/tenants/${tenantId}/users`, {
    method: "POST",
    body: payload,
  });
}

export function regenerateTenantUserPassword(baseUrl, tenantId, userId) {
  return request(
    baseUrl,
    `/v1/admin/tenants/${tenantId}/users/${userId}/password/regenerate`,
    { method: "POST" },
  );
}

export function deleteTenantUser(baseUrl, tenantId, userId) {
  return request(baseUrl, `/v1/admin/tenants/${tenantId}/users/${userId}`, {
    method: "DELETE",
  });
}
