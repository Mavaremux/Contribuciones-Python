def saludar():
    print("Hola, mundo!")

saludar()


def sumar(a, b):
    return a + b
resultado = print(f"El resultado de la suma es: {sumar(4, 5)}")




def funcion_externa(x):
    def funcion_interna(y):
        return y * 3
    print("Resultado de funcion_interna:", funcion_interna(x))

funcion_externa(4)


