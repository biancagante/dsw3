from livro import Livro

class Usuario:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        self.lista_livros = []

    def pegar_emprestado(self, livro):
        if livro.emprestar():
            self.lista_livros.append(livro)

    def devolver_livro(self, livro):
        if livro in self.lista_livros:
            livro.devolver()
            self.lista_livros.remove(livro)

    def __str__(self):
        livros_user = " "
        if self.lista_livros:
            livros_user = ", ".join(l.titulo for l in self.lista_livros)
        else:
            livros_user = "Nenhum"
        print(f"\nNome: {self.nome} | Matrícula: {self.matricula} | Livros emprestados: {livros_user}")

# person1 = Usuario("Bianca", 123)
# person1.__str__()

# teste1 = Livro("Dorian gay", "Oscar", 1800, True)
# teste2 = Livro("Alice no pais das maravia", "Não sei", 1845, True)
# person1.pegar_emprestado(teste1)

# person1.pegar_emprestado(teste1)

# person1.pegar_emprestado(teste2)
# person1.__str__()

# person1.devolver_livro(teste2)

# person1.__str__()