#Funciones definidas por el usuario

def saludar(nombre):
    print("Hola python")

saludar("Alejandro")


def retorn_saludar():
    return "Hola python"
print(retorn_saludar())

#Con un argumento

def saludar(nombre):
    print(f"Hola {nombre}")

saludar("alena")

#  Con varios argumentos

def args_greet(Nombre, Edad):
    print(f"Hola {Nombre}, es verdad que tienes {Edad} años?")

args_greet("Alejandro", 17)

#Con un argumento predeterminado

def args_default_greet(Nombre= " Usuario"):
    print(f"Hola{Nombre}")

args_default_greet(" Alejandro")
args_default_greet()
