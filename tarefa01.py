nome = input("Digite seu nome: ")
nomeItem = ""
peso = 0
lista = []

while peso < 23:
    nomeItem = input("Nome do item: ")
    pesoItem = int(input("Peso do item: ")) 

    if "fim" in nomeItem or pesoItem == 0:
        break;
    else:
        lista += [nomeItem]
        peso = peso + pesoItem

print("Mochileiro(a):", nome)
print("Peso Total da Mochila:", peso, "kg")
print("Espaço Livre:", 23 - peso, "kg")
print("Lista de itens: ")
for item in lista:
    print(" ", item)
