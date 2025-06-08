import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vitejs.dev/config/
export default defineConfig(({ command }) => {
  if (command === 'serve') {
    // DEV-сервер (npm run dev)
    return {
      plugins: [react()],
      server: {
        port: 5173,
        proxy: {
          '/api': {
            target: 'http://localhost:5000', // backend
            changeOrigin: true,
          }
        }
      }
    }
  } else {
    // PROD-сборка (npm run build)
    return {
      plugins: [react()],
      build: {
        outDir: 'dist', // куда собрать
        emptyOutDir: true,
      }
    }
  }
})
