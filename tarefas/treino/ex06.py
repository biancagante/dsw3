lista = []

def somaAcumulada(numero):
    lista.append(numero)
    soma = 0
    for i in lista:
        soma += i

    return soma

while True:
    numero = int(input("Digite um número: "))

    print(somaAcumulada(numero))
    if numero == 0:
        break
    