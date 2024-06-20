while True:
    try:
        numero = int(input("Ingresa un número: "))

        if numero % 2 == 0:
            print("El número es par")
        else:
            print("El número es impar")
        break 

    except ValueError:
        print("Entrada inválida. Por favor, ingresa un número entero.")