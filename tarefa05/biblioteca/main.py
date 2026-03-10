from biblioteca import Biblioteca
from usuario import Usuario

bibliotecaAssis = Biblioteca()

def menuOpcoes() :
    print("\033[93m- Escolha uma das opções abaixo: \033[0m\n1.Cadastrar livro\n2.Cadastrar usuário\n3.Realizar empréstimo\n4.Devolver livro\n5.Listar livros\n6.Sair do programa")

while True:
    menuOpcoes()
    opcaoEscolhida = int(input("\t\033[90m - Sua escolha: \033[0m"))

    match (opcaoEscolhida):
        case 1:
            pass
        case 2:
            print("Cadastre um novo usuário")
            nome = str(input("Nome: "))
            matricula = input("Matrícula: ")
            bibliotecaAssis.cadastrar_usuario(Usuario(nome, matricula))

            for user in bibliotecaAssis.lista_usuarios:
                print(f"Nome: {user.nome} | Matrícula: {user.matricula}")

        case 6:
            print("Até mais!")
            break
        case _:
            print("Opção inválida!")