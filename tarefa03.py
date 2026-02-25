inicio, fim = int(input("Escolha um número: ")), int(input("Escolha um número: "))
num_primos = []

if fim < inicio:
    inicio, fim = fim, inicio

print(f"inicio:{inicio} e fim:{fim}")

def eh_primo(numero):
    if numero < 2:
        return False
    for i in num_primos:
        if numero % i == 0:
            return False
    return True

x = inicio
while x <= fim:
    if eh_primo(x):
        num_primos.append(x)
    x = x + 1

print(f"\nLista de números primos: {num_primos}")
print(f"Quantidade de primos encontrados: {len(num_primos)}")
print(f"Menor primo encontrado: {num_primos[0]}")
print(f"Maior número encontrado: {num_primos[len(num_primos)-1]}")