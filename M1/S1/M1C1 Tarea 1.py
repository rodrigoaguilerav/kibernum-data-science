'''Crear un script en Python que emule el comportamiento de una calculadora.
La calculadora debe soportar las 4 operaciones básicas (suma, resta, multiplicación y división).
Debe preguntar los operandos y la operación en la entrada de la consola.'''

print("Bienvenido a la calculadora Python")
print("Operaciones disponibles:")
print("1. Suma (+)")
print("2. Resta (-)")
print("3. Multiplicación (*)")
print("4. División (/)")

operacion = input("Seleccione una operación (+, -, *, /): ")
if operacion not in ['+', '-', '*', '/']: # si operacion no esta en el arreglo
    print("Operación no válida.") # imprime en terminal
else: # no sucede o ejecuta el if, porque no cumple la condición, entonces:
    try: # intentar ejecutar el siguiente codigo
        a = float(input("Ingrese el primer operando: "))
        b = float(input("Ingrese el segundo operando: "))
    except ValueError:
        print("Entrada no válida. Por favor ingrese números.")
    else:
        if operacion == '+':
            resultado = a + b
        elif operacion == '-':
            resultado = a - b
        elif operacion == '*':
            resultado = a * b
        elif operacion == '/':
            if b == 0:
                resultado = "Error: División por cero no permitida."
            else:
                resultado = a / b
        print(f"El resultado de {a} {operacion} {b} es: {resultado}")

    calculadora()
    