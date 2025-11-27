# utils.py
import datetime
import re
import uuid
from storage import carregar_dados

def gerar_id(prefix: str) -> str:
    mapping = {'u': 'usuarios', 'p': 'projetos', 't': 'tarefas'}
    entity = mapping.get(prefix)
    if not entity:
        return f"{prefix}_{uuid.uuid4().hex[:6]}"
    lista = carregar_dados(entity)
    seq = len(lista) + 1
    return f"{prefix}_{seq:03d}"

def validar_email(email: str) -> bool:
    if not email:
        return False
    email = email.strip()
    if len(email) > 80:
        return False
    regex = r'^[^@\s]+@[^@\s]+\.[^@\s]+$'    #se segue padrão de linguagem de eamil
    return re.match(regex, email) is not None

def validar_data(data_str: str) -> bool:
    if not data_str:
        return False
    try:                                    # bloco de tratamento de erro
        datetime.datetime.strptime(data_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def diferenca_datas(data_str1: str, data_str2: str) -> int:
    d1 = datetime.datetime.strptime(data_str1, "%Y-%m-%d").date()
    d2 = datetime.datetime.strptime(data_str2, "%Y-%m-%d").date()
    return (d1 - d2).days

def data_atual() -> str:
    return datetime.date.today().strftime("%Y-%m-%d")
