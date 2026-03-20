 #Concatenacion

s1 = "Hola"
s2 = "Python"
#   Concatenacion

print(s1 + "","" + s2 + "!")

#Repeticion

print(s1 * 3)

#Indexacion

print(s1[0] + s1[1] + s1[2] + s1[3] )

#Longitud

print(len("Hola"))
print(len(s2))

#slicing ()
print(s2[:5])
print(s2[2:4])

#Busqueda

print("a" in s1)
print("x" in s2)

#Reemplazo 
print(s1.replace("o" , "a"))
print(s2.replace("P" , "T"))

#Division
print(s2.split("o"))

#Mayusculas y minus

print(s2.upper())
print(s1.lower())
print("alejandro mavares".title())
print("brais moure".capitalize())

#Eliminacion de espacios al principio y al final

print("  ALEJANDRO    MAVARES   ".strip() + "@MAVARES")

#Busqueda al principio y al final

print(s1.startswith ("Ho"))
print(s1.endswith("a"))

#Busqueda por posicion

print("Alejandro Mavares".find("Mavares")) #10
print("Alejandro Mavares".find("M")) #10
print("Alejandro Mavares".find("8")) #-1 no existe

#Busqueda de ocurrencias

print(s1.lower().count("o"))


#Formateo

print("Saludo:{}, Lenguaje: {} !" .format(s1,s2))

#Interpolacion

print(f"Saludo {s1} Lenguaje: {s2} ")

#Transformacion en lista de caracteres

s3 = "Programar"
print(list(s3))

l1 = [s1,",",s2, "!"]
print("-".join(l1))

#Transformaciones numericas

s4 = "0329039"
print(int(s4)) #igual con float etc

#Comprobaciones varias

print(s1.isalnum())
print(s4.isalpha())

#EXTRA

s8 = "Hola"
print(s8[::-1])

#Programa para encontrar palindromos, isogramas Y ANAGRAMAS

def check(palabra1: str, palabra2:str):
    print(f"{palabra1} es un palindromo? : {palabra1 == palabra1[::-1]}")
    print(f"{palabra2} es un palindromo? : {palabra2 == palabra2[::-1]}")

    print(f"{palabra1} es anagrama de {palabra2}?")
    if sorted(palabra1) == sorted(palabra2):
        print("Es un anagrama")
    else:
        print("No lo es")



    print(f"{palabra1} es isograma?: {len(set(palabra1)) == len(palabra1)}: ")
    print(f"{palabra2} es isograma?: {len(set(palabra2)) == len(palabra2)}")
    

    
check("Salas" , "Python")


