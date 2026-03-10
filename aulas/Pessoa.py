import os

os.system('cls')

class Pessoa:
    total_pessoas = 0
    # Construtor 
    def __init__(self, _nome, _idade):
        self.nome = _nome
        self.idade = _idade
        Pessoa.total_pessoas += 1

    def __str__(self):
        print(f"Nome: {self.nome} | Idade: {self.idade}")

    def total(self):
        print(f"Total de pessoas: {Pessoa.total_pessoas}")
    
# Herança
class Aluno(Pessoa):
    def __init__(self, _nome, _idade, matricula, curso):
        super().__init__(_nome, _idade)
        self.matricula = matricula
        self.curso = curso

    def __str__(self):
        print(f"Nome: {self.nome} | Idade: {self.idade} | Matricula: {self.matricula} | Curso: {self.curso}")

a1 = Aluno("Maria Clara", 19, 1234, "DSM")
a1.__str__()

p1 = Pessoa("Bianca", 19)
p2 = Pessoa("Maria Vitória", 18)
p1.__str__()
p2.__str__()
p1.total()