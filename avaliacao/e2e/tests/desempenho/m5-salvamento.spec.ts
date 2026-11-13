// M5: tempo de retorno do salvamento de grade (Fase 2, M5; Fase 3, seção 1).
//
// Modalidade conta: início no clique em "ícone de upload" de uma grade local; fim no 1º
// quadro com o toast "Grade salva com sucesso!". Depois do intervalo, a página é recarregada
// e a grade precisa aparecer em "Grades nuvem" (o tempo dessa verificação não entra em M5).
// Sessão: o próprio fluxo do frontend com o token mock no fragmento (#access_token=...),
// como faria o retorno do Google; o token nunca é gravado nem impresso (ocultar()).
//
// Modalidade navegador: NÃO AVALIADA. Não há ação de salvar nem sinal de conclusão; o
// localStorage é gravado como efeito colateral da geração (M4). Ver Fase 3, seção 4.1.
import { test } from '@playwright/test';
import {
  API, type Cenario, executarSerie, lerTokenMock, modoDaExecucao, ocultar, resolverTurma, TMAX_MS,
} from './medicao';

const GRADE = [{ codigo: 'PPGPS2475', turma: '01' }, { codigo: 'PPGPS2939', turma: '01' }];

test('M5 m5-conta: salva grade fixa na conta de teste', async ({ page, browser, request, context }, info) => {
  const m = modoDaExecucao(info);
  test.setTimeout((m.aquecimento + m.medidas) * (TMAX_MS.M5 + 90000));

  const token = lerTokenMock();
  if (!token) throw new Error('GOOGLE_OAUTH2_MOCK_TOKEN ausente em api/.env do produto: modalidade conta não reproduzível');

  // Grade fixa: gerada pela API a partir das turmas identificadas por código e número.
  const ids = [];
  for (const g of GRADE) ids.push((await resolverTurma(request, g)).id);
  const ger = await (await request.post(`${API}/courses/schedules/generate/`,
    { data: { classes: ids, preference: [1, 1, 1] } })).json();
  if (ger.schedules?.length !== 1) throw new Error('grade fixa de M5 não gerada');
  const grade = ger.schedules[0];

  // Autenticação (fora do intervalo): fluxo do frontend com o token no fragmento.
  try {
    const reg = page.waitForResponse(r => r.url().includes('/users/register/google/'), { timeout: 30000 });
    await page.goto(`/#access_token=${encodeURIComponent(token)}`);
    const st = (await reg).status();
    if (st !== 200) throw new Error(`register/google respondeu ${st}`);
    await page.waitForURL('**/schedules/home', { timeout: 30000 });
  } catch (e: any) {
    throw new Error(ocultar(`login da conta de teste falhou: ${String(e.message).split('\n')[0]}`));
  }
  const ck = (await context.cookies(API)).find(c => c.name === 'refresh');
  if (!ck) throw new Error('cookie refresh não aceito pelo navegador');
  const sessao = `fragmento #access_token (fluxo do frontend); cookie refresh aceito: ` +
    `secure=${ck.secure}, httpOnly=${ck.httpOnly}, sameSite=${ck.sameSite}`;
  console.log(`sessão M5: ${sessao}`);

  const logado = (p: typeof page) => p.locator('button[name="profile"]').waitFor({ timeout: 15000 });

  const c: Cenario = {
    metrica: 'M5', cenario: 'm5-conta',
    descricao: 'Salvamento na conta de teste (user@email.com) de uma grade local fixa',
    esperado: {
      grade: GRADE.map(g => `${g.codigo}/${g.turma}`), sinal: 'toast "Grade salva com sucesso!"',
      persistencia: 'após recarregar, "Grades nuvem" com 1 grade', sessao,
      navegador: 'NÃO AVALIADA: sem ação de salvar nem sinal de conclusão',
    },
    arg: {},
    preparar: async (p) => {
      await p.goto('/schedules/mygrades');
      await logado(p);
      // restaura: nuvem vazia (DELETE das grades da conta) e uma grade local fixa
      const r = await p.evaluate(async ({ api, grade }) => {
        const h = { 'Content-Type': 'application/json' };
        const l = await fetch(`${api}/users/login/`, { method: 'POST', credentials: 'include', headers: h, body: '{}' });
        if (!l.ok) return `login ${l.status}`;
        const auth = { ...h, Authorization: `Bearer ${(await l.json()).access}` };
        const lista = await (await fetch(`${api}/courses/schedules/`, { headers: auth })).json();
        for (const s of lista) {
          const d = await fetch(`${api}/courses/schedules/${s.id}/`, { method: 'DELETE', headers: auth });
          if (d.status !== 204) return `delete ${d.status}`;
        }
        localStorage.setItem('schedules', JSON.stringify([grade]));
        return null;
      }, { api: API, grade });
      if (r) throw new Error(`restauração da conta: ${r}`);
      const nuvem = p.waitForResponse(x => x.url().endsWith('/courses/schedules/') && x.request().method() === 'GET');
      await p.reload();
      await logado(p);
      await nuvem;
      const botao = p.getByRole('button', { name: 'ícone de upload' });
      await botao.waitFor();
      return botao;
    },
    limpo: (p) => p.evaluate(() => {
      if (document.querySelectorAll('[role=status]').length) return 'há toast na tela';
      const hs = [...document.querySelectorAll('h1')].map(e => (e.textContent || '').trim());
      if (hs.includes('Grades nuvem')) return 'há grades na nuvem';
      const loc = [...document.querySelectorAll('h1')].find(e => (e.textContent || '').trim() === 'Grades locais');
      const n = loc && loc.nextElementSibling ? loc.nextElementSibling.children.length : 0;
      return n === 1 ? null : `grades locais = ${n}, esperado 1`;
    }),
    verificar: (_arg, _a) => {
      const toasts = [...document.querySelectorAll('[role=status]')]
        .map(e => (e.textContent || '').trim()).filter(Boolean);
      if (toasts.includes('Grade salva com sucesso!')) return { estado: 'sucesso', observado: { toast: 'Grade salva com sucesso!' } };
      if (toasts.length) return { estado: 'erro', motivo: 'toast: ' + toasts.join(' | ') };
      return null;
    },
    posVerificacao: async (p) => {
      await p.reload();
      await logado(p);
      const h = p.getByRole('heading', { name: 'Grades nuvem' });
      try { await h.waitFor({ timeout: 15000 }); } catch { return 'grade não apareceu em "Grades nuvem" após recarregar'; }
      const n = await h.locator('xpath=following-sibling::div[1]').locator(':scope > div').count();
      return n === 1 ? null : `"Grades nuvem" com ${n} grades, esperado 1`;
    },
  };
  await executarSerie(c, { page, browser, request, info });
});
