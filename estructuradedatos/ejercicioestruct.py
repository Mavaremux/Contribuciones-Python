#tuplas ()
#diccionarios o sets {}
#listas []



#LISTAS

my_list = ["Brais" , "Blak" , "Alejandro"]
print(my_list)

my_list.append("Alena") # insercion
print(my_list)

my_list.sort()
print(my_list) #ordena alfabeticamente

my_list.remove("Brais") # eliminacion
print(my_list)

print(my_list[1])
my_list[1] = "Albert" # actualizacion

print(my_list)

#TUPLAS

my_tuple = ("Brais" , "Moure" , "Dev")
print(type(my_tuple))

print(sorted(my_tuple)) 
print(my_tuple[2])   #acceso


#Sets

my_set = {"Brais" , "Moure" , "Dev"}
print(type(my_set))
my_set.add("Alejandro")  #INSERCION
print(my_set)
my_set.add("Alejandro")
print(my_set) #el set evita los duplicados

my_set.remove ("Alejandro")
print(my_set) #Eliminacion

#por definicion el set no es una estructura ordenada


#Diccionarios
#trabaja key-value
my_dict : dict = {    
    "Nombre":"Alejandro",
    "Apellido":"Mavares",
    "Edad": "17" ,

}

for keys,values in my_dict.items(): #se utiliza items para colocar keys-value
    print(f"Datos {keys} : {values}")



 # print(my_dict[0]) # No se puede, se accede a los valores por su key

#Agregar

my_dict["Gmail"] = "mavaresxd@gmail.com"
print(my_dict)

#Acceso

print(my_dict["Apellido"]) #Compila mavares

#actualizacion 
 
my_dict["Edad"] = "18"
print(my_dict)


#ordenacion

my_dict = dict(sorted(my_dict.items()))
print(my_dict)



#EXTRA

#AGENDA DE OCNTACTOS CON INSERCION, ACTUALIZACION, ELIMINACION , Y BUSQUEDA DE CONTACTOS

print("-*100")

agenda = {}






input("hola: ")
    
