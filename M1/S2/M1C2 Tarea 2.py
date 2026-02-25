'''Crear un script en Python que emule el comportamiento de una calculadora.
La calculadora debe soportar las 4 operaciones básicas (suma, resta, multiplicación y división).
Debe preguntar los operandos y la operación en la entrada de la consola.'''
import math # libreria o módulo math

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: División por cero no permitida."
    return a / b

# (log,potencia,raízcuadrada,factorial).
def logaritmo(parametro):
    result = math.log(parametro)
    # operamos con el result
    return result

def potencia(a,b):
    return math.pow(a,b) # a**b

def raiz_cuadrada(a):
    return math.sqrt(a)

def factorial(a):
    return math.factorial(a)

def calculadora():
    print("Bienvenido a la calculadora Python")
    print("Operaciones disponibles:")
    print("1. Suma (+)")
    print("2. Resta (-)")
    print("3. Multiplicación (*)")
    print("4. División (/)")
    print("5. Logaritmo natural (ln)")
    print("6. Potencia (p)")
    print("7. Raíz cuadrada (r)")
    print("8. Factorial (!)")

    operacion = input("Seleccione una operación (+, -, *, /, ln, p, r, !): ")
    if operacion not in ['+', '-', '*', '/', 'ln', 'p', 'r', '!']: # si operacion no se encuentra dentro de el arreglo ['+', '-', '*', '/', 'ln', 'p', 'r', '!']
        print("Operación no válida.")
        return # termino de la función

    try:
        a = float(input("Ingrese el primer operando: "))

        # Para operaciones que necesitan dos operandos
        if operacion in ['+', '-', '*', '/', 'p']:
            b = float(input("Ingrese el segundo operando: "))
    except ValueError:
        print("Entrada no válida. Por favor ingrese números.")
        return

    if operacion == '+':
        resultado = suma(a, b) # a + b
    elif operacion == '-':
        resultado = resta(a, b)
    elif operacion == '*':
        resultado = multiplicacion(a, b)
    elif operacion == '/':
        resultado = division(a, b)
    elif operacion == 'ln':
        resultado = logaritmo(a)
        print(f"El resultado de {a} {operacion} es: {resultado}")

    #print(f"El resultado de {a} {operacion} {b} es: {resultado}")

calculadora()