
import math

# 1. Definimos las funciones PRIMERO
def calcular_cuadrado():
    lado1 = float(input("Ingrese el primer lado: "))
    lado2 = float(input("Ingrese el segundo lado: "))
    area = lado1 * lado2
    print(f"El área del cuadrado es: {area}")

def calcular_circulo():
    radio = float(input("Ingrese el radio: "))
    area = math.pi * (radio ** 2)
    print(f"El área de la circunferencia es: {area}")

def calcular_triangulo():
    base = float(input("Ingrese la base: "))
    altura = float(input("Ingrese la altura: "))
    area = (base * altura) / 2
    print(f"El área del triángulo es: {area}")

# 2. CUERPO PRINCIPAL DEL PROGRAMA
figura = input("¿Qué figura quieres calcular? (cuadrado, circunferencia, triangulo): ").lower()

if figura == "cuadrado":
    # Fíjate en los 4 espacios de sangría aquí
    calcular_cuadrado()

elif figura == "circunferencia":
    # Los dos puntos ':' al final son obligatorios
    calcular_circulo()

elif figura == "triangulo":
    calcular_triangulo()

else:
    print("Esa figura no existe en este programa.")