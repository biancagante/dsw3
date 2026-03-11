from livro import Livro
from usuario import Usuario

class Biblioteca:
    def __init__(self):
        self.lista_livros = []
        self.lista_usuarios = []

    def adicionar_livro(self, livro):
        if livro not in self.lista_livros:
            self.lista_livros.append(livro)
            print("\033[92m✔ Livro adicionado à biblioteca\033[0m")
        else:
            print("\033[91m✖ Livro já adicionado à biblioteca\033[0m")

    def cadastrar_usuario(self, usuario):
        if usuario not in self.lista_usuarios:
            self.lista_usuarios.append(usuario)

    def listar_livros_disponiveis(self):
        print("\n\033[94m- Livros disponíveis:\033[0m")

        for l in self.lista_livros:
            if l.disponivel == True:
                print(f"Livro: {l.titulo} | Disponível: {"Sim" if l.disponivel else "Não"}")


    def listar_livros_emprestados(self):
        print("\n\033[93m- Livros emprestados:\033[0m")
        for l in self.lista_livros:
            if l.disponivel == False:
                print(f"Livro: {l.titulo} | Disponível: {"Sim" if l.disponivel else "Não"}")
        

    # def __str__(self):
    #     print(f"\nLista de livros: {self.lista_livros} \nLista de usuários: {self.lista_usuarios}")

# bibli = Biblioteca()

# livro1 = Livro("Cronicas", "NA", 1277, True)
# teste1 = Livro("Dorian gay", "Oscar", 1800, True)
# teste2 = Livro("Alice no pais das maravia", "Não sei", 1845, False)
# user1 = Usuario("Bianca", 123)

# bibli.adicionar_livro(teste1)
# bibli.adicionar_livro(teste1)
# bibli.adicionar_livro(livro1)
# bibli.adicionar_livro(teste2)
# bibli.cadastrar_usuario(user1)

# bibli.__str__()

# bibli.listar_livros_disponiveis()
# bibli.listar_livros_emprestados()