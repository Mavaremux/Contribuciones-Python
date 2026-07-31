import string

def lenghtpass(pswrd):
    if len(pswrd) > 8:
        print(f"Filtro longitud pasado, tu clave tiene {len(pswrd)} caracteres")
    else:
        print("Filtro longitud errado, clave muy corta")

def charsp(pswrd):
    syssp = sum(1 for c in pswrd if c in string.punctuation)
    print(f"Hay {syssp} caracteres especiales en tu clave")
    if syssp > 3:
        print("Caracteres especiales aprobados")
    else:
        print("Genera otra contraseña")

def charnum(pswrd):
    sysnum = sum(1 for c in pswrd if c in string.digits)
    print(f"Hay {sysnum} numeros en tu clave")
    if sysnum > 3:
        print("Caracteres numericos aprobados")
    else:
        print("Genera otra contraseña")

# --- PEDIMOS LA CLAVE UNA SOLA VEZ AQUÍ ---
genpass = input("Escriba la clave que genero el gen: ")

while True:
    print("\nMENU SEGURIDAD CONTRASEÑAS")
    print("1-Filtro Longitud")
    print("2-Filtro Caracteres especiales")
    print("3-Filtro Numeros")
    print("4-Salir")
    print("5-Aplicar todos los filtros")

    opc = input("\nEscriba la opcion a ejecutar: ")

    if opc == "1":
        lenghtpass(genpass)
    elif opc == "2": 
        charsp(genpass)
    elif opc == "3":
        charnum(genpass)
    elif opc == "4":
        print("¡Hasta luego!")
        break
    elif opc == "5":
        lenghtpass(genpass)
        charsp(genpass)
        charnum(genpass)

        

 


