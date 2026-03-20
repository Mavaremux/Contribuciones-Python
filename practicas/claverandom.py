tareas = []

def agregar_tareas():
    tarea = input('Ingrese la tarea para agendar: ')
    tareas.append(tarea)
    print('Tarea Agregada correctamente')

def mostrar_tareas():
    if not tareas:
        print('No hay tareas agregadas')
    else:
        print('Lista de Tareas:')
        for idx, tarea in enumerate(tareas, start=1):
            print(f'{idx}. {tarea}')

def eliminar_tareas():
    mostrar_tareas()
    if tareas:
        idx = int(input('Ingrese la tarea a eliminar: '))
        if 1 <= idx <= len(tareas):
            tarea_eliminada = tareas.pop(idx - 1)
            print(f'Tarea {tarea_eliminada} eliminada correctamente')
        else:
            print('No pudo ser eliminada')

while True:
    print('Menu:')
    print('1. Agregar Tareas')
    print('2. Eliminar Tareas')
    print('3. Mostrar Tareas')
    print('4. Salir')
    
    opcion = input('Ingrese un numero valido en las opciones: ')
    if opcion == '1':
        agregar_tareas()
    elif opcion == '2':
        eliminar_tareas()
    elif opcion == '3':
        mostrar_tareas()
    elif opcion == '4':
        break
    else:
        print('Opcion invalida. Intente nuevamente.')
            
            

            
            
    