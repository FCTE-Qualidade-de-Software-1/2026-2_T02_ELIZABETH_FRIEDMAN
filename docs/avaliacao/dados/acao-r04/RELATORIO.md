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
da avaliação acompanham a branch `feat-Acao_melhoria`, para revisão antes do merge.
A #46 permanece inalterada a pedido do responsável, que registrará links e
horas reais. Não foi imputada a estimativa de 8 h como esforço realizado.
