num1, num2 = int(input("Insira um número: ")), int(input("Insira um número: "))

def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def divisao(a, b):
    return a / b

def multiplicacao(a, b):
    return a * b

print(round(soma(num1, num2), 2))
print(round(subtracao(num1, num2), 2))
print(round(divisao(num1, num2), 2))
print(round(multiplicacao(num1, num2), 2))