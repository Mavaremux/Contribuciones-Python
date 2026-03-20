def modificar_lista(lista):
    lista.append(4)  # Modificamos el objeto original
    print(f"Dentro: {lista}")

mi_lista = [1, 2, 3]
modificar_lista(mi_lista)
print(f"Fuera: {mi_lista}")  # ¡Ahora tiene el 4!


#Tipos de dato por referencia

my_listaa = [10, 20]
my_listab = [30, 40]
my_listab = my_listaa


my_listab.append(20) # Se añadio tambien a la lista a por tener igual en el principio
print(my_listaa)
print(my_listab)



#Funciones de datos por valor
my_intc = 10
def datos_valor_Func(my_int: int):
    my_int = 20
    print(my_int)
   

datos_valor_Func(my_intc)
print(my_intc)
   
#Funciones con datos por referencia


def my_list_func(my_list: list):
    my_list.append(30)
    my_list_d = my_list
    my_list_d.append(40)
    print(my_list)
    print(my_list_d)


my_listc = [10,20]
my_list_func(my_listc)
print(my_listc)


#EXTRA

#FUNCION RETORNO Y REVERSA DE DATO POR VALOR

def value(value_a: int , value_b: int) -> tuple:
    temp = value_a
    value_a = value_b
    value_b = temp
    return value_a, value_b #Usamos una variable auxiliar para intercambiar los valores

my_int_d = 20
my_int_e = 30
my_int_f , my_int_g = value(my_int_d,my_int_e)

print(f"{my_int_d} , {my_int_e}")
print(f"{my_int_f} , {my_int_g}")

#Funcion lo mismo por referencia

def ref(list_a: list , list_b: list) -> tuple:
    temp = list_a
    list_a = list_b
    list_b = temp
    return list_a, list_b 


my_list_d = [" Hola " " Chao "]
my_list_e = [" Como estas " " Todo bien "]

my_list_f , my_list_g = ref(my_list_d,my_list_e)

print(f"{my_list_d} , {my_list_e}")
print(f"{my_list_f} , {my_list_g}")
