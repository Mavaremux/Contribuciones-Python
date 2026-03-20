import os

file_name = "Mavaresmux.txt"

with open(file_name , "w") as file:
    file.write("Alejandro Mavares\n")
    file.write("17 años\n")
    file.write("Me gusta python y SQL\n")


with open(file_name , "w") as file:

    print(file.read())

os.remove(file_name)


#EXTRA
open(file_name , "w")
while True:


    print("1. Añadir Producto")
    print("2. Consultar Producto")
    print("3. Actualizar Producto")
    print("4. Borrar Producto")
    print("5. Calcular la venta total")
    print("6. Calcular venta por producto")
    print("7. Mostrar productos")
    print("8. Salir")


    opc = input("Ingrese una opcion")

    if opc == 1:
        name = input("Ingrese el producto")
        quantity = input("Ingrese la cantidad de producto")
        prce = input("Ingrese el precio del producto")
        with open(file_name , "w") as file:

            file.write(f" {name} , {prce} , {quantity}\n")

    elif opc == 2:
        pass

    elif opc == 3:
        pass

    elif opc == 4:
        pass

    elif opc == 5:
        pass

    elif opc == 6:
        pass

    elif opc == 7:
        with open(file_name , "r") as file:
            print(file.read())
    elif opc == 8:
        os.remove(file_name)
        break

    else:
        print("Ingrese una opcion valida porfavor")