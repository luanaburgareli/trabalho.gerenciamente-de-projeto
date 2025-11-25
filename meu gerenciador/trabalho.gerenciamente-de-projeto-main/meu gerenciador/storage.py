# storage.py
import os
import json

DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
ENTITY_FILES = {
    'usuarios': 'usuarios.json',
    'projetos': 'projetos.json',
    'tarefas': 'tarefas.json'
}

def _ensure_data_dir():
    os.makedirs(DATA_DIR, exist_ok=True)
    for name, fname in ENTITY_FILES.items():
        path = os.path.join(DATA_DIR, fname)
        if not os.path.exists(path):
            with open(path, 'w', encoding='utf-8') as f:
                json.dump([], f, ensure_ascii=False, indent=2)

def iniciar_dados():
    """Inicializa data/ e arquivos JSON se necessário."""
    _ensure_data_dir()

def _path(entity_name):
    fname = ENTITY_FILES.get(entity_name)
    if not fname:
        raise ValueError(f"Entidade desconhecida: {entity_name}")
    return os.path.join(DATA_DIR, fname)

def carregar_dados(entity_name):
    _ensure_data_dir()
    path = _path(entity_name)
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception:
        return []

def salvar_dados(entity_name, data):
    _ensure_data_dir()
    path = _path(entity_name)
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
