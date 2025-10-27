def pausar():
    input("\nPressione ENTER para voltar ao menu...")



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

