import { defineConfig, devices } from '@playwright/test';

// Os roteiros de desempenho (M2–M5) são opt-in: o projeto `piloto` só existe com PILOTO=1
// e o `coleta` só com COLETA=1 (scripts `npm run piloto` / `npm run coleta`). Sem essas
// variáveis, `npx playwright test` roda apenas o smoke.
const PILOTO = process.env.PILOTO === '1';
const COLETA = process.env.COLETA === '1';
if (PILOTO && COLETA) throw new Error('use PILOTO=1 ou COLETA=1, não os dois');
if ((PILOTO || COLETA) && !process.env.RODADA) {
  // carimbo único da rodada, herdado pelo processo do worker
  const d = new Date(), p = (n: number) => String(n).padStart(2, '0');
  process.env.RODADA = `${d.getFullYear()}${p(d.getMonth() + 1)}${p(d.getDate())}-${p(d.getHours())}${p(d.getMinutes())}`;
}

// Sem trace, vídeo ou screenshot automático: são sobrecarga no intervalo medido.
const desempenho = {
  ...devices['Desktop Chrome'],
  trace: 'off' as const, video: 'off' as const, screenshot: 'off' as const,
  actionTimeout: 15000, navigationTimeout: 30000,
};

// Execução sequencial e sem novas tentativas (Fase 2, pendência 3).
export default defineConfig({
  testDir: './tests',
  workers: 1,
  fullyParallel: false,
  retries: 0,
  reporter: [['list'], ['html', { open: 'never' }]],
  use: {
    baseURL: 'http://localhost:3000',
    trace: 'retain-on-failure',
    screenshot: 'only-on-failure',
  },
  projects: [
    { name: 'chromium', testIgnore: '**/desempenho/**', use: { ...devices['Desktop Chrome'] } },
    ...(PILOTO ? [{ name: 'piloto', testMatch: 'desempenho/**/*.spec.ts', use: desempenho, metadata: { modo: 'piloto' } }] : []),
    ...(COLETA ? [{ name: 'coleta', testMatch: 'desempenho/**/*.spec.ts', use: desempenho, metadata: { modo: 'coleta' } }] : []),
  ],
});
