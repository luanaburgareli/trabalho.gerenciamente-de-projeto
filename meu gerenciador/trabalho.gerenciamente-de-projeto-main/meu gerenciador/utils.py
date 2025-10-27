import uuid
import re
from datetime import datetime

def gerar_id(prefixo):
    return f"{prefixo}_{uuid.uuid4().hex[:8]}"

def validar_email(email):
    regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    return re.fullmatch(regex, email) is not None

def validar_data(data_str):
    try:
        datetime.strptime(data_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False
    
def diferenca_datas(date1_str, date2_str, date_format='%Y-%m-%d'):
    try:
        date1 = datetime.strptime(date1_str, date_format)
        date2 = datetime.strptime(date2_str, date_format)
        return (date1 - date2).days
    except ValueError:
        return None
    
def data_atual(date_format='%Y-%m-%d'):
    return datetime.now().strftime(date_format)
