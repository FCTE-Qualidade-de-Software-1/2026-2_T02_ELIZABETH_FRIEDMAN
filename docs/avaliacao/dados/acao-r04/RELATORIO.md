# Verificação da ação M8–R04 (#46)

Data local: 16/11/2026 (America/Sao_Paulo). Os horários dos JSONs estão em UTC,
em 17/11/2026. Esta coleta é separada da avaliação original de G3.

## Problema e artefato

A [#45](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_ELIZABETH_FRIEDMAN/issues/45)
priorizou impedir a perda de turmas ao recarregar durante a montagem. O cenário
M8–R04 falhou nos dois dispositivos na coleta pública original
([observações preservadas](../g3/m8-observacoes.csv)). Esta ação implementa a
recuperação temporária e verifica seu comportamento sem recrutar participantes.

- Origem: `3d399e745383b05e8e3b1a7c97ac0fdbf93a0360`.
- Correção: [`54c781189868b7138fbeb8659622fd3540cafdcb`](https://github.com/LucasMF1/2023-2-SuaGradeUnB/commit/54c781189868b7138fbeb8659622fd3540cafdcb).
- [Fork e branch](https://github.com/LucasMF1/2023-2-SuaGradeUnB/tree/fix/r04-selection-draft).
- [PR nº 252 no repositório original do Sua Grade UnB](https://github.com/unb-mds/2023-2-SuaGradeUnB/pull/252).
- [Código, roteiro, massa e patch](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_ELIZABETH_FRIEDMAN/tree/main/avaliacao/melhoria-r04).
- [Instruções no commit do fork](https://github.com/LucasMF1/2023-2-SuaGradeUnB/blob/54c781189868b7138fbeb8659622fd3540cafdcb/web/tests/r04/README.md).

## Comportamento implementado

`SelectedClassesContext.tsx` mantém seleção e período juntos e grava o rascunho
nas ações aceitas. `draft.ts` serializa os identificadores, valida a estrutura
e restaura turmas consultando a API no período salvo. O formato é versionado
e limitado a 11 disciplinas e 4 turmas por disciplina, como a interface.

Período não oferecido invalida o rascunho; turmas que não existem mais são
retiradas. Mudar o período no contexto descarta a seleção anterior. O formulário
mantém o aviso existente e bloqueia a troca enquanto há seleção; depois de
remover as turmas é possível escolher outro período. Tanto remover a última
turma quanto limpar a seleção ao sair removem a chave do armazenamento.

Não há efeito que persista o estado vazio inicial. Uma ação do usuário durante
a consulta tem precedência sobre sua resposta. Falha da API mantém o rascunho e
mostra mensagem para tentar novamente por recarga. Armazenamento indisponível
não interrompe o uso em memória, mas não há garantia de recuperação nesse caso.

## Condições da comparação

| Condição | Antes | Depois |
|----------|-------|--------|
| Servidor Next 14.2.21 em desenvolvimento | `127.0.0.1:3045` | `127.0.0.1:3046` |
| Fonte | Commit original, sem alterações rastreadas; symlink de `node_modules` não rastreado | Commit corrigido, checkout limpo |
| Dependências do produto | Instaladas pelo mesmo `package-lock.json`; `node_modules` compartilhado por symlink | Instaladas por `npm ci` |
| API | Interceptada, massa sintética `massa.json` | A mesma massa e interceptação |
| Navegador | Chromium 151.0.7922.34 / Playwright 1.62.1 | Idêntico |
| Sistema / Node | Linux/WSL2 x64 / v24.22.1 | Idêntico |
| Tela de computador | 1366×900 | Idêntica |
| Tela de celular | 390×844, toque, escala 3, emulação Chromium | Idêntica |
| Sessão | Contexto novo, sem rascunho ou grades locais | Idêntica |

Não se comparou o site público diretamente com o fork. A falha original foi
reproduzida localmente antes de verificar o código corrigido no mesmo ambiente.
As portas diferentes permitem duas cópias independentes; os testes executam
sequencialmente. Login anônimo e dados de disciplina são controlados; a limpeza
completa usa resposta sintética de usuário autenticado, sem conta real.

## Procedimento R04

Em cada tela e variante: abrir `/schedules/home`, buscar `MAT0107` em `2026/2`,
expandir a disciplina, selecionar a primeira turma e fechar a busca. Conferir
um cartão, capturar a tela, carregar novamente a mesma URL, conferir a seleção
e capturar a tela. A nova carga do documento reproduz a perda de estado de uma
recarga. Antes, também foi verificada a ausência de diálogo de confirmação.

A massa usa o código de uma disciplina do cenário original, mas nome, IDs,
salas e docentes são **sintéticos**. Esta é uma reprodução controlada do mecanismo
de perda, sem alegar que os dados são uma réplica do SIGAA ou da sessão original.

| Tela | Estado selecionado na origem | Após recarga na origem | Após recarga na correção |
|------|------------------------------|------------------------|-------------------------|
| Computador | [1 turma](antes/computador-R04-selecionada.png) | [0 turmas, sem aviso](antes/computador-R04-recarregada.png) | [1 turma recuperada](depois/computador-R04-recarregada.png) |
| Celular emulado | [1 turma](antes/celular-R04-selecionada.png) | [0 turmas, sem aviso](antes/celular-R04-recarregada.png) | [1 turma recuperada](depois/celular-R04-recarregada.png) |

As capturas da seleção inicial corrigida também estão disponíveis:
[computador](depois/computador-R04-selecionada.png) e
[celular emulado](depois/celular-R04-selecionada.png).

## Verificações da correção

Cada item passou no computador e no celular emulado: **30/30 asserções de cenário**.

| Verificação | Resultado esperado e observado |
|-------------|-------------------------------|
| R04 | Mesma turma restaurada após recarga |
| Segunda recarga | Rascunho preservado, sem sobrescrita inicial vazia |
| Remoção parcial | Ao remover a primeira de duas turmas, só a segunda volta |
| Remoção da última turma | Chave removida; seleção continua vazia após recarga |
| Troca de período | Troca com seleção bloqueada; após limpar, não volta seleção antiga |
| Período indisponível | Período ausente da resposta da API invalida o rascunho |
| Dados inválidos | JSON truncado, `null`, versão errada e ID com tipo errado descartados |
| Dados atualizados | Sala modificada na API aparece na seleção recuperada |
| Turma obsoleta | Turma removida da API não é recuperada |
| API indisponível | HTTP 503 mantém o rascunho, mostra mensagem e permite recuperar em outra carga |
| Restauração concorrente | Resposta atrasada não sobrescreve período escolhido durante a recuperação |
| Outra aba | Nova aba independente, sem `opener`, começa sem rascunho |
| Limpeza completa | Sair limpa duas turmas via `setSelectedClasses(new Map())`; recarga não as recupera |
| Armazenamento indisponível | Exceções ao gravar/remover não quebram alterações em memória |
| JavaScript | Nenhum evento `pageerror` em cada execução |

Os quatro registros de “passou” na variante anterior significam que o roteiro
confirmou a perda em R04 e a ausência de exceções em cada tela; **não** significam
que a versão original passou no critério de proteção de M8.

## Registros e checagens

- [Metadados antes](antes/metadados.json) e [depois](depois/metadados.json), com commits, estado do checkout, versões e horários.
- [Resultados antes](antes/resultados.json) e [depois](depois/resultados.json), com cenário, tela, observação e horário.
- [Códigos de saída](checagens.json), [lint](depois/lint.txt) e checagem de tipos [antes](antes/tipos.txt) / [depois](depois/tipos.txt).

O lint terminou com código 0, sem avisos ou erros. A checagem de tipos não passou:
ambas as variantes apontaram `TS2344` nos tipos de rota gerados, por exportar
`poppins` em `app/layout.tsx`. Esse arquivo não foi alterado pela correção.
Não foi feita validação de build de produção; o resultado funcional é do
servidor de desenvolvimento.

## Teste manual com dados reais (21/11/2026)

Eduardo repetiu R04 à mão, no computador, para conferir a correção fora do roteiro
automatizado e com as disciplinas reais do período.

| Condição | Registro |
|----------|----------|
| Origem | `3d399e7` em `http://127.0.0.1:3045/schedules/home` |
| Correção | `54c7811` em `http://127.0.0.1:3046/schedules/home` |
| Servidor | `next dev` (Next 14.2.21), uma cópia por versão, com as mesmas dependências |
| API | Pública (`api.suagradeunb.com.br`), período 2026/2, por [`proxy-api.cjs`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_ELIZABETH_FRIEDMAN/tree/main/avaliacao/melhoria-r04/proxy-api.cjs) em `127.0.0.1:8999`, que repassa só GET; login responde 401 e gravações respondem 403 |
| Navegador | Google Chrome, Linux, as duas versões em abas da mesma janela |
| Sessão | Anônima, sem conta Google |
| Registro | [Gravação da tela, 40 s](manual/teste-manual-r04.mp4), sem áudio, reduzida para 1280×784 |

| Vídeo | Versão | Ação | Resultado | Captura |
|-------|--------|------|-----------|---------|
| 00:01 | Correção | Quatro turmas selecionadas: FGA0210 Paradigmas de Programação e FGA0242 Técnicas de Programação em Plataformas Emergentes, duas turmas de cada | — | [01](manual/01-corrigido-antes-de-recarregar.png) |
| 00:03 | Correção | Recarga da página | Tela de carregamento | [02](manual/02-corrigido-recarregando.png) |
| 00:06 | Correção | — | As quatro turmas voltam, com sala, horário e professor | [03](manual/03-corrigido-apos-recarregar.png) |
| 00:08–00:26 | Origem | Período 2026/2, busca "tecnicas de progra", seleção das duas turmas de FGA0242 | Duas turmas selecionadas | [04](manual/04-original-antes-de-recarregar.png) |
| 00:28–00:31 | Origem | Recarga da página | Seleção perdida sem aviso: "Nenhuma disciplina escolhida no momento" | [05](manual/05-original-apos-recarregar.png) |
| 00:34–00:37 | Correção | Nova recarga da mesma aba | As quatro turmas voltam de novo | [06](manual/06-corrigido-segunda-recarga.png) |

Observação: na correção, entre a tela de carregamento e o retorno das turmas, a lista
aparece vazia por cerca de 1 s (00:04 e 00:35), enquanto as turmas são consultadas na API.

O teste é uma única execução, num computador e sem participante. Ele confirma, com dados
reais, o mesmo resultado da verificação automatizada para R04, mas não mede o celular nem
substitui a repetição dos demais cenários de M8.

Para repetir: iniciar `node avaliacao/melhoria-r04/proxy-api.cjs`, criar em cada cópia
`web/.env.local` com `NEXT_PUBLIC_API_URL=http://127.0.0.1:8999` e subir os servidores nas
portas 3045 e 3046, como na [reprodução do roteiro](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_ELIZABETH_FRIEDMAN/tree/main/avaliacao/melhoria-r04/README.md).

## Alcance e entrega

Não foram repetidos todos os cenários do denominador de M8 nem as sessões com
participantes. Os resultados formais **3/4 no computador e 4/5 no celular**
permanecem preservados, sem novos percentuais ou mudança do julgamento global
de G3. Não se verificaram celular físico, Safari/Firefox, integração real com
SIGAA, login Google, salvamento na conta ou implantação pública da correção.

`sessionStorage` atende à recuperação da montagem na sessão da aba; não é um
salvamento permanente. Uma nova aba com `opener` pode receber uma cópia inicial
do armazenamento por comportamento do navegador; o teste usa aba independente.

O artefato do produto está publicado no fork. A documentação e as evidências
da avaliação estão neste repositório, em `docs/avaliacao/dados/acao-r04/` e
`avaliacao/melhoria-r04/`.
