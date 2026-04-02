nome = input("Digite seu nome: ")
nomeItem = ""
peso = 0
lista = []

while peso < 23:
    nomeItem = input("\nNome do item: ")
    pesoItem = int(input("Peso do item: ")) 

    peso = peso + pesoItem

    if peso >= 23:
        print("\033[91m\nLimite excedido!\033[0m")
        peso = peso - pesoItem
        break
    elif "fim" in nomeItem or pesoItem == 0:
        break
    else: 
        lista += [nomeItem]

print("\nMochileiro(a):", nome)
print("Peso Total da Mochila:", peso, "kg")
print("Espaço restante: ", 23 - peso, "kg")
for item in lista:
    print(" ", item)
