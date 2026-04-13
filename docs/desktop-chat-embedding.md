# Desktop Chat Embedding

## Recommended Host

Use a Chromium-based embedded browser for the BC4J/Swing client.

- Preferred options: JCEF or Edge WebView2 through a Java bridge
- Avoid passing tenant secrets or JWTs in URL query params
- Inject the bootstrap token through a host bridge after the hosted page loads

## Hosted Shell Contract

The hosted page lives at `/chat` and exposes:

```javascript
window.bootstrapChat({
  bootstrapToken: "<erp-signed-jwt>",
  screenContext: {
    application: "ERP",
    module: "Contabilita",
    screen_id: "FAT-001"
  }
})
```

The page will:

1. `POST /v1/auth/bootstrap`
2. store the short-lived session JWT in memory only
3. `POST /v1/chat/ws-ticket`
4. open `WSS /v1/chat/ws?ticket=...`

## Swing / BC4J Sketch

```java
String bootstrapJwt = erpSigner.issueBootstrapJwt(
    tenantId,
    currentUserId,
    currentRoles,
    currentMaskId,
    List.of("chat:use")
);

String screenContextJson = objectMapper.writeValueAsString(screenContext);

embeddedBrowser.loadURL("https://assist.example.com/chat");
embeddedBrowser.onPageLoadFinished(() -> {
    embeddedBrowser.executeJavaScript(
        "window.bootstrapChat({" +
        "bootstrapToken: " + toJsString(bootstrapJwt) + "," +
        "screenContext: " + screenContextJson +
        "});"
    );
});
```

## Security Notes

- Keep bootstrap JWT expiry at 60-120 seconds
- Keep the tenant private key on-prem only
- Use the cloud-issued session JWT only for API calls to this service
- WebSocket tickets are single-use and short-lived
