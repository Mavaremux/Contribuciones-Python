agenda = {}


def insertar_contacto(name):
    phone = input("Ingrese un numero de telefono: ")
    if phone.isdigit() and len(phone) <= 11:
        agenda[name] = phone
        

def my_agenda():

    while True:

        print("1. Buscar un contacto.")
        print("2. Insertar un contacto.")
        print("3. Actualizar un contacto.")
        print("4. Eliminar un contacto.")
        print("5. Salir.")

        opcion = input("Ingrese una opcion (1-5)")
        match opcion:

            case "1": 
                name = input("Ingrese el contacto a buscar: ")
                if name in agenda:
                    print(f"El numero de telefono de {name} es {agenda[name]}")
                else:
                    print("Contacto no encontrado")

            case "2":
                name = input("Ingrese el contacto nuevo: ")
                insertar_contacto(name)
                print("Contacto agregado exitosamente")
                pass
            case "3":
                name = input("Que contacto quiere actualizar: ")
                if name in agenda:
                    del agenda[name]
                    insertar_contacto(name)
                else:
                    print("No se encontro el contacto")
            case "4":
                name = input("Ingrese el contacto a eliminar")
                if name in agenda:
                    del agenda[name]
                    print("Contacto eliminado exitosamente")
                else:
                    print("Contacto no encontrado")
            case "5":
                print("Adioss")
                
                break


my_agenda()