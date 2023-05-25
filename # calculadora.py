# calculadora.py

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b

print("Calculadora Simple")
print("------------------")

while True:
    print("Operaciones disponibles:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

    opcion = input("Selecciona una operación (1-5): ")

    if opcion == "1":
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        resultado = sumar(num1, num2)
        print("El resultado es:", resultado)
    elif opcion == "2":
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        resultado = restar(num1, num2)
        print("El resultado es:", resultado)
    elif opcion == "3":
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        resultado = multiplicar(num1, num2)
        print("El resultado es:", resultado)
    elif opcion == "4":
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        resultado = dividir(num1, num2)
        print("El resultado es:", resultado)
    elif opcion == "5":
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, selecciona una opción válida (1-5).")