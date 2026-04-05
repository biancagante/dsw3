class Quiz:
    def __init__(self, nome, pontuacao):
        self.nome = nome
        self.pontuacao = pontuacao

    def iniciarQuiz(self, lista_perguntas):
        nome = str(input("\nOlá, seja bem-vindo(a) ao Quiz Simulado P1! \n\n\t- Digite seu nome para iniciarmos: "))
        self.nome = nome
        self.perguntar(lista_perguntas)
        self.__str__()

    def perguntar(self, lista):
        for p in lista:
            print("\033[36m----------------------------------------------------\033[0m")
            print(p['enunciado'], "\n")

            for a in p['alternativas']:
                print(a)

            self.responder(p['resposta'])

    def responder(self, resposta_correta):
        resposta = str(input("\n\tSua resposta: ")).strip().capitalize()
        if resposta == resposta_correta:
            self.pontuacao += 1
        
    def classificarDesempenho(self):
        if self.pontuacao <= 14:
            return "\033[1;31mEstude mais e você irá conseguir!\033[0m"
        
        elif self.pontuacao > 14 and self.pontuacao < 28:
            return "\033[1;33mBom desempenho, estude mais um pouco e você irá arrasar!\033[0m"

        else:
            return "\033[1;32mVocê arrasou!\033[0m"

    def __str__(self):
        resultado = self.classificarDesempenho()
        print(f"\nNome: {self.nome}  | Pontuação: {self.pontuacao} | Desempenho: {resultado}")
