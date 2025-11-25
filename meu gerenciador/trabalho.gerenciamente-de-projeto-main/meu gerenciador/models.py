# models.py
from storage import carregar_dados, salvar_dados, _ensure_data_dir
from utils import gerar_id, validar_data, validar_email, diferenca_datas

# garantir diretório e arquivos antes de operar
_ensure_data_dir()

def validar_usuario(dados_usuario):
    if not dados_usuario.get('nome'):
        return False
    email = dados_usuario.get('email')
    if not email or not validar_email(email):
        return False
    usuarios = carregar_dados('usuarios')
    for usuario in usuarios:
        if usuario['email'] == email and usuario.get('id') != dados_usuario.get('id'):
            return False
    return True

def validar_projeto(dados_projeto):
    if not dados_projeto.get('nome'):
        return False
    data_inicio = dados_projeto.get('data_inicio')
    data_fim = dados_projeto.get('data_fim')
    if not validar_data(data_inicio):
        return False
    if data_fim and not validar_data(data_fim):
        return False
    if data_fim and diferenca_datas(data_fim, data_inicio) < 0:
        return False
    projetos = carregar_dados('projetos')
    for projeto in projetos:
        if projeto['nome'] == dados_projeto['nome'] and projeto.get('id') != dados_projeto.get('id'):
            return False
    return True

def validar_tarefa(dados_tarefa):
    if not dados_tarefa.get('titulo'):
        return False
    projeto_id = dados_tarefa.get('projeto_id')
    prazo = dados_tarefa.get('prazo')
    status = dados_tarefa.get('status')
    projetos = carregar_dados('projetos')
    if not any(projeto['id'] == projeto_id for projeto in projetos):
        return False
    if not validar_data(prazo):
        return False
    if status not in ['pendente', 'em andamento', 'concluida']:
        return False
    return True

def criar_usuario(dados_usuario):
    if not validar_usuario(dados_usuario):
        return None
    dados_usuario['id'] = gerar_id('u')
    usuarios = carregar_dados('usuarios')
    usuarios.append(dados_usuario)
    salvar_dados('usuarios', usuarios)
    return dados_usuario

def criar_projeto(dados_projeto):
    if not validar_projeto(dados_projeto):
        return None
    dados_projeto['id'] = gerar_id('p')
    projetos = carregar_dados('projetos')
    projetos.append(dados_projeto)
    salvar_dados('projetos', projetos)
    return dados_projeto

def criar_tarefa(dados_tarefa):
    if not validar_tarefa(dados_tarefa):
        return None
    dados_tarefa['id'] = gerar_id('t')
    tarefas = carregar_dados('tarefas')
    tarefas.append(dados_tarefa)
    salvar_dados('tarefas', tarefas)
    return dados_tarefa
