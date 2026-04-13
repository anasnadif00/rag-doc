export function createDefaultCreateForm() {
  return {
    tenantCode: '',
    displayName: '',
    issuer: '',
    allowedOrigins: '',
    licenseTier: 'standard',
    overlayCollection: '',
    publicKeyPem: '',
    publicKeyKid: '',
    licenseStatus: 'active',
    dailyMessageLimit: '500',
    dailyTokenLimit: '500000',
    burstRpsLimit: '5',
    concurrentSessionsLimit: '10',
    overlayKbEnabled: false,
    erpToolsEnabled: false,
  }
}

export function createDefaultIngestForm() {
  return {
    limit: '',
    recreateCollection: false,
    docTypes: '',
    erpVersion: '',
    reviewStatuses: 'approved',
    strictValidation: false,
    rebuildLexicalIndex: true,
  }
}

export function createDefaultKeyForm() {
  return {
    publicKeyPem: '',
    kid: '',
    algorithm: 'RS256',
  }
}

export function buildCreatePayload(form) {
  return {
    tenant_code: form.tenantCode.trim(),
    display_name: form.displayName.trim(),
    issuer: form.issuer.trim(),
    allowed_origins: parseListInput(form.allowedOrigins),
    license_tier: form.licenseTier.trim() || 'standard',
    overlay_collection: emptyToNull(form.overlayCollection),
    public_key_pem: emptyToNull(form.publicKeyPem),
    public_key_kid: emptyToNull(form.publicKeyKid),
    license: {
      status: form.licenseStatus,
      daily_message_limit: toPositiveNumber(form.dailyMessageLimit, 500),
      daily_token_limit: toPositiveNumber(form.dailyTokenLimit, 500000),
      burst_rps_limit: toPositiveNumber(form.burstRpsLimit, 5),
      concurrent_sessions_limit: toPositiveNumber(form.concurrentSessionsLimit, 10),
      overlay_kb_enabled: form.overlayKbEnabled,
      erp_tools_enabled: form.erpToolsEnabled,
    },
  }
}

export function buildTenantProfileForm(tenant) {
  return {
    displayName: tenant.display_name,
    status: tenant.status,
    allowedOrigins: tenant.allowed_origins.join('\n'),
    licenseTier: tenant.license_tier,
    overlayCollection: tenant.overlay_collection || '',
  }
}

export function buildTenantProfilePayload(form) {
  return {
    display_name: form.displayName.trim(),
    status: form.status,
    allowed_origins: parseListInput(form.allowedOrigins),
    license_tier: form.licenseTier.trim() || 'standard',
    overlay_collection: emptyToNull(form.overlayCollection),
  }
}

export function buildLicenseForm(tenant) {
  return {
    status: tenant.license.status,
    dailyMessageLimit: String(tenant.license.daily_message_limit),
    dailyTokenLimit: String(tenant.license.daily_token_limit),
    burstRpsLimit: String(tenant.license.burst_rps_limit),
    concurrentSessionsLimit: String(tenant.license.concurrent_sessions_limit),
    overlayKbEnabled: tenant.license.overlay_kb_enabled,
    erpToolsEnabled: tenant.license.erp_tools_enabled,
  }
}

export function buildLicensePayload(form) {
  return {
    status: form.status,
    daily_message_limit: toPositiveNumber(form.dailyMessageLimit, 500),
    daily_token_limit: toPositiveNumber(form.dailyTokenLimit, 500000),
    burst_rps_limit: toPositiveNumber(form.burstRpsLimit, 5),
    concurrent_sessions_limit: toPositiveNumber(form.concurrentSessionsLimit, 10),
    overlay_kb_enabled: form.overlayKbEnabled,
    erp_tools_enabled: form.erpToolsEnabled,
  }
}

export function buildKeyPayload(form) {
  return {
    public_key_pem: form.publicKeyPem.trim(),
    kid: emptyToNull(form.kid),
    algorithm: form.algorithm.trim() || 'RS256',
  }
}

export function buildIngestPayload(form) {
  const payload = {
    limit: emptyNumberToUndefined(form.limit),
    recreate_collection: form.recreateCollection,
    doc_types: parseListInput(form.docTypes),
    erp_version: emptyToNull(form.erpVersion),
    review_statuses: parseListInput(form.reviewStatuses),
    strict_validation: form.strictValidation,
    rebuild_lexical_index: form.rebuildLexicalIndex,
  }

  if (!payload.doc_types.length) {
    delete payload.doc_types
  }
  if (!payload.review_statuses.length) {
    delete payload.review_statuses
  }
  if (!payload.erp_version) {
    delete payload.erp_version
  }
  if (payload.limit === undefined) {
    delete payload.limit
  }

  return payload
}

export function normalizeBaseUrl(value) {
  return value.trim().replace(/\/+$/, '')
}

export function parseListInput(value) {
  return value
    .split(/[\n,]/)
    .map((item) => item.trim())
    .filter(Boolean)
}

export function emptyToNull(value) {
  const trimmed = value.trim()
  return trimmed ? trimmed : null
}

export function formatNumber(value) {
  return new Intl.NumberFormat('it-IT').format(value || 0)
}

export function formatDay(value) {
  return new Intl.DateTimeFormat('it-IT', { month: 'short', day: 'numeric' }).format(new Date(value))
}

export function translateStatus(value) {
  const translations = {
    active: 'Attiva',
    suspended: 'Sospesa',
    quota_exceeded: 'Limite raggiunto',
    standard: 'Standard',
  }
  return translations[value] || value
}

function emptyNumberToUndefined(value) {
  const trimmed = value.trim()
  if (!trimmed) {
    return undefined
  }
  const parsed = Number(trimmed)
  return Number.isFinite(parsed) ? parsed : undefined
}

function toPositiveNumber(value, fallback) {
  const parsed = Number(value)
  return Number.isFinite(parsed) && parsed > 0 ? parsed : fallback
}
