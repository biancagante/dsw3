nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
nota3 = float(input("Nota 3: "))

def media(a, b, c):
    return ((a + b + c) / 3)

if media(nota1, nota2, nota3) >= 7:
    print(f"\033[92m{round(media(nota1, nota2, nota3), 2)} - Aprovado.\033[0m")

else:
    print(f"\033[91m{round(media(nota1, nota2, nota3), 2)} - Reprovado.\033[0m")