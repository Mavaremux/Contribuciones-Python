#creamos un conversor de medidas longitud usando try except

#definimos la funcion

while True:
    print(" Conversor de medidas.")
    print("1. Kilometros a Millas.")
    print("2. Celsius a Farenheit.")
    print("3. Kilogramos a Libras")
    print("4. Salir")
    try:
        opcion = int(input("Ingrese la opcion (1-4): "))


        if opcion == 4: 
            print("Adios")
            break

        elif opcion == 1:
         conversion1 = float(input("Ingrese el valor a convertir"))
         print(f"{conversion1}km a millas son {conversion1 * 0.621371}millas")

        elif opcion == 2:
            conversion2 = float(input("Ingrese el valor en celsius "))
            print(f"{conversion2} grados celsius a farenheit son {conversion2*1.8 + 32} farenheit")
    
        elif opcion == 3: 
            conversion3= float(input("Ingrese los kilogramos a convertir"))
            print(f"{conversion3}kilos a libras son {conversion3*2.2046}")

    except:
        print("Error, ingrese un numero valido")





  

         
