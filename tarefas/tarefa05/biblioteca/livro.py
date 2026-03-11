class Livro:
    def __init__(self, titulo, autor, ano, disponivel):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.disponivel = disponivel

    def emprestar(self):
        if self.disponivel == True:
            self.disponivel = False
            print("\033[92m✔ Livro emprestado\033[0m")
            return True
        else:
            print("\033[91m✖ Livro não pôde ser emprestado\033[0m")
            return False

    def devolver(self):
        if self.disponivel == False:
            self.disponivel = True
            print("\033[94mLivro devolvido\033[0m")
            return True
        else:
            print("Livro já foi devolvido")
            return False

    def __str__(self):
        print(f"\nTítulo: {self.titulo} \nAutor: {self.autor} \nAno: {self.ano} \nDisponível: {self.disponivel}")


class LivroDigital(Livro):
    def __init__(self, titulo, autor, ano, disponivel, tamanho_arquivo):
        super().__init__(titulo, autor, ano, disponivel)
        self.tamanho_arquivo = tamanho_arquivo
        
    def __str__(self):
        print(f"\nTítulo: {self.titulo} \nAutor: {self.autor} \nAno: {self.ano}\nTamanho do Arquivo: {self.tamanho_arquivo}MB")


# teste1 = Livro("Dorian gay", "Oscar", 1800, True)
# teste2 = LivroDigital("Jorge", "NA", 2010, True, 15)

# teste2.__str__()
# teste1.__str__()

# teste1.emprestar()
# teste1.__str__()

# print(teste1.emprestar())
# teste1.__str__()

# print(teste1.emprestar())
# teste1.__str__()

# print(teste1.devolver())
# teste1.__str__()