#!/usr/bin/env bash
# Uso: bash cobertura.sh DIRETORIO_PRODUTO DIRETORIO_EVIDENCIAS
set -euo pipefail
base=$(cd "$(dirname "$0")" && pwd)
produto=$(realpath "$1")
mkdir -p "$2"
saida=$(realpath "$2")
exec > >(tee "$saida/execucao.log") 2>&1
trap 'code=$?; echo "$code" > "$saida/codigo-saida.txt"' EXIT
cd "$produto"
test "$(git rev-parse HEAD)" = 3d399e745383b05e8e3b1a7c97ac0fdbf93a0360
test -z "$(git status --porcelain --untracked-files=no)"
docker compose ps
docker exec django-api python3 -m coverage --version
docker cp "$base/configs/coverage.ini" django-api:/tmp/manutenibilidade-coverage.ini
docker exec -w /usr/src/api django-api python3 -m coverage debug --rcfile=/tmp/manutenibilidade-coverage.ini config
set +e
docker exec -e COVERAGE_FILE=/tmp/manutenibilidade.coverage -w /usr/src/api django-api python3 -m coverage run --rcfile=/tmp/manutenibilidade-coverage.ini manage.py test
testes=$?
set -e
echo "$testes" > "$saida/testes-codigo-saida.txt"
# Preservar relatórios parciais, sem usá-los para confirmar H1.4 em caso de falha.
docker exec -e COVERAGE_FILE=/tmp/manutenibilidade.coverage -w /usr/src/api django-api python3 -m coverage json --rcfile=/tmp/manutenibilidade-coverage.ini -o /tmp/manutenibilidade.json
docker exec -e COVERAGE_FILE=/tmp/manutenibilidade.coverage -w /usr/src/api django-api python3 -m coverage html --rcfile=/tmp/manutenibilidade-coverage.ini -d /tmp/manutenibilidade-html
docker cp django-api:/tmp/manutenibilidade.json "$saida/coverage.json"
docker cp django-api:/tmp/manutenibilidade-html "$saida/html"
cp "$base/configs/coverage.ini" "$saida/coverage.ini"
docker exec -e COVERAGE_FILE=/tmp/manutenibilidade.coverage -w /usr/src/api django-api python3 -m coverage json --rcfile=/tmp/manutenibilidade-coverage.ini --omit='*/tests/*,*/test_*.py,*/migrations/*,utils/json_pretty.py,api/admin.py,users/admin.py' -o /tmp/manutenibilidade-ci.json
docker cp django-api:/tmp/manutenibilidade-ci.json "$saida/comparacao-omit-ci.json"
exit "$testes"
