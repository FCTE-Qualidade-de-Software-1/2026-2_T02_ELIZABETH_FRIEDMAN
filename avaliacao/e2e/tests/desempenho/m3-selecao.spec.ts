// M3: tempo de atualização após seleção de turma (Fase 2, M3; Fase 3, seção 1).
// Início: clique no botão "ícone adicionar matéria" da linha da turma.
// Fim: 1º quadro em que (a) a linha mostra "ícone remover matéria", (b) a lista da página
// tem o número esperado de cartões "Código:" e (c) "Gerar Grade" está habilitado.
// A turma é identificada por código da disciplina e número da turma (resolverTurma).
import { test } from '@playwright/test';
import {
  type Cenario, type TurmaRef, abrirBusca, anoPeriodoCorrente, executarSerie, expandirTurma,
  modoDaExecucao, resolverTurma, selecionarTurma, TMAX_MS,
} from './medicao';

const CENARIOS: { cenario: string; anteriores: TurmaRef[]; alvo: TurmaRef }[] = [
  { cenario: 'm3-sem-selecao', anteriores: [], alvo: { codigo: 'PPGPS2475', turma: '01' } },
  { cenario: 'm3-com-selecao', anteriores: [{ codigo: 'PPGPS0156', turma: '02' }],
    alvo: { codigo: 'PPGPS0156', turma: '04' } },
];

for (const s of CENARIOS) {
  test(`M3 ${s.cenario}: seleciona ${s.alvo.codigo}/${s.alvo.turma}`, async ({ page, browser, request }, info) => {
    const m = modoDaExecucao(info);
    test.setTimeout((m.aquecimento + m.medidas) * (TMAX_MS.M3 + 60000));
    const { texto } = await anoPeriodoCorrente(request);
    const anteriores = await Promise.all(s.anteriores.map(t => resolverTurma(request, t)));
    const alvo = await resolverTurma(request, s.alvo);
    const caixas = anteriores.length + 1;

    const c: Cenario = {
      metrica: 'M3', cenario: s.cenario,
      descricao: `Seleção de ${s.alvo.codigo}/${s.alvo.turma}` +
        (anteriores.length ? ` com ${s.anteriores.map(t => `${t.codigo}/${t.turma}`).join(', ')} já selecionada` : ' sem seleções anteriores'),
      esperado: { alvo: s.alvo, anteriores: s.anteriores, cartoes_codigo: caixas, gerar_grade: 'habilitado' },
      arg: { caixas },
      preparar: async (p) => {
        await p.goto('/schedules/home');          // restaura: seleções só vivem no estado do React
        await abrirBusca(p, texto);
        for (const t of anteriores) await selecionarTurma(p, t);
        const linha = await expandirTurma(p, alvo);
        return linha.getByRole('button');
      },
      limpo: async (p) => {
        const linhaSel = await p.evaluate(() => document.querySelectorAll('img[alt="ícone remover matéria"]').length);
        return p.evaluate(({ antes, linhaSel }) => {
          if (document.querySelectorAll('[role=status]').length) return 'há toast na tela';
          const n = [...document.querySelectorAll('span.font-semibold')].filter(e => (e.textContent || '').trim() === 'Código:').length;
          if (n !== antes) return `cartões "Código:" = ${n}, esperado ${antes}`;
          if (linhaSel !== antes) return `turmas marcadas = ${linhaSel}, esperado ${antes}`;
          return null;
        }, { antes: anteriores.length, linhaSel });
      },
      verificar: (arg, a) => {
        const toasts = [...document.querySelectorAll('[role=status]')]
          .map(e => (e.textContent || '').trim()).filter(Boolean);
        if (toasts.length) return { estado: 'erro', motivo: 'toast: ' + toasts.join(' | ') };
        const linha = a.alvo.closest('div.grid');
        const marcada = !!(linha && linha.querySelector('img[alt="ícone remover matéria"]'));
        const n = [...document.querySelectorAll('span.font-semibold')]
          .filter(e => (e.textContent || '').trim() === 'Código:').length;
        const gerar = [...document.querySelectorAll('button')]
          .find(b => (b.textContent || '').trim() === 'Gerar Grade') as HTMLButtonElement | undefined;
        if (n > arg.caixas) return { estado: 'erro', motivo: `cartões "Código:" = ${n}`, observado: { n } };
        if (marcada && n === arg.caixas && gerar && !gerar.disabled) {
          return { estado: 'sucesso', observado: { cartoes: n, gerar: 'habilitado' } };
        }
        return null;
      },
    };
    await executarSerie(c, { page, browser, request, info });
  });
}
