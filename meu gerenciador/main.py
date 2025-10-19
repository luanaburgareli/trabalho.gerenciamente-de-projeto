import datetime

usuarios = []
projetos = []
tarefas = []

# ============================
# Funções auxiliares
# ============================

def pausar():
    input("\nPressione ENTER para voltar ao menu...")

def validar_data(data_str):
    try:
        datetime.datetime.strptime(data_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

# ============================
# Usuários
# ============================

def menu_usuarios():
    while True:
        print("\n=== MENU USUÁRIOS ===")
        print("1. Cadastrar")
        print("2. Listar")
        print("3. Buscar por nome/e-mail")
        print("4. Atualizar")
        print("5. Remover")
        print("0. Voltar")
        opc = input("Escolha: ")

        if opc == "1":
            cadastrar_usuario()
        elif opc == "2":
            listar_usuarios()
        elif opc == "3":
            buscar_usuario()
        elif opc == "4":
            atualizar_usuario()
        elif opc == "5":
            remover_usuario()
        elif opc == "0":
            break
        else:
            print("Opção inválida.")

def cadastrar_usuario():
    nome = input("Nome: ").strip()
    email = input("E-mail: ").strip().lower()

    if not nome:
        print("Erro: nome não pode ser vazio.")
        return
    if any(u['email'] == email for u in usuarios):
        print("Erro: e-mail já cadastrado.")
        return

    usuario = {"id": f"u_{len(usuarios)+1:03}", "nome": nome, "email": email}
    usuarios.append(usuario)
    print("Usuário cadastrado com sucesso!")

def listar_usuarios():
    if not usuarios:
        print("Nenhum usuário cadastrado.")
    else:
        for u in usuarios:
            print(f"{u['id']} - {u['nome']} ({u['email']})")

def buscar_usuario():
    termo = input("Digite nome ou e-mail: ").lower()
    encontrados = [u for u in usuarios if termo in u['nome'].lower() or termo in u['email']]
    if encontrados:
        for u in encontrados:
            print(f"{u['id']} - {u['nome']} ({u['email']})")
    else:
        print("Nenhum usuário encontrado.")

def atualizar_usuario():
    email = input("E-mail do usuário a atualizar: ").lower()
    for u in usuarios:
        if u['email'] == email:
            novo_nome = input("Novo nome (deixe vazio para manter): ").strip()
            novo_email = input("Novo e-mail (deixe vazio para manter): ").strip().lower()

            if novo_nome:
                u['nome'] = novo_nome
            if novo_email and not any(x['email'] == novo_email and x != u for x in usuarios):
                u['email'] = novo_email
            elif novo_email:
                print("Erro: e-mail já existe.")
                return
            print("Usuário atualizado com sucesso!")
            return
    print("Usuário não encontrado.")

def remover_usuario():
    email = input("E-mail do usuário a remover: ").lower()
    global usuarios
    usuarios = [u for u in usuarios if u['email'] != email]
    print("Usuário removido (se existia).")

# ============================
# Projetos
# ============================

def menu_projetos():
    while True:
        print("\n=== MENU PROJETOS ===")
        print("1. Cadastrar")
        print("2. Listar")
        print("3. Buscar")
        print("4. Atualizar")
        print("5. Remover")
        print("0. Voltar")
        opc = input("Escolha: ")

        if opc == "1":
            cadastrar_projeto()
        elif opc == "2":
            listar_projetos()
        elif opc == "3":
            buscar_projeto()
        elif opc == "4":
            atualizar_projeto()
        elif opc == "5":
            remover_projeto()
        elif opc == "0":
            break
        else:
            print("Opção inválida.")

def cadastrar_projeto():
    nome = input("Nome do projeto: ").strip()
    descricao = input("Descrição: ").strip()
    inicio = input("Data de início (YYYY-MM-DD): ").strip()
    fim = input("Data de fim (YYYY-MM-DD): ").strip()

    if any(p['nome'].lower() == nome.lower() for p in projetos):
        print("Erro: nome de projeto já existe.")
        return
    if not (validar_data(inicio) and validar_data(fim)):
        print("Erro: datas inválidas.")
        return
    if inicio > fim:
        print("Erro: data de início deve ser anterior ou igual à data de fim.")
        return

    projeto = {"id": f"p_{len(projetos)+1:03}", "nome": nome, "descricao": descricao, "inicio": inicio, "fim": fim}
    projetos.append(projeto)
    print("Projeto cadastrado com sucesso!")

def listar_projetos():
    if not projetos:
        print("Nenhum projeto cadastrado.")
    else:
        for p in projetos:
            print(f"{p['id']} - {p['nome']} ({p['inicio']} → {p['fim']})")

def buscar_projeto():
    termo = input("Digite o nome do projeto: ").lower()
    encontrados = [p for p in pr]()
