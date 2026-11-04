import { test, expect } from '@playwright/test';

// Smoke do ambiente local (F3-C2): confirma que API e frontend respondem.
// Não é coleta de métrica.

test('API responde o período letivo', async ({ request }) => {
  const r = await request.get('http://localhost:8000/courses/year-period/');
  expect(r.status()).toBe(200);
  expect((await r.json())['year/period']).toHaveLength(2);
});

test('frontend abre a tela inicial', async ({ page }) => {
  await page.goto('/');
  await expect(page.getByText('Continuar como anônimo')).toBeVisible();
});
