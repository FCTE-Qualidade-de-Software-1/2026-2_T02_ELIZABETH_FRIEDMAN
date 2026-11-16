# Guarda, organização e anonimização dos dados de G3

Complementa [dados.md](../../docs/avaliacao-interacao/dados.md) e
[registros.md](../../docs/avaliacao-interacao/registros.md) para a issue #44. Nada deste
arquivo substitui o termo de consentimento. **A equipe deve confirmar os pontos marcados
com (confirmar) antes de usar.**

## 1. Onde ficam os arquivos

| Material | Onde fica | Vai para o Git? |
|---|---|---|
| Termos assinados, nome e contato, chave código ↔ pessoa | Pasta restrita da equipe avaliadora (confirmar qual: pasta local ou armazenamento compartilhado com acesso só a Júlia, João e Kaleb) | Não |
| Gravações de tela e áudio, capturas originais | Mesma pasta restrita, subpasta `gravacoes/` | Não |
| Fichas e CSVs originais (`observacoes`, `recrutamento`, inventário M8 preenchido) | Mesma pasta restrita, subpasta `fichas/`. Cópia de trabalho local em `dados-restritos/` (ignorada pelo Git) | Não |
| Cópia anonimizada das observações e do inventário M8 | `docs/avaliacao/dados/g3/` | Sim, depois da revisão |
| Capturas revisadas (rosto, nome, e-mail e foto removidos) | `docs/avaliacao/dados/g3/capturas/`, só com autorização de publicação | Sim, se autorizado |

Vídeos e áudios nunca vão para o Git, nem em repositório privado.

## 2. Nomes de arquivo

Sem nome de pessoa. Usar o código pseudonimizado e a métrica:

```
P01_computador_conta_M6-M9_2026-11-15.mp4
P02_celular_conta_M6-M9_2026-11-16.mp4
M8_inspecao_2026-11-17.mp4
```

## 3. Conferência ao fim de cada sessão

- Termo assinado, com cópia entregue à pessoa e autorizações marcadas como `sim` ou `nao`.
- Código atribuído (P01, P02, ...) e chave guardada separada das observações.
- Gravação pausada durante o login Google, sem senha vista ou registrada.
- Ficha completa: IDs, resultados, tempos em ISO 8601, `estado_observacao` e `motivo` das inválidas.
- Grade salva na conta do participante: oferecida a exclusão ao final.
- Arquivos movidos para a pasta restrita e nada deixado em Downloads, área de trabalho ou repositório.

## 4. Anonimização para publicar

1. Partir da cópia de trabalho, nunca do original.
2. Remover nome, e-mail, foto e nome exibido da conta Google, IDs de conta e contatos.
3. Revisar o texto livre (`ajuda_detalhe`, `motivo`, `resultado_observado`) e os metadados.
4. Em capturas: recortar ou desfocar nome, e-mail, foto e itens da grade que identifiquem a pessoa.
5. Retirar horários exatos que permitam identificar a pessoa. Manter duração e contexto.
6. Publicar só o que a pessoa autorizou. Sem autorização de publicação, só resultados agregados.
7. Antes do `git add`, rodar `git status --short` e conferir que nenhum arquivo de gravação,
   termo ou recrutamento aparece. Nunca usar `git add .`.

## 5. Retirada e exclusão

Se alguém pedir a retirada dos dados, remover as observações e as evidências dessa pessoa,
recalcular a cobertura e registrar a execução sem dados pessoais. Na data de exclusão do termo,
apagar originais, chave de correspondência, cópias locais e backups controlados pela equipe.