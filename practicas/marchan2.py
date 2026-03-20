import math

# Definimos las funciones (asegúrate de que estén arriba)
def area_cuadrado(v1, v2):
    resultado = v1 * v2
    print(f"El área del cuadrado es: {resultado}")

def area_circunferencia(radio):
    resultado = math.pi * (radio ** 2)
    print(f"El área de la circunferencia es: {resultado}")

# --- FLUJO PRINCIPAL ---

# 1. Pedimos la figura y la convertimos a minúsculas inmediatamente
figura = input("Ingrese la forma geométrica: ").lower()

# 2. Estructura de decisión (Ojo con los : y los espacios)
if figura == "cuadrado":
    # Todo esto debe estar alineado (4 espacios adentro)
    v1 = float(input("Ingrese el lado 1: "))
    v2 = float(input("Ingrese el lado 2: "))
    area_cuadrado(v1, v2)

elif figura == "circunferencia": # <-- ¡No olvides los dos puntos!
    # Esto también debe estar alineado (4 espacios adentro)
    r = float(input("Ingrese el radio: "))
    area_circunferencia(r)

elif figura == "triangulo":
    # ... código para triángulo ...
    pass 

else:
    print("Figura no reconocida.")