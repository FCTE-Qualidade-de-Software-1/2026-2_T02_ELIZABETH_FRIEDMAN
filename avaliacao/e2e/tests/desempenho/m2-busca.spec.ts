// M2: tempo de resposta da busca de disciplinas (Fase 2, M2; Fase 3, seção 1).
// Início: clique no botão "ícone de pesquisa" (a busca só roda no submit; não há debounce).
// Fim: 1º quadro em que a lista mostra exatamente as disciplinas esperadas.
import { test } from '@playwright/test';
import {
  type Cenario, abrirBusca, anoPeriodoCorrente, botaoPesquisa, executarSerie, modoDaExecucao, TMAX_MS,
} from './medicao';

const CENARIOS = [
  { cenario: 'm2-nome', termo: 'seminario', codigos: ['PPGPS0156', 'PPGPS0157', 'PPGPS2989'] },
  { cenario: 'm2-codigo', termo: 'PPGPS2475', codigos: ['PPGPS2475'] },
];

for (const s of CENARIOS) {
  test(`M2 ${s.cenario}: busca "${s.termo}"`, async ({ page, browser, request }, info) => {
    const m = modoDaExecucao(info);
    test.setTimeout((m.aquecimento + m.medidas) * (TMAX_MS.M2 + 60000));
    const { texto } = await anoPeriodoCorrente(request);

    const c: Cenario = {
      metrica: 'M2', cenario: s.cenario,
      descricao: `Busca por ${s.cenario === 'm2-nome' ? 'nome' : 'código'}: termo "${s.termo}", período ${texto}`,
      esperado: { termo: s.termo, disciplinas: s.codigos },
      arg: { codigos: s.codigos },
      preparar: async (p) => {
        await p.goto('/schedules/home');          // restaura: lista de resultados vazia
        await abrirBusca(p, texto);
        await p.getByPlaceholder('Matéria ou Professor...').fill(s.termo);
        return botaoPesquisa(p);
      },
      limpo: (p) => p.evaluate((termo) => {
        if (document.querySelectorAll('section button img[alt="expand icon"]').length) return 'há resultados na tela';
        if (document.querySelectorAll('[role=status]').length) return 'há toast na tela';
        const inp = document.querySelector('input[placeholder="Matéria ou Professor..."]') as HTMLInputElement | null;
        return inp && inp.value === termo ? null : 'termo não preenchido';
      }, s.termo),
      verificar: (arg, _a) => {
        const toasts = [...document.querySelectorAll('[role=status]')]
          .map(e => (e.textContent || '').trim()).filter(Boolean);
        if (toasts.length) return { estado: 'erro', motivo: 'toast: ' + toasts.join(' | ') };
        const bts = [...document.querySelectorAll('section button')]
          .filter(b => b.querySelector('img[alt="expand icon"]')) as HTMLButtonElement[];
        if (!bts.length) return null;
        if (!bts.every(b => b.getBoundingClientRect().height > 0 && !b.disabled)) return null;
        const codigos = bts.map(b => (b.textContent || '').trim().split(' - ').pop()).sort();
        const ok = JSON.stringify(codigos) === JSON.stringify([...arg.codigos].sort());
        return ok ? { estado: 'sucesso', observado: { codigos } }
          : { estado: 'erro', motivo: 'resultado diferente do esperado', observado: { codigos } };
      },
    };
    await executarSerie(c, { page, browser, request, info });
  });
}
