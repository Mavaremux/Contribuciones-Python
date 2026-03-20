# Definir una lista para almacenar las tareas
tareas = []

# Función para agregar una tarea a la lista
def agregar_tarea():
    tarea = input("Ingrese la tarea a agregar: ")
    tareas.append(tarea)
    print("Tarea agregada correctamente.")

# Función para mostrar todas las tareas en la lista
def mostrar_tareas():
    if not tareas:
        print("No hay tareas en la lista de tu asistente Marchan")
    else:
        print("Lista de tareas:")
        for idx, tarea in enumerate(tareas, start=1):
            print(f"{idx}. {tarea}")

# Función para eliminar una tarea de la lista
def eliminar_tarea():
    mostrar_tareas()
    if tareas:
        idx = int(input("Ingrese el número de la tarea a eliminar: "))
        if 1 <= idx <= len(tareas):
            tarea_eliminada = tareas.pop(idx - 1)
            print(f"Tarea '{tarea_eliminada}' eliminada correctamente.")
        else:
            print("Número de tarea inválido.")
            
# Menú de opciones
while True:
    print("\nMenú:")
    print("1. Agregar tarea")
    print("2. Mostrar tareas")
    print("3. Eliminar tarea")
    print("4. Salir")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == '1':
        agregar_tarea()
    elif opcion == '2':
        mostrar_tareas()
    elif opcion == '3':
        eliminar_tarea()
    elif opcion == '4':
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida, Marchan no te quiere.")
