inicio, fim = int(input("Escolha um número: ")), int(input("Escolha um número: "))
num_primos = []

if fim < inicio:
    inicio, fim = fim, inicio

def eh_primo(numero):
    if numero < 2:
        return False
    
    elif numero % 2 == 0 or numero % 3 == 0 or numero % 5 == 0 or numero % 7 == 0 or numero % 11 == 0:
        return False
        
    return True

inicio
while inicio <= fim:
    if eh_primo(inicio):
        num_primos.append(inicio)
    inicio = inicio + 1

print(f"\nLista de números primos: {num_primos}")
print(f"Quantidade de primos encontrados: {len(num_primos)}")
print(f"Menor primo encontrado: {num_primos[0]}")
print(f"Maior número encontrado: {num_primos[-1]}")