while True:
    numero = int(input("Insira um número: "))

    if numero < 0: 
        print("\033[91mNegativo.\033[0m")
    
    elif numero == 0:
        print("\033[93mÉ zero.\033[0m")

    else:
        print("\033[92mPositivo.\033[0m")
