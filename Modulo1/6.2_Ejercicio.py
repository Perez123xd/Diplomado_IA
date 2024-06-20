while True:
    try:
        edad = float(input("Ingresa la edad: "))
        
        if 0 <= edad < 13:
            print("Categoría: Niño")
        elif 13 <= edad < 18:
            print("Categoría: Adolescente")
        elif 18 <= edad < 65:
            print("Categoría: Adulto")
        elif 65 <= edad <= 100:
            print("Categoría: Adulto Mayor")
        elif 100 <= edad <= 150:
            print("Categoría: Anciano con pie en tumba")
        else:
            print("Edad inválida. Ingresa una edad entre 0 y 150.")
            continue  # Volver al inicio del bucle si la edad es inválida

        break  # Salir del bucle si la edad es válida

    except ValueError:
        print("Entrada inválida. Por favor, ingresa un número.")