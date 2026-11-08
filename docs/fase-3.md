# Fase 3 — Projetar a avaliação

<!--
Referência: ISO/IEC 25040, atividade 3.
F3-C8: para cada métrica da Fase 2, indicar explicitamente o método e os recursos que a medem.
-->

## 1. Método de avaliação

<!--
F3-C1: método justificado e instruções passo a passo para o avaliador,
garantindo repetibilidade e reprodutibilidade.
-->

| Métrica ([Fase 2](fase-2.md#3-metricas-nivel-quantitativo)) | Método / técnica | Ferramenta | Instruções |
|---------------------------------------------------------------|------------------|------------|------------|
| M1 | | | |

## 2. Recursos e ambiente de avaliação

<!--
F3-C2: hardware e software necessários, massa de dados (dados-exemplo) quando pertinente,
perfil exigido dos avaliadores/usuários (conhecimento em informática e no domínio).
-->

Esta seção descreve o ambiente local usado nas métricas que dependem da reprodução do
produto (M1.3, M1.4 e M2–M5, ver [Fase 2](fase-2.md)). Cada versão traz a fonte de onde
foi lida: um arquivo do repositório do produto ou a saída de um comando executado na
máquina de avaliação em 03/11/2026. O que ainda não foi confirmado está marcado como
**a confirmar**.

### 2.1 Versão avaliada e subida do ambiente

**Produto:** [unb-mds/2023-2-SuaGradeUnB](https://github.com/unb-mds/2023-2-SuaGradeUnB),
branch `main`.

| Campo | Valor | Fonte |
|-------|-------|-------|
| *Commit* (curto) | `3d399e7` | `git log -1 --format=%h 3d399e7` |
| *Commit* (completo) | `3d399e745383b05e8e3b1a7c97ac0fdbf93a0360` | `git log -1 --format=%H 3d399e7` |
| Data | 15/02/2026 10:44:50 -0300 | `git log -1 --format=%ci 3d399e7` |
| Autor | Caio Felipe | `git log -1 --format=%an 3d399e7` |
| Mensagem | `Merge pull request #250 from Marcosatc147/main` | `git log -1 --format=%s 3d399e7` |

**Fixar a versão:**

```bash
git clone https://github.com/unb-mds/2023-2-SuaGradeUnB.git
cd 2023-2-SuaGradeUnB
git checkout 3d399e745383b05e8e3b1a7c97ac0fdbf93a0360
git log -1 --format='%H %ci'   # deve mostrar 3d399e7… 2026-02-15 10:44:50 -0300
```

**Serviços** (fonte: `docker-compose.yml`, `docker/Dockerfile`, `docker/Dockerfile.web`):

| Serviço (`compose`) | Contêiner | Imagem / base | Porta no host | Papel |
|---------------------|-----------|---------------|---------------|-------|
| `db` | `postgresql` | `postgres:16` | não publicada | PostgreSQL; volume `postgres_data` |
| `redis` | `rediscache` | `redis:alpine` | não publicada | *Cache* e sessões |
| `api` | `django-api` | `python:3.11.6-alpine3.18` (build) | `8000` | API Django (`runserver 0.0.0.0:8000`) |
| `web` | `nextjs-web` | `node:20.9.0-alpine3.18` (build) | `3000` | *Frontend* Next.js (`npm run dev`) |

As tags `postgres:16` e `redis:alpine` não são fixas e podem mudar entre as execuções. Por
isso, o digest de cada imagem deve ser registrado depois do primeiro `pull`:
`docker image inspect --format '{{index .RepoDigests 0}}' postgres:16 redis:alpine`.
Versões registradas na máquina de avaliação em 03/11/2026:

| Componente | Versão em execução | Fonte |
|------------|--------------------|-------|
| PostgreSQL | 16.11, `postgres@sha256:d4c3314b2dd74ff23cd6cd07e4d7e737cb6ef791c22a7cbd744cfbfb4815df72` | `docker exec postgresql postgres --version`; `docker image inspect` |
| Redis | 8.10.3, `redis@sha256:21090af93f8324db2f0f0f4f38a7c60369d47d917e000c3423d89d2ae2883537` | `docker exec rediscache redis-server --version`; `docker image inspect` |
| Python (API) | 3.11.6; Django 5.1.5 | `docker exec django-api python3 --version`; log do `runserver` |
| Node / npm (*frontend*) | v20.9.0 / 10.1.0; Next.js 14.2.21 | `docker exec nextjs-web node --version`, `npm --version`, `node -p "require('next/package.json').version"` |

**Variáveis de ambiente.** O alvo `make config` (fonte: `Makefile`) copia
`api/.env.example` → `api/.env` e `web/.env.example` → `web/.env.local`. Em seguida, gera
valores aleatórios para `DJANGO_SECRET_KEY` (`scripts/env.sh`) e `GOOGLE_OAUTH2_MOCK_TOKEN`
(`scripts/config.sh`). Os outros valores ficam como no exemplo:

| Arquivo | Variável | Valor do `.env.example` | Uso |
|---------|----------|-------------------------|-----|
| `api/.env` | `DJANGO_SECRET_KEY` | `your_secret_key` → aleatório | Chave do Django |
| `api/.env` | `SETTINGS_FILE_PATH` | `core.settings.dev` | `DEBUG=True`, CORS liberado |
| `api/.env` | `DB_ENGINE`, `DB_NAME`, `DB_USERNAME`, `DB_PASSWORD`, `DB_HOSTNAME`, `DB_PORT` | `django.db.backends.postgresql`, `postgres`, `suagradeunb`, `suagradeunb`, `db`, `5432` | Conexão da API |
| `api/.env` | `POSTGRES_DB`, `POSTGRES_USER`, `POSTGRES_PASSWORD` | `postgres`, `suagradeunb`, `suagradeunb` | Inicialização do contêiner `db` |
| `api/.env` | `REDIS_CACHE_LOCATION` | `redis://redis:6379/1` | *Cache* |
| `api/.env` | `ADMIN_NAME`, `ADMIN_PASS`, `ADMIN_EMAIL` | `admin`, `admin`, `admin@gmail.com` | Superusuário criado por `initadmin` |
| `api/.env` | `GOOGLE_OAUTH2_MOCK_TOKEN` | `your_google_oauth2_mock_token` → aleatório | Login simulado na API (ver 2.3) |
| `web/.env.local` | `NEXT_PUBLIC_API_URL` | `http://localhost:8000` | Endereço da API usado pelo navegador |
| `web/.env.local` | `NEXT_PUBLIC_GOOGLE_OAUTH_URL` | `https://accounts.google.com/o/oauth2/v2/auth` | Login Google |
| `web/.env.local` | `NEXT_PUBLIC_GOOGLE_OAUTH_CLIENT_ID` | `your_client_id` | Mantido sem valor real; o login Google fica fora do escopo ([Fase 1, Tabela 12](fase-1.md#62-o-que-fica-fora-do-escopo)) |

**Passo a passo:**

```bash
# 1. Configurar o ambiente (cria api/.env e web/.env.local)
make config

# 2. Construir e subir os quatro serviços em segundo plano
docker compose up --build -d

# 3. Acompanhar a inicialização da API
docker compose logs -f api
```

**Ordem de inicialização.** O `depends_on` do compose sobe `db` e `redis` antes de `api`, e
`api` antes de `web`. O `api/config/entrypoint.sh` espera a porta do PostgreSQL responder
(`nc -z $DB_HOSTNAME $DB_PORT`). Depois executa `python3 manage.py migrate` e
`python3 manage.py initadmin`, e só então inicia o servidor. A API está pronta quando o log
mostra `PostgreSQL iniciado`, `Migrando banco de dados...` e a linha de escuta do
`runserver`.

**Verificação de cada serviço:**

| Serviço | Comando | Resultado esperado |
|---------|---------|--------------------|
| Todos | `docker compose ps` | Quatro contêineres com estado `running` |
| PostgreSQL | `docker exec postgresql pg_isready -U suagradeunb` | `accepting connections` |
| Redis | `docker exec rediscache redis-cli ping` | `PONG` |
| API | `curl -s http://localhost:8000/courses/year-period/` | JSON `{"year/period": [...]}` com o período atual e o seguinte (rota em `api/api/urls.py`) |
| *Frontend* | `curl -s -o /dev/null -w '%{http_code}\n' http://localhost:3000` | `200` |

Para encerrar sem apagar dados, use `docker compose stop` ou `docker compose down`. **Não**
use `docker compose down -v` (alvo `make stop-v`), porque esse comando apaga o volume do
banco.

**Execução nesta máquina (03/11/2026):** depois de `make config`, o
`docker compose up --build -d` construiu as imagens `2023-2-suagradeunb-api` e
`2023-2-suagradeunb-web`, criou o volume `2023-2-suagradeunb_postgres_data` e iniciou os
quatro contêineres em cerca de 3 min (`time`). Antes da subida, as portas `3000` e `8000` do
host estavam livres (`ss -ltn`). As portas `5432` e `6379` estão em uso por outros serviços
da máquina, mas isso não causa conflito porque o compose não publica essas portas.
Resultados das verificações:

| Verificação | Saída obtida |
|-------------|--------------|
| `docker compose ps` | `api`, `web`, `db` e `redis` em `running`; `0.0.0.0:8000->8000/tcp` e `0.0.0.0:3000->3000/tcp` |
| `docker compose logs api` | `PostgreSQL iniciado`, todas as migrações `OK`, `Conta do usuário admin será criada!`, `System check identified no issues (0 silenced).`, `Starting development server at http://0.0.0.0:8000/` |
| `pg_isready` | `/var/run/postgresql:5432 - accepting connections` |
| `redis-cli ping` | `PONG` |
| `/courses/year-period/` | `{"year/period":["2026/2","2027/1"]}` |
| `http://localhost:3000` | `200` |

Uma reprodução anterior, de 17/10/2026, está na
[Fase 1, Seção 3.6](fase-1.md#36-reproducao-local-e-implicacoes-para-a-avaliacao).

### 2.2 Requisitos do avaliador

O projeto declara os pré-requisitos em `docs/executing.md`. Os dados da máquina de
avaliação foram coletados em 03/11/2026.

| Item | Mínimo exigido pelo projeto (fonte) | Máquina usada na avaliação (comando) |
|------|-------------------------------------|--------------------------------------|
| Sistema operacional | Não declarado | Ubuntu 24.04.2 LTS (`lsb_release -a`); *kernel* Linux 7.0.0-38-generic x86_64 (`uname -a`) |
| Equipamento | Não declarado | Modelo `550XDA` (`/sys/devices/virtual/dmi/id/product_name`) |
| CPU | Não declarado | Intel Core i5-1135G7 @ 2.40 GHz, 4 núcleos / 8 *threads* (`lscpu`) |
| Memória | Não declarado | 7,5 GiB de RAM + 4,0 GiB de *swap* (`free -h`) |
| Disco | Não declarado | 233 GB, 73 GB livres (`df -h ~`) |
| Docker Engine | v24.0.6 ou superior (`docs/executing.md`) | 29.1.2 (`docker --version`) |
| Docker Compose | v2.21.0 ou superior (`docs/executing.md`) | v2.40.3 (`docker compose version`) |
| GNU Make | 4.3 ou superior (`docs/executing.md`) | 4.3 (`make --version`) |
| Python (host) | 3.11.6 (`docs/executing.md`, `api/runtime.txt`) | 3.12.3 (`python3 --version`); a API roda no contêiner `python:3.11.6-alpine3.18` |
| Node / npm (host) | Node 20.9.0 / npm 10.1.0 (`docs/executing.md`) | Node v22.22.3 / npm 11.16.0 (`node --version`, `npm --version`); o *frontend* roda no contêiner `node:20.9.0-alpine3.18` |
| Git | Não declarado | 2.43.0 (`git --version`) |
| Navegador (automação) | Não declarado | Chromium do Playwright, ver 2.4 |
| Navegador (manual) | Não declarado | Google Chrome 153.0.8010.36 (`google-chrome --version`) |

**Observações sobre a máquina:**

- Python e Node do host diferem do mínimo declarado, mas isso não afeta a execução: API e
  *frontend* rodam nos contêineres com as versões fixadas nos Dockerfiles. As versões do host
  só importam para `make config` (usa `python3`) e para o Playwright (usa Node).
- No momento da coleta havia outros contêineres em execução na máquina (de outros
  projetos), e a memória disponível era de 795 MiB (`free -h`). Para as métricas de
  eficiência de desempenho, esses contêineres devem ser parados antes da medição, e o
  `docker ps` e o `free -h` devem ser registrados junto com cada coleta.

**Perfil do avaliador:** saber usar terminal Linux, Git e Docker Compose, e conhecer o
básico de Playwright/TypeScript para rodar e ler os roteiros. Para as tarefas não é preciso
conhecer o domínio (matrícula na UnB) além do descrito na [Fase 1](fase-1.md).

### 2.3 Massa de referência

**O que o repositório oferece:**

- Não há *fixtures* nem *seed* de disciplinas e turmas. O comando
  `python3 manage.py updatedb` (`api/api/management/commands/updatedb.py`; alvos
  `make updatedb-all` e `make deletedb-all`) baixa os dados do SIGAA em produção. Com isso o
  resultado muda a cada execução e depende de um serviço externo, o que não serve como massa
  fixa.
- O próprio projeto guarda uma página do SIGAA usada nos testes, em
  `api/utils/mock/sigaa.html` (departamento `1499`, 2023/2, conforme
  `api/utils/mock/infos.json`), com SHA-256
  `17ae00b1edcc0348c3dff66ef7709be26f8f3f2f5efc244ee65d54a198dead65` (`sha256sum`).
  O *parser* do próprio produto (`DisciplineWebScraper.make_web_scraping_of_disciplines`)
  extrai desse arquivo, sem acesso à rede, **14 disciplinas e 43 turmas** do Programa de
  Pós-Graduação em Política Social (códigos `PPGPS*`).
- `initadmin` cria o superusuário `admin` / `admin` (valores do `.env.example`).
- Usuário de teste: um `POST /users/register/google/` com
  `{"access_token": "<GOOGLE_OAUTH2_MOCK_TOKEN>"}` cria ou autentica o usuário
  `user@email.com` sem chamar o Google (`api/users/backends/google.py`). O *frontend* não
  usa esse caminho. Por isso, para o salvamento na conta (M5), a sessão precisaria ser
  injetada pelo roteiro, o que fica **a confirmar** no piloto.

**Massa adotada:** as 14 disciplinas e 43 turmas do mock acima, carregadas no
departamento `1499`, no **ano e período correntes** devolvidos por
`/courses/year-period/`. O *frontend* só oferece o período atual e o seguinte
(`api/utils/sessions.py`). O conteúdo da massa não muda, mas o ano/período em que ela é
gravada acompanha a data da execução, e esse valor deve ser registrado em cada coleta.

**Carga e restauração:** o *script*
[`avaliacao/massa/seed_referencia.py`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_ELIZABETH_FRIEDMAN/blob/main/avaliacao/massa/seed_referencia.py)
confere o SHA-256 do mock e o lê com o *parser* do produto, sem acessar a rede. Em seguida,
apaga e recria o departamento `1499` do período corrente em uma transação. Assim, rodar o
*script* de novo restaura o estado inicial das disciplinas e turmas. Ele deve ser executado
a partir do diretório do produto, com os serviços de pé:

```bash
docker exec -i django-api python3 manage.py shell \
  < ../2026-2_T02_ELIZABETH_FRIEDMAN/avaliacao/massa/seed_referencia.py
# massa carregada: 2026/2 depto 1499 14 disciplinas, 43 turmas, mock 17ae00b1edcc
```

O *script* foi executado duas vezes seguidas em 03/11/2026. Depois disso, o banco tinha
1 departamento, 14 disciplinas e 43 turmas, o que confirma que repetir a carga não duplica
os dados. Grades salvas no navegador são descartadas porque cada execução do Playwright usa
um contexto novo.

**Resultados de referência** (API local, ano 2026, período 2, 03/11/2026):

| Operação | Entrada | Resultado esperado |
|----------|---------|--------------------|
| Busca por nome | `GET /courses/?search=seminario&year=2026&period=2` | 3 disciplinas: `PPGPS0156` (4 turmas), `PPGPS0157` (1), `PPGPS2989` (16) |
| Busca por nome | `search=politica` | 6 disciplinas: `PPGPS0032`, `PPGPS0156`, `PPGPS0157`, `PPGPS2475`, `PPGPS2991`, `PPGPS0030` |
| Busca por código | `search=PPGPS2475` | 1 disciplina (`ESTADO E POLÍTICA SOCIAL NO BRASIL`, 1 turma) |
| Geração | `POST /courses/schedules/generate/` com as turmas `PPGPS2475/01` (5T2345) e `PPGPS2939/01` (4M1234) | `Horários gerados com sucesso.`, 1 grade com as duas turmas |

Os `id` das turmas mudam a cada carga, porque são gerados pelo banco. Por isso, os roteiros
devem identificar a turma por código da disciplina e número da turma, nunca pelo `id`.

### 2.4 Playwright e Chromium

O produto não usa Playwright (`web/package.json` não tem a dependência e o *frontend* não
tem testes). A automação fica no projeto `avaliacao/e2e/` deste repositório, com execução
sequencial (`workers: 1`) e sem novas tentativas (`retries: 0`), definidas em
`playwright.config.ts`.

| Item | Versão | Fonte |
|------|--------|-------|
| `@playwright/test` | `1.62.1` (exata, sem `^`) | `avaliacao/e2e/package.json` e `package-lock.json` (`@playwright/test`, `playwright` e `playwright-core` em `1.62.1`); `npx playwright --version` → `Version 1.62.1` |
| Chromium | Chrome for Testing `151.0.7922.34` (revisão `1234`) | `npx playwright install --dry-run chromium`; `~/.cache/ms-playwright/chromium-1234/chrome-linux64/chrome --version` |
| Chromium *headless shell* | `151.0.7922.34` (revisão `1234`) | `npx playwright install --dry-run chromium` |

É a mesma versão usada no teste de inicialização da [Fase 2](fase-2.md).

**Instalação fixada:**

```bash
cd avaliacao/e2e
npm ci                             # instala exatamente o package-lock.json
npx playwright --version           # esperado: Version 1.62.1
npx playwright install chromium    # baixa a revisão 1234 se ainda não estiver no cache
```

Na máquina de avaliação, as revisões `chromium-1234` e `chromium_headless_shell-1234` já
estavam no cache (`--dry-run`), então nada foi baixado.

**Demonstração de inicialização (03/11/2026)**, com os serviços da 2.1 de pé:

```text
$ npx playwright test --list
  [chromium] › smoke.spec.ts:6:5 › API responde o período letivo
  [chromium] › smoke.spec.ts:12:5 › frontend abre a tela inicial
Total: 2 tests in 1 file

$ npx playwright test
Running 2 tests using 1 worker
  ✓  1 [chromium] › tests/smoke.spec.ts:6:5 › API responde o período letivo (89ms)
  ✓  2 [chromium] › tests/smoke.spec.ts:12:5 › frontend abre a tela inicial (4.1s)
  2 passed (5.4s)
```

O *smoke* só confirma que o Chromium inicia, que a API responde e que a tela inicial
(`Continuar como anônimo`) é exibida. Não é coleta de M2–M5.

## 3. Cronograma da avaliação

<!--
F3-C3: cronograma realista com atividades distribuídas e alinhadas à execução da Fase 4.
-->

Cada linha corresponde a uma issue do repositório. A coluna **Fim** é a meta registrada na issue;
**Início** é a previsão da equipe. Todas as atividades terminam até **22/11/2026**.

| Issue | Atividade | Responsável | Início | Fim | Métricas | Depende de |
|------|-----------|-------------|--------|-----|----------|------------|
| #37 | Ambiente de avaliação e massa de referência (concluído) | Júlia | 03/11 | 03/11 | M1.3, M1.4, M2–M5 | n/a |
| #38 | Método e roteiros de Manutenibilidade, com piloto | Lucas | 04/11 | 07/11 | M1.1–M1.4 | #37 |
| #39 | Método e roteiros de Eficiência de desempenho, com piloto | Júlia | 04/11 | 07/11 | M2–M5 | #37 |
| #40 | Protocolo com participantes de Capacidade de interação, com piloto | Lucas, kaleb | 04/11 | 07/11 | M6–M9 | n/a |
| #41 | Cronograma e consistência com a Fase 2 (esta página) | Joaquim | 03/11 | 03/11 | M1.1–M9 | n/a |
| #36 | Material do PC2 (apresentação em 16/11 ou 18/11) | Todos | 08/11 | 15/11 | n/a | #38–#41 |
| #42 | Fase 4: coleta e análise de Manutenibilidade (G1) | kaleb | 08/11 | 17/11 | M1.1–M1.4 | #38 |
| #43 | Fase 4: coleta e análise de Eficiência de desempenho (G2) | Júlia | 08/11 | 17/11 | M2–M5 | #39 |
| #44 | Fase 4: sessões e análise de Capacidade de interação (G3) | Lucas, João | 08/11 | 17/11 | M6–M9 | #40 |
| #45 | Fase 4: julgamento, relações entre características e recomendações | kaleb, Joaquim | 17/11 | 19/11 | M1.1–M9 | #42–#44 |
| #46 | Fase 4: ação de melhoria | Lucas | 19/11 | 20/11 | n/a | #45 |
| #47 | Artigo: metodologia, resultados e conclusão | João | 17/11 | 20/11 | n/a | #41–#46 |
| #48 | Artigo: revisão final da 2ª versão | João | 20/11 | 21/11 | n/a | #47 |
| #50 | Gestão PSM/CID, atas e decisões da E2 | Joaquim | 03/11 | 21/11 | n/a | contínuo |
| #51 | Fechamento da E2: GitPage, contribuição e *release* v2.0 | Eduardo | 21/11 | 22/11 | n/a | #48, #50 |

---

## 4. Consistência com a Fase 2

<!--
F3-C8: para cada métrica da Fase 2, indicar explicitamente o método e os recursos que a medem.
Esta seção registra o que a Fase 3 fixou, o que mudou em relação à Fase 2 e o que ainda está pendente.
-->

A Fase 3 não altera nenhuma métrica, fórmula nem faixa de pontuação da [Fase 2](fase-2.md).
A tabela da seção 1 cobre M1.1 a M1.4 e M2 a M9, com a mesma numeração.

### 4.1 O que mudou em relação à Fase 2 e por quê

| # | Tema | Na Fase 2 | Na Fase 3 | Por quê e efeito |
|---|------|-----------|-----------|------------------|
| 1 | Máquina e Docker | Docker indisponível na distribuição WSL inspecionada em 18/10 ([3.2](fase-2.md#32-verificacao-de-viabilidade-da-coleta)); Node 24.19.0, npm 11.17.0 | Ubuntu 24.04.2 LTS, Docker 29.1.2, Compose v2.40.3; quatro serviços de pé em 03/11 ([2.1](#21-versao-avaliada-e-subida-do-ambiente), [2.2](#22-requisitos-do-avaliador)); Node v22.22.3, npm 11.16.0 | A coleta passou para outra máquina. A pendência 1 da Fase 2 está atendida. As ferramentas de análise estática de M1.1 e M1.2 devem registrar de novo as versões do host, pois as execuções de 18/10 foram só verificação inicial |
| 2 | Massa de M2–M5 | Conjuntos fixos a definir na Fase 3, sem acionar o SIGAA | Mock do projeto (`api/utils/mock/sigaa.html`): departamento 1499, 14 disciplinas e 43 turmas, todas de Pós-Graduação em Política Social ([2.3](#23-massa-de-referencia)) | É o único conjunto fixo e reproduzível sem rede. Os resultados valem para essa massa, não para o volume de uma matrícula real; a Fase 2 já limita as conclusões nesse sentido |
| 3 | Sessão na conta (M5) | Conta de teste com autenticação funcional por OAuth local | O login Google fica fora do escopo ([Fase 1, Tabela 12](fase-1.md#62-o-que-fica-fora-do-escopo)); a API aceita um *token* simulado, mas o *frontend* não usa esse caminho, então o roteiro injeta a sessão (**a confirmar** no piloto) | Evita depender de credenciais reais. Se a sessão não puder ser reproduzida, vale a regra da Fase 2: registrar a limitação e não atribuir resultado à modalidade conta |
| 4 | Período da massa | Não especificado | A massa é gravada no ano e período correntes (`/courses/year-period/`), e o valor é registrado em cada coleta ([2.3](#23-massa-de-referencia)) | O *frontend* só oferece o período atual e o seguinte |

### 4.2 Decisões que a Fase 2 deixou para a Fase 3

| Decisão pendente na Fase 2 | Situação | Issue |
|----------------------------|----------|------|
| Fixar versões de Playwright e Chromium; execução sequencial sem nova tentativa | Fixadas: 1.62.1 e 151.0.7922.34; `workers: 1`, `retries: 0` ([2.4](#24-playwright-e-chromium)) | #37, concluído |
| Reprodução local e massa de referência | Feitas em 03/11 ([2.1](#21-versao-avaliada-e-subida-do-ambiente), [2.3](#23-massa-de-referencia)) | #37, concluído |
| Tempo máximo de espera por operação (maior que $L_j$) | Pendente | #39 |
| Seletores e sinais de conclusão visual de M2–M5 | Pendente | #39 |
| Configuração própria do `coverage` (`source` explícito, sem `pragma: no cover`) | Pendente; conferir no piloto | #38 |
| Executor de C1 e C2 e fichas das mudanças | Pendente | #38 |
| Número e perfil dos participantes, limites $E$ e $T$ de M6, consentimento | Pendente | #40 |
| Inventário de riscos de M8 e gabarito de M9 | Pendente | #40 |
| Pilotos de todas as métricas | Pendente | #38, #39, #40 |

---

Anterior: [Fase 2](fase-2.md) · Próxima: [Fase 4 — Execução e resultados](fase-4.md).
