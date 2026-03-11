from biblioteca import Biblioteca
from livro import Livro
from usuario import Usuario

objBiblioteca = Biblioteca()

def menuOpcoes() :
    print("\n\033[93m- Escolha uma das opções abaixo: \033[0m\n1.Cadastrar livro\n2.Cadastrar usuário\n3.Realizar empréstimo\n4.Devolver livro\n5.Listar livros disponíveis\n6.Sair do programa")

def verificarUserELivro(biblioteca, operacao) :
    nome_matricula = str(input("Informe o nome ou matrícula do usuário: "))
    titulo = str(input("Informe o nome do livro: "))
    usuario = None
    livro = None

    for u in biblioteca.lista_usuarios:
        if nome_matricula == u.nome or nome_matricula == u.matricula:
            usuario = u
    
    if not usuario : return ("Usuário não encontrado")

    for l in biblioteca.lista_livros:
        if titulo == l.titulo:
            livro = l
    
    if not livro : return ("Livro não encontrado")
    
    operacao(usuario, livro)

def realizar_emprestimo(usuario, livro):
    usuario.pegar_emprestado(livro)

def realizar_devolucao(usuario, livro):
    usuario.devolver_livro(livro)

while True:
    menuOpcoes()
    opcaoEscolhida = int(input("\t\033[90m - Sua escolha: \033[0m"))

    match (opcaoEscolhida):
        case 1:
            print("\nCadastre um novo livro:")
            titulo = str(input("Título: "))
            autor = str(input("Autor: "))
            ano = int(input("Ano: "))
            objBiblioteca.adicionar_livro(Livro(titulo, autor, ano, True))
        case 2:
            print("\nCadastre um novo usuário")
            nome = str(input("Nome: "))
            matricula = input("Matrícula: ")
            objBiblioteca.cadastrar_usuario(Usuario(nome, matricula))
            print("\033[92mUsuário cadastrado com sucesso!\033[0m")

        case 3:
            print("\n\033[93m- Empréstimo de livro\033[0m")
            print(verificarUserELivro(objBiblioteca, realizar_emprestimo))

        case 4:
            print("\n\033[93m- Devolução de livro\033[0m")
            print(verificarUserELivro(objBiblioteca, realizar_devolucao))

        case 5:
            if len(objBiblioteca.lista_livros) == 0:
                print("Nenhum livro cadastrado.")
            else:
                objBiblioteca.listar_livros_disponiveis()

        case 6:
            print("Até mais!")
            break
        case _:
            print("Opção inválida!")

            # for user in bibliotecaAssis.lista_usuarios:
            #     print(f"Nome: {user.nome} | Matrícula: {user.matricula}")