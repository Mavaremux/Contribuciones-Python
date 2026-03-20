

#funcion con retorno de varios valores

#def funcion_multiple_greet():
    #return "Hola" , "Python"

#
   # for name in names:
 #funcion_variable_greet("Alena" , "Alejandro" , "Claudio")


def variable_key_arg_greet(**names):
    for key, value in names.items():
        print(f"Hola {key}, {value}")


variable_key_arg_greet(
        language = "Python",
        Computadora = "HP",
        software = " Windows 11"
)