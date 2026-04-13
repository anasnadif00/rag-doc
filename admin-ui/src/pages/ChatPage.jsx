import { useEffect, useEffectEvent, useRef, useState } from 'react'

import { GhostButton, PrimaryButton, SectionCard, TextArea } from '../components/ui.jsx'
import { closeChatSession, createWebSocketUrl, issueWsTicket, startWebChatSession } from '../lib/api.js'
import { normalizeBaseUrl } from '../lib/dashboard.js'

const API_BASE_URL = normalizeBaseUrl(import.meta.env.VITE_API_BASE_URL || '')

function normalizeAssistantPayload(payload) {
  return {
    text:
      (typeof payload.answer === 'string' && payload.answer.trim()) ||
      (typeof payload.detail === 'string' && payload.detail.trim()) ||
      'Risposta pronta.',
    steps: Array.isArray(payload.steps)
      ? payload.steps.map((step) => String(step || '').trim()).filter(Boolean)
      : [],
    followUpQuestion:
      typeof payload.follow_up_question === 'string' && payload.follow_up_question.trim()
        ? payload.follow_up_question.trim()
        : '',
    inferenceNotice:
      typeof payload.inference_notice === 'string' && payload.inference_notice.trim()
        ? payload.inference_notice.trim()
        : '',
  }
}

function ChatPage() {
  const socketRef = useRef(null)
  const [sessionId, setSessionId] = useState(null)
  const [messageDraft, setMessageDraft] = useState('')
  const [messages, setMessages] = useState([])
  const [statusMessage, setStatusMessage] = useState('Stiamo preparando la conversazione...')
  const [serviceUnavailable, setServiceUnavailable] = useState('')
  const [busyAction, setBusyAction] = useState('')
  const [isReady, setIsReady] = useState(false)
  const avviaConversazioneIniziale = useEffectEvent(() => {
    void avviaConversazione()
  })

  useEffect(() => {
    avviaConversazioneIniziale()

    return () => {
      const socket = socketRef.current
      if (socket) {
        socketRef.current = null
        socket.close(1000, 'chat-page-unmount')
      }
    }
  }, [])

  function appendMessage(entry) {
    setMessages((current) => [
      ...current,
      {
        id: `${Date.now()}-${Math.random().toString(36).slice(2, 8)}`,
        ...entry,
      },
    ])
  }

  function closeSocket(reason = 'chat-page-reset') {
    const socket = socketRef.current
    if (socket) {
      socketRef.current = null
      socket.close(1000, reason)
    }
  }

  async function avviaConversazione() {
    setBusyAction('start')
    setServiceUnavailable('')
    setStatusMessage('Stiamo preparando la conversazione...')
    setIsReady(false)
    setMessages([])

    try {
      const sessione = await startWebChatSession(API_BASE_URL)
      setSessionId(sessione.session_id)
      await openSocket()
    } catch {
      setSessionId(null)
      setServiceUnavailable('Servizio momentaneamente non disponibile. Riprova tra qualche minuto.')
      setStatusMessage('Al momento non e possibile avviare la chat.')
    } finally {
      setBusyAction('')
    }
  }

  async function openSocket() {
    closeSocket('chat-page-restart')
    setStatusMessage('Connessione in corso...')

    const ticket = await issueWsTicket(API_BASE_URL)
    const url = createWebSocketUrl(API_BASE_URL, `/v1/chat/ws?ticket=${encodeURIComponent(ticket.ticket)}`)
    const socket = new WebSocket(url)
    socketRef.current = socket

    socket.onopen = () => {
      if (socketRef.current !== socket) return
      setStatusMessage('Connessione stabilita. Sto preparando la risposta.')
    }

    socket.onmessage = (event) => {
      if (socketRef.current !== socket) return

      const payload = JSON.parse(event.data)
      if (payload.type === 'ready') {
        setIsReady(true)
        setStatusMessage('Puoi iniziare a scrivere.')
        setSessionId(payload.session_id)
        appendMessage({
          role: 'assistant',
          text: 'Ciao, sono qui per aiutarti. Scrivimi pure la tua richiesta.',
          steps: [],
          followUpQuestion: '',
          inferenceNotice: '',
        })
        return
      }

      if (payload.type === 'error') {
        setStatusMessage('Si e verificato un problema durante la risposta.')
        appendMessage({
          role: 'assistant',
          text: 'Non sono riuscito a completare la risposta. Prova a riformulare la richiesta.',
          steps: [],
          followUpQuestion: '',
          inferenceNotice: '',
        })
        return
      }

      const assistantPayload = normalizeAssistantPayload(payload)
      appendMessage({
        role: 'assistant',
        text: assistantPayload.text,
        steps: assistantPayload.steps,
        followUpQuestion: assistantPayload.followUpQuestion,
        inferenceNotice: assistantPayload.inferenceNotice,
      })
      setStatusMessage('Risposta pronta.')
    }

    socket.onerror = () => {
      if (socketRef.current !== socket) return
      setIsReady(false)
      setStatusMessage('Connessione temporaneamente non disponibile.')
    }

    socket.onclose = () => {
      if (socketRef.current === socket) {
        socketRef.current = null
        setIsReady(false)
        setStatusMessage('La conversazione e stata interrotta.')
      }
    }
  }

  async function handleRestart() {
    if (sessionId) {
      try {
        await closeChatSession(API_BASE_URL, sessionId)
      } catch {
        // Ignore close errors and start a fresh session anyway.
      }
    }
    closeSocket('chat-page-new-session')
    setSessionId(null)
    await avviaConversazione()
  }

  function handleSendMessage(event) {
    event.preventDefault()
    const message = messageDraft.trim()
    if (!message) return

    const socket = socketRef.current
    if (!socket || socket.readyState !== WebSocket.OPEN) {
      setStatusMessage('La chat non e ancora pronta.')
      return
    }

    socket.send(
      JSON.stringify({
        type: 'user_message',
        message,
        screen_context: {},
        retrieval_options: {},
      }),
    )
    appendMessage({ role: 'user', text: message })
    setMessageDraft('')
    setStatusMessage('Messaggio inviato. Attendi la risposta...')
  }

  return (
    <>
      <SectionCard
        eyebrow="Assistenza"
        title="Chat guidata"
        subtitle="Scrivi la tua richiesta e ricevi un aiuto passo dopo passo in modo semplice e immediato."
        actions={
          <GhostButton type="button" onClick={() => void handleRestart()} disabled={busyAction === 'start'}>
            {busyAction === 'start' ? 'Avvio in corso...' : 'Nuova conversazione'}
          </GhostButton>
        }
      >
        <div className="space-y-4">
          <div className="rounded-2xl border border-white/10 bg-white/[0.04] px-4 py-3 text-sm text-stone-200">
            {statusMessage}
          </div>

          {serviceUnavailable ? (
            <div className="rounded-2xl border border-amber-300/25 bg-amber-300/10 px-5 py-5 text-sm text-amber-50">
              {serviceUnavailable}
            </div>
          ) : (
            <div className="space-y-4">
              <div className="min-h-[24rem] space-y-3 rounded-[1.6rem] border border-white/10 bg-black/20 p-4">
                {messages.length ? (
                  messages.map((message) => (
                    <article
                      key={message.id}
                      className={`max-w-[92%] rounded-[1.4rem] border px-4 py-3 shadow-[0_12px_30px_rgba(0,0,0,0.14)] ${
                        message.role === 'user'
                          ? 'ml-auto border-amber-300/25 bg-amber-300/12 text-amber-50'
                          : 'border-white/10 bg-white/[0.05] text-stone-50'
                      }`}
                    >
                      <div className="text-[11px] uppercase tracking-[0.22em] text-stone-400">
                        {message.role === 'user' ? 'Tu' : 'Assistente'}
                      </div>
                      <p className="mt-2 whitespace-pre-wrap text-sm leading-6">{message.text}</p>
                      {message.role === 'assistant' && Array.isArray(message.steps) && message.steps.length ? (
                        <ol className="mt-3 list-decimal space-y-2 pl-5 text-sm leading-6 text-stone-100">
                          {message.steps.map((step, index) => (
                            <li key={`${message.id}-step-${index}`} className="whitespace-pre-wrap">
                              {step}
                            </li>
                          ))}
                        </ol>
                      ) : null}
                      {message.role === 'assistant' && message.followUpQuestion ? (
                        <p className="mt-3 whitespace-pre-wrap text-sm leading-6 text-amber-100">
                          Per continuare: {message.followUpQuestion}
                        </p>
                      ) : null}
                      {message.role === 'assistant' && message.inferenceNotice ? (
                        <p className="mt-3 whitespace-pre-wrap text-sm leading-6 text-stone-300">
                          Nota: {message.inferenceNotice}
                        </p>
                      ) : null}
                    </article>
                  ))
                ) : (
                  <div className="rounded-2xl border border-dashed border-white/10 bg-white/[0.03] px-5 py-10 text-center">
                    <div className="text-lg text-stone-50">Conversazione pronta</div>
                    <p className="mx-auto mt-3 max-w-xl text-sm leading-6 text-stone-400">
                      Appena la connessione sara disponibile potrai scrivere la tua richiesta qui sotto.
                    </p>
                  </div>
                )}
              </div>

              <form className="space-y-3" onSubmit={handleSendMessage}>
                <TextArea
                  label="Il tuo messaggio"
                  value={messageDraft}
                  rows={4}
                  placeholder="Scrivi qui la tua richiesta..."
                  disabled={!isReady || Boolean(serviceUnavailable)}
                  onChange={setMessageDraft}
                />
                <div className="flex flex-wrap gap-3">
                  <PrimaryButton type="submit" disabled={!isReady || Boolean(serviceUnavailable)}>
                    Invia
                  </PrimaryButton>
                  <GhostButton type="button" onClick={() => setMessageDraft('')} disabled={!messageDraft}>
                    Cancella testo
                  </GhostButton>
                </div>
              </form>
            </div>
          )}
        </div>
      </SectionCard>
    </>
  )
}

export default ChatPage
