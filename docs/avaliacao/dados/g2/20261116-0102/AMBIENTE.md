# Rodada 20261116-0102: ambiente da recoleta de M3

Nova rodada identificada de M3 (`m3-sem-selecao` e `m3-com-selecao`), feita depois da
correção do roteiro de `m3-com-selecao` (commit `f487e78`). A rodada `20261115-2128`
continua preservada (Fase 2, seção 4.3, regra 1). Os dois cenários de M3 foram coletados de
novo, juntos, para que a nota de M3 não misture ambientes (regra 4).

Antes da coleta, um piloto com 10 medidas de `m3-com-selecao` (fora da amostra) teve 10
sucessos.

**Atenção:** a coluna `ambiente` dos CSVs diz "local Docker Compose", porque esse texto é
fixo no roteiro (`medicao.ts`). Esta rodada **não** usou Docker Compose. O ambiente real foi:

| Item | Valor |
|------|-------|
| Máquina | VM Linux na nuvem, 2 vCPUs, 7,8 GiB de memória, sem swap (`uname`: Linux 6.18.44 x86_64) |
| Produto | `unb-mds/2023-2-SuaGradeUnB`, commit `3d399e7`, sem alterações rastreadas |
| API | Django 5.1.5 em Python 3.11.18 (venv com `api/requirements.txt` e `setuptools<70`), `manage.py runserver 0.0.0.0:8000`, `core.settings.dev` |
| Banco e cache | PostgreSQL 16.15 e Redis 7.0.15 instalados na máquina, sem contêiner |
| Frontend | Next.js 14.2.21 com `npm run dev`, Node 22.23.4 |
| Massa | `avaliacao/massa/seed_referencia.py`: 2026/2, departamento 1499, 14 disciplinas, 43 turmas |
| Navegador | Chromium 153.0.8010.12 *headless* (Chrome for Testing já instalado na máquina), Playwright 1.62.1, viewport 1280×720, `workers: 1`, `retries: 0` |

Motivo do desvio: a máquina não tinha acesso ao Docker Hub nem ao download do Chromium 151
do Playwright. Por isso o campo `docker_ps` do `metadados.json` registra falha.

Os tempos desta rodada não são comparáveis em valor absoluto com os de M2, M4 e M5 da rodada
`20261115-2128`, feitos em outra máquina. A comparação com o limite de cada cenário vale
dentro de cada rodada.
