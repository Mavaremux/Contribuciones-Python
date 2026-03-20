#funcion dentro de otra funcion

def outer_funcion():
    def inner_funcion():
        print(" Funcion interna: Hola python")

    inner_funcion()

outer_funcion()


#build in funciones

print(len("Hola"))
print(type(True))


print("Alejandro".upper())


#variables locales y globales

global_variable = "python"
print(global_variable)

def hola_variable():
    local_var = "Php"
    print(f"Hola {global_variable} y {local_var}")

hola_variable()
#casi siempre hacer variables locales porque es una buena practica de programacion

#EXTRA

def print_numbersint(text1, text2)->int:
    count = 0
    for number in range (1, 101):
        
        if number % 5 == 0 and number % 3 == 0:
            print(text2 + text1)

        elif number % 5 == 0:
            print(text2)

        elif number % 3 == 0:
            print(text1)

        else:
            print(number)
            count += 1

    print(count)

print_numbersint("Texto1" , "Texto2")
