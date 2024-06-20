while True:
    try:
        #Ingrese los lados del triángulo
        lado_a = float(input("Ingresa la longitud del lado a: "))
        lado_b = float(input("Ingresa la longitud del lado b: "))
        lado_c = float(input("Ingresa la longitud del lado c: "))

        # Validar que los lados formen un triángulo
        if (lado_a + lado_b <= lado_c) or (lado_a + lado_c <= lado_b) or (lado_b + lado_c <= lado_a):
            raise ValueError("Los lados no forman un triángulo válido.")

        #Tipo de triángulo
        if lado_a == lado_b == lado_c:
            tipo_triangulo = "Equilátero"
        elif lado_a == lado_b or lado_b == lado_c or lado_a == lado_c:
            tipo_triangulo = "Isósceles"
        else:
            tipo_triangulo = "Escaleno"

        # Resultado
        print("El triángulo es:", tipo_triangulo)
        break  # Salir del bucle si los lados son válidos

    except ValueError as e:
        print(e)