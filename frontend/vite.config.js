import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// Railway + GitHub deploy-kompatibilis build
export default defineConfig({
  plugins: [react()],
  build: {
    outDir: 'dist',
  },
  server: {
    port: 3000,
  }
})
