def main():
    # Solicitar los dos números al usuario
    numero1 = float(input("Ingresa el primer número: "))
    numero2 = float(input("Ingresa el segundo número: "))

    # Realizar los cálculos
    suma = numero1 + numero2
    resta = numero1 - numero2
    producto = numero1 * numero2
    cubo_suma = suma ** 3  # Elevar al cubo la suma
    cociente = numero1 / numero2 if numero2 != 0 else "Indefinido"  # Manejar división por cero

    # Imprimir los resultados
    print("\nResultados:")
    print("1. Suma:", suma)
    print("2. Resta:", resta)
    print("3. Producto:", producto)
    print("4. Cubo de la suma:", cubo_suma)
    print("5. Cociente:", cociente)

if __name__ == "__main__":
    main()