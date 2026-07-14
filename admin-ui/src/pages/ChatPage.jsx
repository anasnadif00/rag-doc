import {
  useEffect,
  useEffectEvent,
  useLayoutEffect,
  useRef,
  useState,
} from "react";

import {
  GhostButton,
  PrimaryButton,
  SectionCard,
  TextArea,
} from "../components/ui.jsx";
import {
  createWebSocketUrl,
  issueWsTicket,
} from "../lib/api.js";
import { normalizeBaseUrl } from "../lib/dashboard.js";

const API_BASE_URL = normalizeBaseUrl(import.meta.env.VITE_API_BASE_URL || "");

const INITIAL_CHAT_STATUS = {
  state: "connecting",
  title: "Connessione all'assistente",
  detail: "Prepariamo uno spazio sicuro per la conversazione.",
};

const USAGE_LIMIT_REASON_CODES = new Set([
  "daily_message_limit",
  "daily_token_limit",
]);
const USAGE_LIMIT_MESSAGE =
  "Servizio non disponibile: hai superato il limite di utilizzo previsto. Contatta l'amministratore o l'assistenza di sistema.";

function getReasonCode(source) {
  return (
    (source && typeof source.reasonCode === "string" && source.reasonCode) ||
    (source && typeof source.reason_code === "string" && source.reason_code) ||
    ""
  );
}

function isUsageLimitError(source) {
  const reasonCode = getReasonCode(source);
  return (
    USAGE_LIMIT_REASON_CODES.has(reasonCode) ||
    (source && source.status === 429 && !reasonCode)
  );
}

function resolveUnavailableMessage(source) {
  if (isUsageLimitError(source)) {
    return USAGE_LIMIT_MESSAGE;
  }
  return "Servizio momentaneamente non disponibile. Riprova tra qualche minuto.";
}

function resolveUnavailableStatus(source) {
  if (isUsageLimitError(source)) {
    return {
      state: "error",
      title: "Limite di utilizzo raggiunto",
      detail: "Contatta l'amministratore o l'assistenza di sistema.",
    };
  }
  return {
    state: "error",
    title: "Assistente non disponibile",
    detail: "Riprova tra qualche minuto.",
  };
}

function normalizeAssistantPayload(payload) {
  return {
    text:
      (typeof payload.answer === "string" && payload.answer.trim()) ||
      (typeof payload.detail === "string" && payload.detail.trim()) ||
      "Risposta pronta.",
    steps: Array.isArray(payload.steps)
      ? payload.steps.map((step) => String(step || "").trim()).filter(Boolean)
      : [],
    followUpQuestion:
      typeof payload.follow_up_question === "string" &&
      payload.follow_up_question.trim()
        ? payload.follow_up_question.trim()
        : "",
    inferenceNotice:
      typeof payload.inference_notice === "string" &&
      payload.inference_notice.trim()
        ? payload.inference_notice.trim()
        : "",
  };
}

function AssistantThinking() {
  return (
    <article className="chat-thinking" role="status" aria-live="polite">
      <div className="chat-thinking__bot" aria-hidden="true">
        <span className="chat-thinking__orbit" />
        <svg viewBox="0 0 48 48" fill="none">
          <path d="M24 8v5" />
          <circle cx="24" cy="6" r="2" />
          <rect x="10" y="13" width="28" height="23" rx="9" />
          <circle cx="19" cy="24" r="2" />
          <circle cx="29" cy="24" r="2" />
          <path d="M19 30c1.4 1.3 3.1 2 5 2s3.6-.7 5-2M10 22H7v7h3M38 22h3v7h-3" />
        </svg>
      </div>
      <div>
        <div className="text-[11px] uppercase tracking-[0.2em] text-muted">
          Mia
        </div>
        <div className="mt-1 flex items-center gap-2 text-sm text-copy">
          <span>Sto elaborando la risposta</span>
        </div>
      </div>
    </article>
  );
}

function ChatPage({ chatSession, onLogout, onSessionExpired }) {
  const socketRef = useRef(null);
  const composerRef = useRef(null);
  const formRef = useRef(null);
  const messagesEndRef = useRef(null);
  const [sessionId, setSessionId] = useState(null);
  const [messageDraft, setMessageDraft] = useState("");
  const [messages, setMessages] = useState([]);
  const [chatStatus, setChatStatus] = useState(INITIAL_CHAT_STATUS);
  const [serviceUnavailable, setServiceUnavailable] = useState("");
  const [busyAction, setBusyAction] = useState("");
  const [isReady, setIsReady] = useState(false);
  const [isGenerating, setIsGenerating] = useState(false);
  const avviaConversazioneIniziale = useEffectEvent(() => {
    void avviaConversazione();
  });

  useEffect(() => {
    avviaConversazioneIniziale();

    return () => {
      const socket = socketRef.current;
      if (socket) {
        socketRef.current = null;
        socket.close(1000, "chat-page-unmount");
      }
    };
  }, []);

  useEffect(() => {
    function focusComposer(event) {
      if (
        event.key !== "/" ||
        event.ctrlKey ||
        event.altKey ||
        event.metaKey ||
        !isReady ||
        serviceUnavailable
      ) {
        return;
      }

      const activeElement = document.activeElement;
      const isTyping =
        activeElement instanceof HTMLElement &&
        (activeElement.matches("input, textarea, select") ||
          activeElement.isContentEditable);

      if (isTyping) return;

      event.preventDefault();
      composerRef.current?.focus();
    }

    window.addEventListener("keydown", focusComposer);
    return () => window.removeEventListener("keydown", focusComposer);
  }, [isReady, serviceUnavailable]);

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({
      behavior: "smooth",
      block: "nearest",
    });
  }, [messages, isGenerating]);

  useLayoutEffect(() => {
    resizeComposer();
  }, [messageDraft]);

  useEffect(() => {
    function handleViewportResize() {
      resizeComposer();
    }

    window.addEventListener("resize", handleViewportResize);
    return () => window.removeEventListener("resize", handleViewportResize);
  }, []);

  function resizeComposer() {
    const composer = composerRef.current;
    if (!composer) return;

    const maxHeight = Math.max(72, Math.min(176, window.innerHeight * 0.28));
    composer.style.height = "0px";
    const contentHeight = composer.scrollHeight;
    composer.style.height = `${Math.min(contentHeight, maxHeight)}px`;
    composer.style.overflowY = contentHeight > maxHeight ? "auto" : "hidden";
  }

  function appendMessage(entry) {
    setMessages((current) => [
      ...current,
      {
        id: `${Date.now()}-${Math.random().toString(36).slice(2, 8)}`,
        ...entry,
      },
    ]);
  }

  function closeSocket(reason = "chat-page-reset") {
    const socket = socketRef.current;
    if (socket) {
      socketRef.current = null;
      socket.close(1000, reason);
    }
  }

  async function avviaConversazione() {
    setBusyAction("start");
    setServiceUnavailable("");
    setChatStatus(INITIAL_CHAT_STATUS);
    setIsReady(false);
    setIsGenerating(false);
    setMessages([]);

    if (!chatSession?.session_id) {
      setBusyAction("");
      onSessionExpired();
      return;
    }


    try {
      setSessionId(chatSession.session_id);
      await openSocket();
    } catch (error) {
      setSessionId(null);
      if (error.status === 401) {
        onSessionExpired();
        return;
      }
      setServiceUnavailable(resolveUnavailableMessage(error));
      setChatStatus(resolveUnavailableStatus(error));
    } finally {
      setBusyAction("");
    }
  }

  async function openSocket() {
    closeSocket("chat-page-restart");
    setChatStatus({
      state: "connecting",
      title: "Connessione sicura in corso",
      detail: "Manca solo un istante.",
    });

    const ticket = await issueWsTicket(API_BASE_URL);
    const url = createWebSocketUrl(
      API_BASE_URL,
      `/v1/chat/ws?ticket=${encodeURIComponent(ticket.ticket)}`,
    );
    const socket = new WebSocket(url);
    socketRef.current = socket;

    socket.onopen = () => {
      if (socketRef.current !== socket) return;
      setChatStatus({
        state: "connecting",
        title: "Ultimi preparativi",
        detail: "L'assistente sarà pronto a breve.",
      });
    };

    socket.onmessage = (event) => {
      if (socketRef.current !== socket) return;

      const payload = JSON.parse(event.data);
      if (payload.type === "ready") {
        setIsReady(true);
        setIsGenerating(false);
        setChatStatus({
          state: "ready",
          title: "Pronto quando vuoi",
          detail: "Scrivi la tua domanda qui sotto.",
        });
        setSessionId(payload.session_id);
        return;
      }

      if (payload.type === "error") {
        setIsGenerating(false);
        if (isUsageLimitError(payload)) {
          socketRef.current = null;
          socket.close(1000, "usage-limit");
          setIsReady(false);
          setServiceUnavailable(resolveUnavailableMessage(payload));
          setChatStatus(resolveUnavailableStatus(payload));
          return;
        }
        setChatStatus({
          state: "error",
          title: "Non ho completato la risposta",
          detail: "Puoi riprovare o riformulare la domanda.",
        });
        appendMessage({
          role: "assistant",
          text: "Non sono riuscito a completare la risposta. Prova a riformulare la richiesta.",
          steps: [],
          followUpQuestion: "",
          inferenceNotice: "",
        });
        return;
      }

      const assistantPayload = normalizeAssistantPayload(payload);
      appendMessage({
        role: "assistant",
        text: assistantPayload.text,
        steps: assistantPayload.steps,
        followUpQuestion: assistantPayload.followUpQuestion,
        inferenceNotice: assistantPayload.inferenceNotice,
      });
      setIsGenerating(false);
      setChatStatus({
        state: "complete",
        title: "Risposta completata",
        detail: "Puoi continuare la conversazione quando vuoi.",
      });
    };

    socket.onerror = () => {
      if (socketRef.current !== socket) return;
      setIsReady(false);
      setIsGenerating(false);
      setChatStatus({
        state: "error",
        title: "Connessione non disponibile",
        detail: "Controlla la rete e avvia una nuova conversazione.",
      });
    };

    socket.onclose = () => {
      if (socketRef.current === socket) {
        socketRef.current = null;
        setIsReady(false);
        setIsGenerating(false);
        setChatStatus({
          state: "error",
          title: "Conversazione interrotta",
          detail: "Avvia una nuova conversazione per riprendere.",
        });
      }
    };
  }

  async function handleLogout() {
    setBusyAction("logout");
    try {
      await onLogout();
    } finally {
      setBusyAction("");
    }
  }

  async function handleRestart() {
    closeSocket("chat-page-new-session");
    setSessionId(chatSession?.session_id || sessionId || null);
    await avviaConversazione();
  }

  function handleSendMessage(event) {
    event.preventDefault();
    const message = messageDraft.trim();
    if (!message || isGenerating) return;

    const socket = socketRef.current;
    if (!socket || socket.readyState !== WebSocket.OPEN) {
      setChatStatus({
        state: "error",
        title: "La chat non è ancora pronta",
        detail: "Attendi la connessione prima di inviare.",
      });
      return;
    }

    socket.send(
      JSON.stringify({
        type: "user_message",
        message,
        screen_context: {},
        retrieval_options: {},
      }),
    );
    appendMessage({ role: "user", text: message });
    setMessageDraft("");
    setIsGenerating(true);
    setChatStatus({
      state: "thinking",
      title: "Sto preparando la risposta",
      detail: "Analizzo la richiesta e cerco le informazioni più utili.",
    });
  }

  function handleComposerKeyDown(event) {
    if (
      event.key !== "Enter" ||
      event.shiftKey ||
      event.nativeEvent.isComposing
    ) {
      return;
    }

    event.preventDefault();
    if (!isGenerating && messageDraft.trim()) {
      formRef.current?.requestSubmit();
    }
  }

  return (
    <div className="chat-page">
        <SectionCard
          title={
            <span className="chat-title">
              <span className="chat-title__name">MIA</span>
            </span>
          }
          subtitle="Fai una domanda e ricevi una risposta dall'assistente virtuale."
          className="chat-panel"
          contentClassName="chat-panel__body"
          actions={
            <div className="flex flex-wrap items-center justify-end gap-2">
              <div className="hidden min-w-0 text-right sm:block">
                <div className="max-w-48 truncate text-xs uppercase tracking-[0.18em] text-muted">
                  {chatSession?.tenant_display_name || chatSession?.tenant_code || "Chat"}
                </div>
                <div className="max-w-48 truncate text-sm text-ink">
                  {chatSession?.display_name || chatSession?.username || "Utente"}
                </div>
              </div>
              <GhostButton
                type="button"
                className="chat-new-button"
                onClick={() => void handleRestart()}
                disabled={busyAction === "start" || busyAction === "logout"}
                aria-label="Nuova chat"
                title="Nuova chat"
              >
                <svg viewBox="0 0 24 24" fill="none" aria-hidden="true">
                  <path d="M12 3H5.75A2.75 2.75 0 0 0 3 5.75v12.5A2.75 2.75 0 0 0 5.75 21h12.5A2.75 2.75 0 0 0 21 18.25V12" />
                  <path d="M17.9 3.55a1.55 1.55 0 0 1 2.2 2.2l-8.8 8.8a2 2 0 0 1-.86.51l-2.6.72.72-2.6a2 2 0 0 1 .51-.86Z" />
                  <path d="m16.5 4.95 2.55 2.55" />
                </svg>
                <span>Nuova chat</span>
              </GhostButton>
              <GhostButton
                type="button"
                className="chat-action-button"
                onClick={() => void handleLogout()}
                disabled={busyAction === "logout"}
              >
                {busyAction === "logout" ? "Uscita..." : "Esci"}
              </GhostButton>
            </div>
          }
        >
          <div className="chat-workspace">
            <p
              className="sr-only"
              role="status"
              aria-live="polite"
              aria-atomic="true"
            >
              {chatStatus.title}. {chatStatus.detail}
            </p>

            <div className="chat-conversation">
              <div className="chat-messages">
                {serviceUnavailable ? (
                  <div className="rounded-2xl border border-accent-soft bg-accent-soft px-5 py-5 text-sm text-accent-ink">
                    {serviceUnavailable}
                  </div>
                ) : messages.length ? (
                  messages.map((message) => (
                    <article
                      key={message.id}
                      className={`chat-message ${
                        message.role === "user"
                          ? "chat-message--user"
                          : "chat-message--assistant"
                      }`}
                    >
                      <div className="text-[11px] uppercase tracking-[0.22em] text-muted">
                        {message.role === "user" ? "Tu" : "Mia"}
                      </div>
                      <p className="mt-1.5 whitespace-pre-wrap text-[13px] leading-5">
                        {message.text}
                      </p>
                      {message.role === "assistant" &&
                      Array.isArray(message.steps) &&
                      message.steps.length ? (
                        <ol className="mt-3 list-decimal space-y-2 pl-5 text-[13px] leading-5 text-copy">
                          {message.steps.map((step, index) => (
                            <li
                              key={`${message.id}-step-${index}`}
                              className="whitespace-pre-wrap"
                            >
                              {step}
                            </li>
                          ))}
                        </ol>
                      ) : null}
                      {message.role === "assistant" &&
                      message.followUpQuestion ? (
                        <p className="mt-3 whitespace-pre-wrap text-[13px] leading-5 text-accent-ink">
                          Per continuare: {message.followUpQuestion}
                        </p>
                      ) : null}
                      {message.role === "assistant" &&
                      message.inferenceNotice ? (
                        <p className="mt-3 whitespace-pre-wrap text-[13px] leading-5 text-copy">
                          Nota: {message.inferenceNotice}
                        </p>
                      ) : null}
                    </article>
                  ))
                ) : (
                  <div className="chat-empty">
                    <div className="chat-empty__icon" aria-hidden="true">
                      <svg viewBox="0 0 24 24" fill="none">
                        <path d="M12 3.5c.45 4.7 2.8 7.05 7.5 7.5-4.7.45-7.05 2.8-7.5 7.5-.45-4.7-2.8-7.05-7.5-7.5 4.7-.45 7.05-2.8 7.5-7.5Z" />
                        <path d="M19 3v3M20.5 4.5h-3" />
                      </svg>
                    </div>
                    <div className="chat-empty__title">
                      {isReady ? "Come posso aiutarti?" : "Prepariamo la chat"}
                    </div>
                    <p className="chat-empty__copy">
                      {isReady
                        ? "Scrivi una richiesta qui sotto per iniziare."
                        : "Manca solo un istante."}
                    </p>
                  </div>
                )}
                {!serviceUnavailable && isGenerating ? (
                  <AssistantThinking />
                ) : null}
                <div ref={messagesEndRef} />
              </div>

              <form
                ref={formRef}
                className="chat-composer space-y-2.5"
                onSubmit={handleSendMessage}
              >
                <TextArea
                  value={messageDraft}
                  rows={1}
                  placeholder="Scrivi qui la tua richiesta..."
                  disabled={!isReady || Boolean(serviceUnavailable)}
                  onChange={setMessageDraft}
                  onKeyDown={handleComposerKeyDown}
                  textareaRef={composerRef}
                  ariaDescribedBy="chat-shortcuts"
                  ariaKeyShortcuts="/ Enter Shift+Enter"
                />
                <div className="flex flex-col gap-2.5 sm:flex-row sm:items-center sm:justify-between">
                  <div className="flex flex-wrap gap-2">
                    <PrimaryButton
                      type="submit"
                      className="chat-action-button"
                      disabled={
                        !isReady ||
                        Boolean(serviceUnavailable) ||
                        isGenerating ||
                        !messageDraft.trim()
                      }
                      aria-keyshortcuts="Enter"
                    >
                      {isGenerating ? "Elaborazione..." : "Invia"}
                    </PrimaryButton>
                    <GhostButton
                      type="button"
                      className="chat-action-button"
                      onClick={() => setMessageDraft("")}
                      disabled={!messageDraft}
                    >
                      Cancella testo
                    </GhostButton>
                  </div>
                  <div
                    id="chat-shortcuts"
                    className="chat-shortcuts"
                    aria-label="Scorciatoie da tastiera"
                  >
                    <span>
                      <kbd>/</kbd> Scrivi
                    </span>
                    <span>
                      <kbd>Invio</kbd> Invia
                    </span>
                    <span>
                      <kbd>Maiusc</kbd> + <kbd>Invio</kbd> A capo
                    </span>
                  </div>
                </div>
              </form>
            </div>
          </div>
        </SectionCard>
      </div>
  );
}

export default ChatPage;
