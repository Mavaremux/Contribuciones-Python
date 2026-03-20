#Pila / Stack (LIFO : Last In , First Out)

stack = []
stack.append("1")
stack.append("2") #push
stack.append("3")

print(stack)

stack_item = stack[len(stack)-1] #pop desapilar
del stack[len(stack)-1]
print(stack_item) 

print(stack.pop())
print(stack)



#Cola / Queue (FIFO : First In, First Out)

queue = []

#enqueue
queue.append("1")
queue.append("2")
queue.append("3")

#denqueue

queue_item = queue[0]
del queue[0]
print(queue_item)

print(queue.pop(0))

print(queue)


#EXTRA

#nAVEGADOR

def web_browser():
    stack = []
    while True:
        accion = input("Ingrese la accion a obtener (URL) Adelante/Atras/ Salir")

        if accion.lower() == "salir":
            print("Adios")
            break
        elif accion.lower() == "adelante":
            pass
        elif accion.lower() == "atras":
            if len(stack) > 0:
                stack.pop()
            else:
                print("Estas en la pagina de inicio")

        else:
            stack.append(accion)
        
            if len(stack) > 0:
                 print(f"Haz navegado hasta {stack[len(stack)-1]}")
            else:
                 print("Estas en el inicio")

#web_browser()

#Impresora

def impresoracomp():
    
    queue =[]

    while True:
        action = input("Añade un documento o selecciona imprimir/salir: ")

        if action == "salir":
            break
        elif action == "imprimir":
            if len(queue) > 0:
                print(f"Imprimiendo: {queue.pop(0)}")
        else:
            queue.append(action)

        print(f"Cola de impresion {queue}")



impresoracomp()