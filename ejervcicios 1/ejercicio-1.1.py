while True:
    print("\n--- Conversor de medidas ---")
    print("1. Kilometros a Millas")
    print("2. Celsius a Farenheit")
    print("3. Kilogramos a Libras")
    print("4. Salir")

    try:
        # Aquí convertimos a entero. Si el usuario escribe "hola", salta al except.
        opcion = int(input("Ingrese la opcion (1-4): "))

        if opcion == 4: 
            print("Adios")
            break # Sale del bucle inmediatamente

        elif opcion == 1:
            valor = float(input("Ingrese kilómetros: "))
            print(f"{valor} km son {valor * 0.621371:.2f} millas")

        elif opcion == 2:
            valor = float(input("Ingrese celsius: "))
            print(f"{valor} °C son {valor * 1.8 + 32:.2f} °F")
    
        elif opcion == 3: 
            valor = float(input("Ingrese kilogramos: "))
            print(f"{valor} kg son {valor * 2.2046:.2f} libras")

        else:
            # Si pone un número como 8, esto evita que el programa solo reinicie en silencio
            print("Esa opción no existe. Intenta del 1 al 4.")

    except ValueError:
        # Esto captura errores de escritura (letras, símbolos)
        print("Error: ¡Debes ingresar un número válido!")