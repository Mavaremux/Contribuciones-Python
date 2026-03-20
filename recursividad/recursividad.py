def funcion_recursiva(n):
    if n <= 0:
        return 
    print(n)
    funcion_recursiva(n-1)
funcion_recursiva(100)


#EXTRA

#Hacer una funcion con el factorial de numeros

def factorial(number : int)->int:
    if number < 0:
        print("Los numeros negativos no son validos")
        return 0
    elif number == 0:
        return 1

    else:
        return number * factorial(number -1)

print(factorial(0))


#Sucecion de fibonacci

def fibonacci(number: int ) -> int:

    if number <= 0:
        print("La posicion no puede ser negativa")
        return 0
    
    elif number == 1: 
        return 1
    
    elif number == 2:
        return 1

    else:
        return fibonacci(number -1 ) + fibonacci(number -2)
    
n = int(input("Ingrese el numero a calcular con la sucesion de fibonacci"))
print(f"La ubicacion de {n} en fibonacci es {fibonacci(n)}")
