while True: 
    try:
        # Datos del usuario
        temperatura = float(input("Ingresa la temperatura (°C): "))
        humedad = float(input("Ingresa la humedad (%): "))

        # Validar datos
        if temperatura < 0 or humedad < 0 or humedad > 100:
            raise ValueError("Datos inválidos. Deben ser valores positivos, y la humedad no puede exceder el 100%.")

        # Analizar condiciones y recomendar acciones
        if temperatura > 30:
            if humedad >= 30:
                print("Recomendación: Ventilación")
            else: 
                print("Recomendación: Riego y ventilación")
        else:  
            if humedad < 30:
                print("Recomendación: Riego")
            else:  
                print("No se necesitan acciones")

        # Preguntar
        otro_invernadero = input("¿Deseas analizar otro invernadero? (s/n): ")
        if otro_invernadero.lower() != 's':
            break  # Salir del bucle

    except ValueError as e:
        print(e)  # Datos inválidos
