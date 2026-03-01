lista_telefonica = {
    "Ana": "13987654321",
    "Bruno": "11923456789",
    "Carla": "21999887766",
    "Daniel": "31987651234",
    "Eduarda": "27934561234",
    "Felipe": "41991234567",
    "Gabriela": "51987654321",
    "Henrique": "61999881234"
}

def formatarNumero(numero):
    return f"(+{numero[:2]}) {numero[2:7]}-{numero[7:11]}"

def menu():
    opcao = int(
        input("\n" \
        "Escolha uma ação: " \
        "\n1.Cadastrar novo contato" \
        "\n2.Buscar contato" \
        "\n3.Listar contatos" \
        "\n4.Excluir contato" \
        "\n5.Sair do programa" \
        "\n\t- Digite sua escolha: "
    ))

    return opcao

while True:
    match menu():
        case 1:
            nome, telefone = input("Novo contato: "), input("Telefone: ")

            if nome in lista_telefonica:
                print("Nome já cadastrado, ao continuar você irá atualizar o número de telefone.")

            lista_telefonica.update({str(nome):str(telefone)})
            print(f"Novo contato adicionado: {nome} - (tel): {formatarNumero(telefone)}")

        case 2:
            buscar = input("\nQual nome deseja encontrar: ")
            if buscar in lista_telefonica:
                    print(f"{buscar}: {formatarNumero(lista_telefonica[buscar])}")
            else:
                print("Nenhum contato com esse nome encontrado.")

        case 3:
            i = 1;
            print("\n--Lista de Contatos: ")
            for contato, tel in lista_telefonica.items():
                print(f"{i}.{contato}: {formatarNumero(tel)}")
                i = i + 1

        case 4:
            buscar = input("\nQual nome deseja deletar: ")
            if buscar in lista_telefonica:
                del lista_telefonica[buscar]
                print("Contato deletado.")
            else:
                print("Nenhum contato com esse nome encontrado.")

        case 5:
            print("Até mais, tenha um ótimo dia ❤")
            break
        case _:
            print("Opção inválida.")