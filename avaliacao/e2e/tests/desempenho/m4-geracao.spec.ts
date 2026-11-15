// M4: tempo de geração de grades (Fase 2, M4; Fase 3, seção 1).
// Início: clique em "Gerar" no modal "Período de preferência" (preferências padrão 1/1/1).
// Fim: 1º quadro em /schedules/mygrades, sem a tela de carregamento, com o título
// "Grades locais" e o número esperado de grades (inclui o setTimeout de 500 ms do produto).
// Quantidades conferidas pelo ScheduleGenerator: avaliacao/massa/m4_combinacoes.py.
import { test } from '@playwright/test';
import {
  type Cenario, type TurmaRef, abrirBusca, anoPeriodoCorrente, executarSerie, modoDaExecucao,
  resolverTurma, selecionarTurma, TMAX_MS,
} from './medicao';

const t = (codigo: string, ...turmas: string[]): TurmaRef[] => turmas.map(turma => ({ codigo, turma }));

const CENARIOS = [
  {
    cenario: 'm4-a',
    turmas: [...t('PPGPS2475', '01'), ...t('PPGPS2939', '01')],
    disciplinas: 2, candidatas: 1, validas: 1, exibidas: 1,
  },
  {
    cenario: 'm4-b',
    turmas: [...t('PPGPS0156', '02', '03', '04', '05'), ...t('PPGPS0161', '01', '02', '03', '04'),
      ...t('PPGPS0163', '01', '02'), ...t('PPGPS0165', '01', '02', '03', '05'),
      ...t('PPGPS2475', '01'), ...t('PPGPS2939', '01')],
    // 76 válidas pelo gerador; a API devolve no máximo 5 (MAXIMUM_RETURNED_SCHEDULES).
    disciplinas: 6, candidatas: 128, validas: 76, exibidas: 5,
  },
];

for (const s of CENARIOS) {
  test(`M4 ${s.cenario}: ${s.turmas.length} turmas`, async ({ page, browser, request }, info) => {
    const m = modoDaExecucao(info);
    test.setTimeout((m.aquecimento + m.medidas) * (TMAX_MS.M4 + 120000));
    const { texto } = await anoPeriodoCorrente(request);
    const turmas = [];
    for (const x of s.turmas) turmas.push(await resolverTurma(request, x));

    const c: Cenario = {
      metrica: 'M4', cenario: s.cenario,
      descricao: `Geração com ${s.disciplinas} disciplinas e ${s.turmas.length} turmas, preferências 1/1/1`,
      esperado: {
        turmas: s.turmas.map(x => `${x.codigo}/${x.turma}`), disciplinas: s.disciplinas,
        combinacoes_candidatas: s.candidatas, combinacoes_validas_gerador: s.validas, grades_exibidas: s.exibidas,
      },
      arg: { grades: s.exibidas },
      preparar: async (p) => {
        // restaura: sem grades locais (a geração soma às existentes) e sem seleções
        await p.goto('/schedules/home');
        await p.evaluate(() => localStorage.removeItem('schedules'));
        await p.reload();
        await abrirBusca(p, texto);
        for (const x of turmas) await selecionarTurma(p, x);
        await p.getByRole('button', { name: 'Buscar matéria' }).click();   // fecha o painel
        await p.locator('section select').waitFor({ state: 'detached' });
        await p.getByRole('button', { name: 'Gerar Grade' }).click();
        await p.getByText('Período de preferência').waitFor();
        return p.getByRole('button', { name: 'Gerar', exact: true });
      },
      limpo: (p) => p.evaluate((n) => {
        if (location.pathname !== '/schedules/home') return `página ${location.pathname}`;
        if (JSON.parse(localStorage.getItem('schedules') || '[]').length) return 'há grades locais';
        if (document.querySelectorAll('[role=status]').length) return 'há toast na tela';
        const c = [...document.querySelectorAll('span.font-semibold')].filter(e => (e.textContent || '').trim() === 'Código:').length;
        return c === n ? null : `cartões "Código:" = ${c}, esperado ${n}`;
      }, turmas.length),
      verificar: (arg, _a) => {
        const toasts = [...document.querySelectorAll('[role=status]')]
          .map(e => (e.textContent || '').trim()).filter(Boolean);
        if (toasts.length) return { estado: 'erro', motivo: 'toast: ' + toasts.join(' | ') };
        if (location.pathname !== '/schedules/mygrades') return null;
        if (document.querySelector('[class*="loading_screen"]')) return null;
        const h = [...document.querySelectorAll('h1')].find(e => (e.textContent || '').trim() === 'Grades locais');
        if (!h || !h.nextElementSibling) return null;
        const n = h.nextElementSibling.children.length;
        const ls = JSON.parse(localStorage.getItem('schedules') || '[]').length;
        if (n === arg.grades && ls === arg.grades) return { estado: 'sucesso', observado: { grades: n } };
        return { estado: 'erro', motivo: `grades exibidas ${n}, no localStorage ${ls}, esperado ${arg.grades}`, observado: { n, ls } };
      },
    };
    await executarSerie(c, { page, browser, request, info });
  });
}
