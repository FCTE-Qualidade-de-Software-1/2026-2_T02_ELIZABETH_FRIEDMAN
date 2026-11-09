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
| M1.1–M1.4 | Preparação em issue própria (#38) | A definir nessa entrega | Pendente |
| M2–M5 | Preparação em issue própria (#39) | A definir nessa entrega | Pendente |
| M6 — Primeiro uso | Teste observado com estudantes sem uso prévio; mede conclusão independente do fluxo | Navegador, cronômetro, massa fixa, CSV e evidência de recuperação | [Protocolo, §3](avaliacao-interacao/protocolo.md#3-m6-primeiro-uso) |
| M7 — Controle da grade | Tarefas observadas de seleção, remoção e alteração; conferência do estado final | Computador/celular reais, estados restauráveis, CSV e capturas | [Protocolo, §4](avaliacao-interacao/protocolo.md#4-m7-controle-da-grade) |
| M8 — Proteção contra perda | Inspeção por cenários de risco, executada pelo avaliador | Grades descartáveis, inventário, CSV e capturas antes/depois | [Instrumentos M8/M9](avaliacao-interacao/instrumentos.md) |
| M9 — Compreensão | Perguntas neutras sobre estado e próxima ação, classificadas por gabarito | Estados reais, captura no instante da pergunta e CSV | [Instrumentos M8/M9](avaliacao-interacao/instrumentos.md) |

O protocolo observado permite conferir comportamento e respostas de estudantes; a
inspeção de M8 permite provocar perdas com dados descartáveis sem expor participantes.
Automação pode preparar estados e capturas, mas não substitui respostas humanas.
As fórmulas e os critérios de julgamento continuam sendo os da [Fase 2, §3.3](fase-2.md#33-metricas-de-capacidade-de-interacao-g3).
Este documento cobre F3-C8 para M6–M9; as demais métricas dependem de suas próprias entregas.

## 2. Recursos e ambiente de avaliação

<!--
F3-C2: hardware e software necessários, massa de dados (dados-exemplo) quando pertinente,
perfil exigido dos avaliadores/usuários (conhecimento em informática e no domínio).
-->

Esta seção descreve o ambiente local usado nas métricas que dependem da reprodução do
produto (M1.3, M1.4 e M2–M5, ver [Fase 2](fase-2.md)) e, na [seção 2.5](#25-participantes-e-sessoes-m6-a-m9),
o uso desse ambiente nas sessões com participantes de M6 a M9. Cada versão traz a fonte de onde
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

### 2.5 Participantes e sessões (M6 a M9)

Para M6–M9, usar a versão `3d399e745383b05e8e3b1a7c97ac0fdbf93a0360`
do Sua Grade UnB (seção 2.1) em ambiente local isolado, com a massa de referência da seção 2.3,
conta de teste quando necessária e acesso por computador e celular físicos. Registrar sistema operacional,
navegador/versão, dimensões e URL efetiva no manifesto da sessão. As sessões serão online por Google Meet. Validar acesso remoto privado ao ambiente
nos dispositivos dos participantes antes do piloto; `localhost` no celular aponta
para o próprio celular. O compartilhamento de tela também deve ser validado.

O avaliador deve saber restaurar o estado, conferir disciplinas/turmas e preservar
registros sem orientar o caminho. Participantes: estudantes adultos sem uso prévio,
com conhecimento básico de navegador e do conceito de disciplina/turma. Planejam-se
dois estudantes no computador e dois no celular, com um suplente por grupo;
uma pessoa adicional participa apenas do piloto. A redução de dez para quatro
participantes foi definida antes da coleta em 08/11/2026 para viabilizar a execução
pela dupla, com menor cobertura e sem alterar os limiares de julgamento da Fase 2.
Trata-se de amostra exploratória
por conveniência, sem pretensão de representatividade estatística.

Recursos, instruções, tempos e pendências estão no [protocolo](avaliacao-interacao/protocolo.md).
O [consentimento](avaliacao-interacao/consentimento.md), o [recrutamento](avaliacao-interacao/recrutamento.md)
e os [modelos CSV](avaliacao-interacao/registros.md) fazem parte do instrumento.
O [procedimento de proteção dos dados](avaliacao-interacao/dados.md) orienta a equipe
sobre o preenchimento do termo e o tratamento das autorizações e registros.
O ambiente e a massa de referência são os da #37 (seções 2.1 e 2.3). Ainda precisam ser
confirmados os identificadores reais das disciplinas e turmas usadas nas tarefas e o acesso
às modalidades de salvamento. Preparação documental não constitui coleta validada.

## 3. Cronograma da avaliação

<!--
F3-C3: cronograma realista com atividades distribuídas e alinhadas à execução da Fase 4.
-->


| Atividade | Responsável | Início | Fim | Métricas envolvidas |
|-----------|-------------|--------|-----|---------------------|
| Preparar roteiro, consentimento, CSV e instrumentos | Lucas e Kaleb | 03/11/2026 | 08/11/2026 | M6–M9 |
| Preencher campos do termo, validar acesso ao ambiente nos dois dispositivos, preparar cartões com disciplinas reais, recrutar PIL01 e participantes | Lucas e Kaleb | 09/11/2026 | 10/11/2026 | M6–M9 |
| Executar piloto com PIL01 e verificar recursos nos dois dispositivos | Lucas e Kaleb | 11/11/2026 | 11/11/2026 | M6–M9 |
| Corrigir instrumentos, repetir trechos afetados e congelar protocolo | Lucas e Kaleb | 12/11/2026 | 12/11/2026 | M6–M9 |
| Inspeção M8 no ambiente, com dados descartáveis | Lucas e Kaleb | 12/11/2026 | 13/11/2026 | M8 |
| Coleta formal: sessões com os quatro participantes (suplentes se necessário) | Lucas e Kaleb | 13/11/2026 | 14/11/2026 | M6, M7, M9 |
| Análise e escrita dos resultados na Fase 4 | Equipe | 14/11/2026 | 16/11/2026 | M6–M9 |

### Situação da issue #40

Materiais preparados em 03/11/2026 e revisados em 08/11/2026, protocolo 0.2, **aguardando validação humana**.
O [registro de piloto e fechamento](avaliacao-interacao/piloto.md) mantém os critérios
de liberação e as pendências. Não encerrar a issue antes de confirmar recrutamento,
inventário no ambiente real e piloto com pessoa fora da amostra.

---

Anterior: [Fase 2](fase-2.md) · Próxima: [Fase 4 — Execução e resultados](fase-4.md).