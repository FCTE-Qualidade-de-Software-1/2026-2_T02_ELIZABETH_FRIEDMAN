"""Massa de referência da avaliação (F3-C2).

Carrega no banco o mock do SIGAA versionado no produto (api/utils/mock/sigaa.html,
departamento 1499) no ano/período corrente, sem acesso à rede. Idempotente: apaga e
recria o departamento, restaurando o estado inicial.

Uso (no diretório do produto, com os serviços de pé):
  docker exec -i django-api python3 manage.py shell < <caminho>/seed_referencia.py
"""
import hashlib
from pathlib import Path

import requests
from django.db import transaction

from api.models import Department
from utils import db_handler as dbh
from utils.sessions import get_current_year_and_period
from utils.web_scraping import DisciplineWebScraper

MOCK = Path("utils/mock/sigaa.html")
SHA256_ESPERADO = "17ae00b1edcc0348c3dff66ef7709be26f8f3f2f5efc244ee65d54a198dead65"
DEPARTAMENTO = "1499"

conteudo = MOCK.read_bytes()
sha = hashlib.sha256(conteudo).hexdigest()
if sha != SHA256_ESPERADO:
    raise SystemExit(f"mock diferente do esperado: {sha}")


class _Resposta:  # objeto mínimo aceito pelo scraper
    content = conteudo


ano, periodo = get_current_year_and_period()
# session e cookie explícitos evitam a requisição ao SIGAA no construtor
scraper = DisciplineWebScraper(DEPARTAMENTO, ano, periodo,
                               session=requests.Session(), cookie={})
scraper.make_web_scraping_of_disciplines(_Resposta())

with transaction.atomic():
    # delete em QuerySet não passa pelo delete() do modelo (que exige o cache)
    Department.objects.filter(code=DEPARTAMENTO, year=ano, period=periodo).delete()
    depto = dbh.get_or_create_department(code=DEPARTAMENTO, year=ano, period=periodo)
    turmas_total = 0
    for codigo, turmas in scraper.disciplines.items():
        disc = dbh.get_or_create_discipline(name=turmas[0]["name"], code=codigo,
                                            department=depto)
        for t in turmas:
            dbh.create_class(teachers=t["teachers"], classroom=t["classroom"],
                             schedule=t["schedule"], days=t["days"],
                             _class=t["class_code"], special_dates=t["special_dates"],
                             discipline=disc)
            turmas_total += 1

print(f"massa carregada: {ano}/{periodo} depto {DEPARTAMENTO} "
      f"{len(scraper.disciplines)} disciplinas, {turmas_total} turmas, mock {sha[:12]}")
