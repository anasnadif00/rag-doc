import { defineConfig, loadEnv } from 'vite'
import react from '@vitejs/plugin-react'
import tailwindcss from '@tailwindcss/vite'

export default defineConfig(({ mode }) => {
  const env = loadEnv(mode, '.', '')
  const proxyTarget = env.VITE_PROXY_TARGET || 'http://localhost:8000'

  return {
    base: '/',
    plugins: [react(), tailwindcss()],
    server: {
      host: '0.0.0.0',
      port: 5173,
      proxy: {
        '/health': {
          target: proxyTarget,
          changeOrigin: true,
        },
        '/ingest': {
          target: proxyTarget,
          changeOrigin: true,
        },
        '/query': {
          target: proxyTarget,
          changeOrigin: true,
        },
        '/v1': {
          target: proxyTarget,
          changeOrigin: true,
          ws: true,
        },
        '/docs': {
          target: proxyTarget,
          changeOrigin: true,
        },
        '/redoc': {
          target: proxyTarget,
          changeOrigin: true,
        },
        '/openapi.json': {
          target: proxyTarget,
          changeOrigin: true,
        },
      },
    },
  }
})
