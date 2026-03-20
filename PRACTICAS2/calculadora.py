print('Bienvenido a calcular')
is_running = True

def suma():
    a = int(input("Ingrese un numero: "))
    b = int(input("Ingrese otro numero: "))
    c = a + b
    print('***************')
    print(c)
    print('***************')

def resta():
    a = int(input("Ingrese un numero: "))
    b = int(input('Ingrese otro numero'))
    c = a - b
    print('***************')
    print(c)
    print('***************')

def multiplicacion():
    a = int(input("Ingrese un numero: "))
    b = int(input('Ingrese otro numero: '))
    c = a * b
    print('***************')
    print(c)
    print('***************')

def division():
    a = int(input("Ingrese un numero: "))
    b = int(input('Ingrese otro numero: '))
    c = a/b
    print('***************')
    print(c)
    print('****************')

def main():
    while is_running:
        print('1. Suma')
        print('2. Resta')
        print('3. Multiplicacion')
        print('4. Division')
        print('5. Cerrar')
        global is_running

        opcion = input('Elige una de las siguientes opciones (1-5): ')


        if opcion == "1":
            suma()
        elif opcion == "2":
            resta()
        elif opcion == "3":
            multiplicacion()
        elif opcion == "4":
            division()
        elif opcion == "5":
            
            is_running = False
        else:
            print('Opcion no valida')

if __name__ == '__main__':
    main()