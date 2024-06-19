
"""
Realiza un programa que solicite al usuario que introduzca tres números
luego realiza las siguientes verificaciones lógicas.

Paso 1: Solicitar tres números al usuario.
    Nota: Usa la función input() para pedir al usuario que introduzca tres números.
        La función float() se usa para convertir el valor introducido en un número decimal.
Paso 2: Verificar si los tres números son positivos.
Paso 3: Verificar si al menos uno de los números es negativo.
Paso 4: Verificar si el primer número es mayor que el segundo y el segundo es mayor que el tercero.
Paso 5: Mostrar los resultados.
    Nota: Usa la función print() para mostrar los resultados.
"""

num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))
num3 = float(input("Introduce el tercer número: "))

# Paso 2: Verificar si los tres números son positivos
todos_positivos = num1 > 0 and num2 > 0 and num3 > 0
print("¿Son todos los números positivos?", todos_positivos)

# Paso 3: Verificar si al menos uno de los números es negativo
al_menos_uno_negativo = num1 < 0 or num2 < 0 or num3 < 0
print("¿Al menos uno de los números es negativo?", al_menos_uno_negativo)

# Paso 4: Verificar si el primer número es mayor que el segundo y el segundo es mayor que el tercero
orden_descendente = num1 > num2 > num3
print("¿Los números están en orden descendente?", orden_descendente)

