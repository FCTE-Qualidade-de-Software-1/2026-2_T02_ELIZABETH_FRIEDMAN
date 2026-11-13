// Protocolo de medição de M2–M5 (Fase 2, seção 3.1; Fase 3, seção 1).
//
// - Instante inicial: Event.timeStamp do clique confiável no elemento que dispara a ação,
//   capturado na página. Mesmo relógio de performance.now() (origem: timeOrigin da página).
// - Instante final: performance.now() no primeiro quadro (requestAnimationFrame) em que o
//   sinal de conclusão está completo. A espera é armada ANTES do clique, para não perder
//   quadros; o sinal só é aceito depois que t0 existe.
// - Expiração: performance.now() - t0 > Tmax, no mesmo relógio.
// - Erros e expirações entram no CSV sem duração e sem nova tentativa; uma tentativa que
//   falha não interrompe a série.
import { execSync } from 'node:child_process';
import fs from 'node:fs';
import path from 'node:path';
import type { APIRequestContext, Browser, Locator, Page, TestInfo } from '@playwright/test';

export const API = 'http://localhost:8000';
export const VERSAO_SISTEMA = '3d399e7';
export const PRODUTO_DIR = process.env.PRODUTO_DIR
  ?? path.resolve(__dirname, '../../../../../2023-2-SuaGradeUnB');
const RESULTADOS = path.resolve(__dirname, '../../../resultados/desempenho');

export const CABECALHO = [
  'métrica', 'cenário', 'ambiente', 'versão do sistema', 'data', 'número da tentativa',
  'aquecimento', 'instante inicial', 'instante final', 'duração (ms)', 'estado',
  'referência à evidência',
];

// Tempo máximo de espera por operação (Fase 3, seção 1), estritamente maior que L_j.
export const TMAX_MS = { M2: 10000, M3: 5000, M4: 30000, M5: 10000 } as const;
export const L_MS = { M2: 2000, M3: 1000, M4: 10000, M5: 2000 } as const;
export type Metrica = keyof typeof TMAX_MS;
export type Estado = 'sucesso' | 'erro' | 'expiração';

// Função executada na página a cada quadro, depois do clique.
// Recebe o argumento do cenário e o estado armado (alvo, t0); devolve null enquanto a
// operação não terminou, ou { estado, motivo?, observado? }.
export type Verificador = (arg: any, a: { t0: number; alvo: Element }) =>
  null | { estado: 'sucesso' | 'erro'; motivo?: string; observado?: unknown };

export interface Cenario {
  metrica: Metrica;
  cenario: string;           // ex.: 'm2-nome'
  descricao: string;
  esperado: Record<string, unknown>;
  // Restaura o estado e prepara a tentativa (fora do intervalo medido).
  // Devolve o elemento que será clicado.
  preparar: (page: Page) => Promise<Locator>;
  // Confere, antes do clique, que não há sinal de conclusão de tentativa anterior.
  // Devolve null se o estado está limpo, ou o motivo.
  limpo: (page: Page) => Promise<string | null>;
  verificar: Verificador;
  arg: unknown;
  // Verificação depois do intervalo medido (M5: persistência). Devolve null ou o motivo.
  posVerificacao?: (page: Page) => Promise<string | null>;
}

export interface Modo {
  modo: 'piloto' | 'coleta';
  aquecimento: number;
  medidas: number;
  tmaxSobrescrito?: number;
}

export function modoDaExecucao(info: TestInfo): Modo {
  const modo = (info.project.metadata as { modo?: string }).modo;
  const sobrescrito = process.env.TMAX_MS ? Number(process.env.TMAX_MS) : undefined;
  if (modo === 'coleta') {
    if (sobrescrito !== undefined) throw new Error('TMAX_MS não é permitido na coleta formal');
    return { modo, aquecimento: 2, medidas: 30 };
  }
  if (modo === 'piloto') {
    const medidas = Number(process.env.PILOTO_MEDIDAS ?? 3);
    return { modo, aquecimento: 1, medidas, tmaxSobrescrito: sobrescrito };
  }
  throw new Error('roteiro de desempenho fora dos projetos piloto/coleta');
}

// ---------- segredo da conta de teste (M5) ----------

let tokenMock: string | undefined;
export function lerTokenMock(): string | undefined {
  if (tokenMock !== undefined) return tokenMock || undefined;
  try {
    const env = fs.readFileSync(path.join(PRODUTO_DIR, 'api/.env'), 'utf8');
    const m = env.match(/^GOOGLE_OAUTH2_MOCK_TOKEN=(.*)$/m);
    tokenMock = m ? m[1].trim().replace(/^["']|["']$/g, '') : '';
  } catch { tokenMock = ''; }
  return tokenMock || undefined;
}
// Remove o token mock de qualquer texto gravado em arquivo ou impresso.
export function ocultar(texto: string): string {
  const t = lerTokenMock();
  return t ? texto.split(t).join('<token-mock>').split(encodeURIComponent(t)).join('<token-mock>') : texto;
}

// ---------- arquivos de saída ----------

function pastaRodada(m: Modo): string {
  const sufixo = m.tmaxSobrescrito !== undefined ? `-tmax${m.tmaxSobrescrito}` : '';
  const dir = path.join(RESULTADOS, m.modo, `${process.env.RODADA}${sufixo}`);
  fs.mkdirSync(path.join(dir, 'evidencias'), { recursive: true });
  return dir;
}

function csv(v: unknown): string {
  const s = v === undefined || v === null ? '' : String(v);
  return /[",\n]/.test(s) ? `"${s.replace(/"/g, '""')}"` : s;
}

function dataLocal(): string {
  const d = new Date();
  const off = -d.getTimezoneOffset();
  const p = (n: number) => String(Math.floor(Math.abs(n))).padStart(2, '0');
  return `${d.getFullYear()}-${p(d.getMonth() + 1)}-${p(d.getDate())}T${p(d.getHours())}:` +
    `${p(d.getMinutes())}:${p(d.getSeconds())}${off >= 0 ? '+' : '-'}${p(off / 60)}:${p(off % 60)}`;
}

function sh(cmd: string): string {
  try { return execSync(cmd, { encoding: 'utf8', stdio: ['ignore', 'pipe', 'pipe'] }).trim(); }
  catch (e: any) { return `falhou: ${String(e.message).split('\n')[0]}`; }
}

async function intervaloQuadros(page: Page): Promise<{ min: number; mediana: number; max: number }> {
  return page.evaluate(() => new Promise(resolve => {
    const t: number[] = [];
    const f = (x: number) => {
      t.push(x);
      if (t.length < 61) requestAnimationFrame(f);
      else {
        const d = t.slice(1).map((v, i) => v - t[i]).sort((a, b) => a - b);
        const r = (n: number) => Math.round(n * 10) / 10;
        resolve({ min: r(d[0]), mediana: r(d[30]), max: r(d[d.length - 1]) });
      }
    };
    requestAnimationFrame(f);
  }));
}

async function gravarMetadados(dir: string, m: Modo, c: Cenario, tmax: number,
  browser: Browser, request: APIRequestContext, page: Page) {
  const arq = path.join(dir, 'metadados.json');
  const meta = fs.existsSync(arq) ? JSON.parse(fs.readFileSync(arq, 'utf8')) : {
    modo: m.modo,
    observacao: m.modo === 'piloto'
      ? 'PILOTO: verificação do método; não integra as 30 tentativas medidas (Fase 2, 3.2, pendência 4).'
      : 'Coleta formal (Fase 2, 3.1).',
    rodada: path.basename(dir),
    inicio: dataLocal(),
    produto: {
      repositorio: 'unb-mds/2023-2-SuaGradeUnB',
      commit: sh(`git -C "${PRODUTO_DIR}" rev-parse HEAD`),
      alteracoes_rastreadas: sh(`git -C "${PRODUTO_DIR}" status --short --untracked-files=no`) || 'nenhuma',
    },
    playwright: require('@playwright/test/package.json').version,
    chromium: browser.version(),
    headless: true,
    dispositivo: 'Desktop Chrome (Playwright devices), viewport 1280x720',
    config: { workers: 1, fullyParallel: false, retries: 0, trace: 'off', screenshot: 'manual', video: 'off' },
    massa: {
      year_period: await request.get(`${API}/courses/year-period/`).then(r => r.json()).catch(() => 'falhou'),
      fonte: 'avaliacao/massa/seed_referencia.py (depto 1499, 14 disciplinas, 43 turmas)',
    },
    docker_ps: sh("docker ps --format '{{.Names}}\\t{{.Image}}\\t{{.Status}}'").split('\n'),
    free_h: sh('free -h').split('\n'),
    host: { node: process.version, uname: sh('uname -srm') },
    mecanismo: 'Início: Event.timeStamp do clique confiável; fim: performance.now() no 1º quadro ' +
      '(requestAnimationFrame) com o sinal completo; mesmo relógio da página.',
    cenarios: {},
  };
  meta.cenarios[c.cenario] = {
    metrica: c.metrica, descricao: c.descricao, esperado: c.esperado,
    tmax_ms: tmax, L_ms: L_MS[c.metrica],
    aquecimento: m.aquecimento, medidas: m.medidas,
    intervalo_quadros_ms: await intervaloQuadros(page).catch(() => 'falhou'),
  };
  fs.writeFileSync(arq, ocultar(JSON.stringify(meta, null, 2)) + '\n');
}

// ---------- uma tentativa ----------

interface Resultado {
  estado: Estado; t0?: number; tFim?: number; motivo?: string; observado?: unknown;
}

function expressaoEspera(verificar: Verificador, arg: unknown, tmax: number): string {
  return `(() => {
    const a = window.__aval;
    if (!a || a.t0 === null) return false;
    const agora = performance.now();
    const r = (${verificar.toString()})(${JSON.stringify(arg)}, a);
    if (r) return Object.assign({ t: agora, t0: a.t0 }, r);
    if (agora - a.t0 > ${tmax}) return { estado: 'expiração', t: agora, t0: a.t0, motivo: 'Tmax ${tmax} ms excedido' };
    return false;
  })()`;
}

async function medirUma(page: Page, c: Cenario, tmax: number): Promise<Resultado> {
  // 1. Restauração e preparação (fora do intervalo).
  let alvo: Locator;
  try {
    alvo = await c.preparar(page);
    const sujo = await c.limpo(page);
    if (sujo) return { estado: 'erro', motivo: `preparação: estado não limpo (${sujo})` };
    const h = await alvo.elementHandle({ timeout: 10000 });
    if (!h) return { estado: 'erro', motivo: 'preparação: alvo não encontrado' };
    await h.evaluate((el) => {
      const w = window as any;
      w.__aval = { t0: null, alvo: el };
      el.addEventListener('click', (e) => {
        if (e.isTrusted && w.__aval.t0 === null) w.__aval.t0 = e.timeStamp;
      }, { capture: true });
    });
  } catch (e: any) {
    return { estado: 'erro', motivo: `preparação: ${String(e.message).split('\n')[0]}` };
  }

  // 2. Intervalo medido: espera armada antes do clique.
  const espera = page.waitForFunction(expressaoEspera(c.verificar, c.arg, tmax), undefined,
    { polling: 'raf', timeout: tmax + 5000 })
    .then(h => h.jsonValue() as Promise<any>)
    .catch((e: Error) => ({ falhaEspera: String(e.message).split('\n')[0] }));
  try {
    await alvo.click({ timeout: 10000 });
  } catch (e: any) {
    await espera;
    return { estado: 'erro', motivo: `clique falhou: ${String(e.message).split('\n')[0]}` };
  }
  const r = await espera;
  if (r.falhaEspera) {
    const t0 = await page.evaluate(() => (window as any).__aval?.t0 ?? null).catch(() => null);
    if (t0 === null) return { estado: 'erro', motivo: `clique não registrado na página (${r.falhaEspera})` };
    return { estado: 'expiração', t0, motivo: `guarda externa: ${r.falhaEspera}` };
  }
  const res: Resultado = { estado: r.estado, t0: r.t0, tFim: r.t, motivo: r.motivo, observado: r.observado };
  if (res.estado === 'sucesso' && !(res.tFim! > res.t0!)) {
    return { ...res, estado: 'erro', motivo: 'sinal de fim não posterior a t0' };
  }

  // 3. Verificação posterior (não entra na métrica).
  if (res.estado === 'sucesso' && c.posVerificacao) {
    try {
      const falha = await c.posVerificacao(page);
      if (falha) return { ...res, estado: 'erro', motivo: `persistência: ${falha}` };
    } catch (e: any) {
      return { ...res, estado: 'erro', motivo: `persistência: ${String(e.message).split('\n')[0]}` };
    }
  }
  return res;
}

// ---------- série completa ----------

export async function executarSerie(c: Cenario, opts: {
  page: Page; browser: Browser; request: APIRequestContext; info: TestInfo;
}) {
  const m = modoDaExecucao(opts.info);
  const tmax = m.tmaxSobrescrito ?? TMAX_MS[c.metrica];
  if (m.modo === 'coleta' && !(tmax > L_MS[c.metrica])) throw new Error('Tmax deve ser > L_j');
  const dir = pastaRodada(m);
  const arqCsv = path.join(dir, `${c.cenario}.csv`);
  const arqEvid = path.join(dir, 'evidencias.jsonl');
  fs.writeFileSync(arqCsv, CABECALHO.map(csv).join(',') + '\n');

  let page = opts.page;
  await page.goto('/');
  await gravarMetadados(dir, m, c, tmax, opts.browser, opts.request, page);
  const ambiente = `local Docker Compose (db, redis, api, web); Chromium ${opts.browser.version()} headless; ${m.modo}`;

  const total = m.aquecimento + m.medidas;
  const contagem: Record<string, number> = {};
  for (let i = 1; i <= total; i++) {
    const aquecimento = i <= m.aquecimento;
    const n = aquecimento ? i : i - m.aquecimento;
    const id = `${c.cenario}-${aquecimento ? 'aq' : ''}${n}`;
    if (page.isClosed()) page = await page.context().newPage();
    const r = await medirUma(page, c, tmax);
    const data = dataLocal();

    let ref = `evidencias.jsonl#${id}`;
    if ((!aquecimento && n === 1) || r.estado !== 'sucesso') {
      const png = `evidencias/${id}.png`;
      await page.screenshot({ path: path.join(dir, png) }).then(() => { ref += `; ${png}`; }).catch(() => {});
    }
    const fmt = (x?: number) => (x === undefined ? '' : x.toFixed(1));
    const linha = [
      c.metrica, c.cenario, ambiente, VERSAO_SISTEMA, data, n, aquecimento ? 'sim' : 'não',
      fmt(r.t0), fmt(r.tFim),
      r.estado === 'sucesso' ? (r.tFim! - r.t0!).toFixed(1) : '',
      r.estado, ref,
    ];
    fs.appendFileSync(arqCsv, ocultar(linha.map(csv).join(',')) + '\n');
    fs.appendFileSync(arqEvid, ocultar(JSON.stringify({
      id, metrica: c.metrica, cenario: c.cenario, tentativa: n, aquecimento, data,
      estado: r.estado, motivo: r.motivo ?? null, observado: r.observado ?? null,
    })) + '\n');
    if (!aquecimento) contagem[r.estado] = (contagem[r.estado] ?? 0) + 1;
    console.log(ocultar(`${id}: ${r.estado}${r.estado === 'sucesso' ? ` ${(r.tFim! - r.t0!).toFixed(1)} ms` : ` (${r.motivo})`}`));
  }
  console.log(`${c.cenario}: ${JSON.stringify(contagem)} -> ${path.relative(process.cwd(), arqCsv)}`);
  return { dir, arqCsv, contagem };
}

// ---------- utilidades comuns aos roteiros ----------

export async function anoPeriodoCorrente(request: APIRequestContext): Promise<{ ano: string; periodo: string; texto: string }> {
  const r = await request.get(`${API}/courses/year-period/`);
  const texto: string = (await r.json())['year/period'][0];
  const [ano, periodo] = texto.split('/');
  return { ano, periodo, texto };
}

export interface TurmaRef { codigo: string; turma: string }
export interface TurmaResolvida extends TurmaRef { nome: string; indice: number; schedule: string; id: number }

// Resolve a turma por código da disciplina e número da turma (nunca por id fixo):
// o índice é a posição na lista de turmas devolvida pela API, que é a ordem exibida
// pelo frontend (DisciplineFragment.tsx, discipline.classes.map).
export async function resolverTurma(request: APIRequestContext, t: TurmaRef): Promise<TurmaResolvida> {
  const { ano, periodo } = await anoPeriodoCorrente(request);
  const r = await request.get(`${API}/courses/`, { params: { search: t.codigo, year: ano, period: periodo } });
  const disc = (await r.json()).find((d: any) => d.code === t.codigo);
  if (!disc) throw new Error(`disciplina ${t.codigo} não encontrada na massa`);
  const indice = disc.classes.findIndex((c: any) => c._class === t.turma);
  if (indice < 0) throw new Error(`turma ${t.codigo}/${t.turma} não encontrada na massa`);
  return { ...t, nome: disc.name, indice, schedule: disc.classes[indice].schedule, id: disc.classes[indice].id };
}

// Abre o painel "Buscar matéria" e escolhe o ano/período corrente.
export async function abrirBusca(page: Page, anoPeriodo: string) {
  await page.getByRole('button', { name: 'Buscar matéria' }).click();
  const sel = page.locator('section select').first();
  await sel.waitFor();
  await page.waitForFunction((v) => [...document.querySelectorAll('section select option')]
    .some(o => (o as HTMLOptionElement).value === v), anoPeriodo);
  await sel.selectOption(anoPeriodo);
}

export function botaoPesquisa(page: Page): Locator {
  return page.getByRole('button', { name: 'ícone de pesquisa' });
}

export function botaoDisciplina(page: Page, codigo: string): Locator {
  return page.locator('section button:has(img[alt="expand icon"])', { hasText: ` - ${codigo}` });
}

// Linha (ClassInfoBox) da turma, na ordem exibida sob a disciplina expandida.
export function linhaTurma(page: Page, t: TurmaResolvida): Locator {
  return botaoDisciplina(page, t.codigo).locator('xpath=following-sibling::div[1]')
    .locator(':scope > div').nth(t.indice);
}

// Busca o código, expande a disciplina e confere que a linha exibida é a turma esperada.
export async function expandirTurma(page: Page, t: TurmaResolvida): Promise<Locator> {
  await page.getByPlaceholder('Matéria ou Professor...').fill(t.codigo);
  // espera a resposta desta busca: a lista antiga pode ter a mesma disciplina
  const resp = page.waitForResponse(r => r.url().includes('/courses/?') && r.url().includes(`search=${t.codigo}`));
  await botaoPesquisa(page).click();
  await resp;
  await botaoDisciplina(page, t.codigo).click();
  const linha = linhaTurma(page, t);
  await linha.waitFor();
  const texto = await linha.innerText();
  if (!texto.includes(t.schedule)) throw new Error(`linha ${t.indice} não mostra o horário ${t.schedule} de ${t.codigo}/${t.turma}`);
  return linha;
}

export async function selecionarTurma(page: Page, t: TurmaResolvida) {
  const linha = await expandirTurma(page, t);
  await linha.getByRole('button').click();
  await linha.getByRole('img', { name: 'ícone remover matéria' }).waitFor();
}
