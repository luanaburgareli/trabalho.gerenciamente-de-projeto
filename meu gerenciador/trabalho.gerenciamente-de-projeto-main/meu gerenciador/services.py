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
    encontrados = [p for p in projetos if termo in p['nome'].lower()]
    if encontrados:
        for p in encontrados:
            print(f"{p['id']} - {p['nome']} ({p['email']})")
    else:
        print("Nenhum usuário encontrado.")
    
def atualizar_projeto():
    id = input("Id do projeto que deseja atualizar: ").lower()
    for p in projetos:
        if p['id'] == id:
            novo_nome = input("Novo nome para o projeto (deixe vazio para manter): ").strip()
            novo_id = input("Novo Id par ao projeto (deixe vazio para manter): ")

            if novo_nome:
                p['nome'] = novo_nome
            if novo_id and not any(x['id'] == novo_id and x != p for x in projetos):
                p['id'] = novo_id
            elif novo_id:
                print("Erro: ID já existente.")
                return
            print("Projeto atualizado com sucesso!")
            return
    print("Projeto não encontrado.")

def remover_projeto(): 
    id = input("Id do projeto a remover: ")
    global projetos
    projetos = [p for p in projetos if p['id'] != id]
    print("Projeto removido.")
