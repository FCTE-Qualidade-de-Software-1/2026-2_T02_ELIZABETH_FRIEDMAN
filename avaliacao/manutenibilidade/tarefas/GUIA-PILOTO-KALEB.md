# Piloto de C1/C2 em outra máquina — Kaleb

Este guia prepara o piloto M1.3 da issue #38. Lucas fica reservado para a coleta formal. Não compartilhar as soluções ou patches com Lucas antes dessa coleta.

## Antes da sessão, fora do cronômetro

1. Instalar Git, Docker Engine/Desktop, Docker Compose, Python 3 e Make. Conferir `docker ps` e `docker compose version`.
2. Obter este repositório de avaliação para consultar as fichas C1.md e C2.md e a seção 2 da Fase 3. Não consultar soluções preparadas.
3. Criar duas cópias independentes do produto:

```bash
git clone https://github.com/unb-mds/2023-2-SuaGradeUnB.git suagrade-piloto-C1
git clone https://github.com/unb-mds/2023-2-SuaGradeUnB.git suagrade-piloto-C2
git -C suagrade-piloto-C1 checkout 3d399e745383b05e8e3b1a7c97ac0fdbf93a0360
git -C suagrade-piloto-C2 checkout 3d399e745383b05e8e3b1a7c97ac0fdbf93a0360
mkdir -p evidencias-kaleb/C1 evidencias-kaleb/C2
```

4. Preencher uma cópia da ficha de cada tarefa: executor Kaleb; data; máquina/SO; experiência com Python/Django; familiaridade com o SuaGradeUnB. O usuário informou que Kaleb conhece as linguagens; detalhes de experiência e familiaridade ainda não foram informados. Não presumir anos de experiência.
5. Dentro de `suagrade-piloto-C1`, preparar o ambiente e guardar a suíte inicial. Os comandos abaixo pressupõem as três pastas criadas lado a lado:

```bash
make config
docker compose up --build -d db redis api
docker compose ps
docker exec postgresql pg_isready -U suagradeunb
docker exec rediscache redis-cli ping
git rev-parse HEAD > ../evidencias-kaleb/C1/sha-inicial.txt
git status --short > ../evidencias-kaleb/C1/estado-inicial.txt
docker exec -w /usr/src/api django-api python3 manage.py test > ../evidencias-kaleb/C1/antes.log 2>&1
echo $? > ../evidencias-kaleb/C1/antes-codigo-saida.txt
```

6. Conferir o log e código 0. Falha inicial impede começar a medição. Guardar também versões dos serviços e ferramentas, sem copiar arquivos `.env` para as evidências.

## Durante cada tarefa

Ordem C1 → C2. Iniciar cronômetro monotônico ao receber/abrir a ficha da tarefa. Registrar início/fim com fuso e tempo decorrido. Incluir leitura, edição, depuração e espera pelos testes. Documentação e busca permitidas; sem IA nem ajuda de terceiros durante a medição.

Implementar a solicitação e os testes exigidos pela ficha. Guardar o comando dos testes de aceitação, sua saída em `aceitacao.log` e seu código de saída. Rodar também a suíte completa e guardar `depois.log` e o código. Encerrar quando os critérios passarem ou aos 90 minutos. Preencher o resultado e a lista de aceitação; não atribuir tempo de sucesso a uma tarefa incompleta.

Na raiz da cópia C1, execute os comandos abaixo durante a medição. Substitua
`pacote.tests.ClasseDeAceitacao` pelo identificador real dos testes criados;
registre esse identificador para permitir reprodução. Para C2, substitua também
o diretório de evidências. Não iniciar esses comandos com o identificador de exemplo.

```bash
printf '%s\n' 'docker exec -w /usr/src/api django-api python3 manage.py test pacote.tests.ClasseDeAceitacao' > ../evidencias-kaleb/C1/aceitacao-comando.txt
docker exec -w /usr/src/api django-api python3 manage.py test pacote.tests.ClasseDeAceitacao > ../evidencias-kaleb/C1/aceitacao.log 2>&1
echo $? > ../evidencias-kaleb/C1/aceitacao-codigo-saida.txt
docker exec -w /usr/src/api django-api python3 manage.py test > ../evidencias-kaleb/C1/depois.log 2>&1
echo $? > ../evidencias-kaleb/C1/depois-codigo-saida.txt
```

Saída esperada: ambos os códigos iguais a `0`, testes novos efetivamente
descobertos e resumo `OK` nos logs. Conferir também cada item da ficha; um
comando bem-sucedido com zero testes não comprova aceitação.

Na ficha preenchida, registrar: início/fim com fuso, segundos do cronômetro
monotônico, minutos (`segundos / 60`), ferramenta de cronometragem, resultado
(sucesso/insucesso/Não avaliado), motivo, desvios e localização de guarda dos
artefatos. Não usar apenas a diferença entre horários de parede, sujeita a
ajustes do relógio. Não arredondar minutos antes de aplicar as faixas da Fase 2.

## Depois de cada tarefa, fora do cronômetro

Guardar a ficha preenchida e selecionar explicitamente apenas os arquivos da tarefa para o patch:

```bash
git status --short
# Substituir os caminhos pelos arquivos alterados e testes novos da tarefa:
git add -- caminho/arquivo-alterado caminho/teste-novo
git diff --cached --binary > ../evidencias-kaleb/C1/mudanca.patch
git diff --cached --stat > ../evidencias-kaleb/C1/diff-stat.txt
git diff --cached --numstat > ../evidencias-kaleb/C1/diff-numstat.txt
git rev-parse HEAD > ../evidencias-kaleb/C1/sha-final.txt
```

Sem commit, SHA final pode ser igual ao inicial: o patch registra a alteração. Anotar isso na ficha. Registrar conferência dos critérios e logs, sem apresentar a autoavaliação como revisão independente.

Encerrar os serviços de C1 com `docker compose down`, sem `-v`. Entrar na cópia C2, repetir a preparação e a suíte inicial e executar a segunda tarefa. Trocar `C1` por `C2` nos caminhos de evidências. Confirmar que o contêiner da API usa a pasta C2 antes de medir.

## Entrega das evidências

Kaleb guarda os patches, testes e soluções até a coleta formal de Lucas. Pode informar agora os tempos, resultados de aceitação, identificação da máquina e dificuldades do procedimento sem revelar a solução. Informar a localização de guarda no relatório do piloto.

Após a sessão formal, integrar as evidências completas em `avaliacao/manutenibilidade/evidencias/piloto/M1.3/{C1,C2}/`. A guarda restrita não dispensa evidência verificável do piloto. Não marcar C1/C2 como executadas antes da sessão real.
