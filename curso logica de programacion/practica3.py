#realizar una check llist con funiones como mostrar tareas, eliminar tareas, agregar tareas y salir

tareas = []

#funcion para mostrar tareas

def agregar_tareas():
    tarea = input("Ingrese la tarea a agregar: ")
    tareas.append(tarea)
    print("Tarea agregada correctamente")
def mostrar_tareas():
    if not tareas:
        print("No hay tareas agregadas")
    else:
        print("Lista de Tareas: ")
        for idx, tarea in enumerate(tareas, start= 1):
            print(f"{idx}. {tarea}")

def eliminar_tareas():
    mostrar_tareas()
    if tareas:
       idx = int(input("Ingrese la tarea que quiere eliminar"))
       if 1<= idx <= len(tareas):
           tarea_eliminada= tareas.pop(idx-1)
           print("Tarea eliminada correctamente")

       else:
           print("Numero de tarea invalido")

while True:
    print("Menu de opciones: ")

    print(" Agregar Tareas")
    print(" Mostrar Tareas")
    print("Eliminar Tareas")
    print(" Salir")

    opcion = int(input("Ingrese lo que quiere hacer: "))
    if opcion == 1:
        agregar_tareas()

    elif opcion == 2:
        mostrar_tareas()

    elif opcion == 3:
        eliminar_tareas()

    elif opcion == 4:
        break


    else:
        print("NUMERO INVALIDO INGRESE NUEVAMENTE")