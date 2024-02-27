def adicionar_contato(contatos, nome_contato):
    contato = {"nome": nome_contato, "favorito": False}
    contatos.append(contato)
    print(f"O contato {nome_contato} foi adicionado a sua lista!")
    return

def visualizar_contato(contatos):
    for indice, contato in enumerate(contatos, start=1):
        status = "Favoritado" if contato ["favorito"] else " "
        nome_contato = contato["nome"]
        print(f"{indice}. [{status}] {nome_contato}")

def alterar_contato(contatos, indice_contato, novo_contato):
    indice_contato_ajustado = int(indice_contato) - 1
    if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos):
        contatos[indice_contato_ajustado]["nome"] = novo_contato
        print(f"Contato {indice_contato} alterado para {novo_contato}")
    else:
        print("Indice do contato inválido.")
    return

def favoritar_contato(contatos, indice_contato):
    indice_contato_ajustado = int(indice_contato) - 1
    contatos[indice_contato_ajustado]["favorito"] = True
    print(f"Contato {indice_contato} marcado como favorito")
    return

def deletar_contato(contatos, indice_contato):
    indice_contato_ajustado = int(indice_contato) - 1
    if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos):
        contato_deletar = contatos[indice_contato_ajustado]
        contatos.remove(contato_deletar)
        print(f"Contato {indice_contato} foi deletado")
    else:
        print("Índice do contato inválido")
    return


contatos = []

while True:
    print("\nAgenda de contatos: ")
    print("1. Adicionar contato")
    print("2. Visualizar contatos")
    print("3. Alterar contato")
    print("4. Favoritar contato")
    print("5. Deletar contato")
    print("6. Sair")

    escolha = input("\nDigite a sua escolha: ")
    if escolha == "1":
        nome_contato = input("Informe o email do contato: ")
        adicionar_contato(contatos, nome_contato)

    elif escolha == "2":
        visualizar_contato(contatos)

    elif escolha == "3":
        visualizar_contato(contatos)
        indice_contato = input("Escolha qual contato alterar: ")
        novo_contato = input("Informe o contato: ")
        alterar_contato(contatos, indice_contato, novo_contato)
    
    elif escolha == "4":
        visualizar_contato(contatos)
        indice_contato = input("Marcar como favorito o contato: ")
        favoritar_contato(contatos, indice_contato)
    
    elif escolha == "5":
        visualizar_contato(contatos)
        indice_contato = input("Qual o contato deseja deletar: ")
        deletar_contato(contatos, indice_contato)

    elif escolha == "6":
        break

print("Programa finalizado.")