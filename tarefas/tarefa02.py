import random

def gerarNumAleatorios():
    lista_gerada = []
    i = 1

    while i <= 5:
        numero = random.randint(1, 10)

        if numero not in lista_gerada:
            lista_gerada.append(numero)
            i += 1
    return lista_gerada
    
def acertos (gerado, usuario):
    pontos = 0

    for n in usuario:
        if n in gerado:
            pontos += 1
    
    return pontos

lista_usuario = []
x = 1

while x <= 5:
    num = int(input("Digite um número: "))

    if num not in lista_usuario:
        lista_usuario.append(num)
        x += 1

numeros_gerados = gerarNumAleatorios()
print(f"Números sorteados: {numeros_gerados}")

pontuacao = acertos(numeros_gerados, lista_usuario)
print(f"Você fez {pontuacao} pontos!")