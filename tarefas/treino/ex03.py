while True:
    numero = int(input("Insira um número: "))

    if numero % 2 == 0:
        print("\033[92mÉ par.\033[0m")

    else:
        print("\033[91mÉ ímpar.\033[0m")