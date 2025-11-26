# ui.py
def display_menu(title, options: dict) -> str:
    print(f"\n--- {title} ---")
    for key, val in sorted(options.items()):
        print(f"[{key}] {val}")
    print("[0] Voltar / Sair")
    escolha = input("Escolha: ").strip()
    if escolha in options or escolha == '0':
            return escolha
    else:
        print("Opção Inválida. Tente novamente.")

def display_entity_lista(lista, titulo="Lista"):
    print(f"\n--- {titulo} ---")
    if not lista:
        print("Nenhum registro encontrado.")
        return
    for item in lista:
        for k, v in item.items():
            print(f"{k}: {v}", end=" | ")
        print()

def display_relatorio(relatorio, titulo="Relatório"):
    print(f"\n--- {titulo} ---")
    if relatorio is None:
        print("Nenhum dado para exibir.")
        return
    if isinstance(relatorio, dict):
        for k, v in relatorio.items():
            print(f"{k}: {v}")
    else:
        print(relatorio)

