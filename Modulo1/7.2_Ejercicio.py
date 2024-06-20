import random

numero_secreto = random.randint(1, 10) 
adivinado = False                    

while not adivinado:   # Mientras no se haya adivinado
    try:
        numero = int(input("Adivina el número entre 1 y 10: "))
        if numero == numero_secreto:
            print("¡Felicitaciones XD!.")
            adivinado = True  # Para salir del bucle
        else:
            print("Fallaste XC.")
    except ValueError:
        print("Entrada inválida. Ingresa un número entero.")
