mamaguevos = ["maduro" , "diosdado", " padrino", " delcy"]
for mamaguevo in mamaguevos:
    print(f"Este es un becerro {mamaguevo}")
    if mamaguevo == "diosdado":
        print("este es el mas becerro, asesinenlo")
        asesinado= mamaguevos.pop(1)
        print(f"Los becerros restantes son {mamaguevos}")
        print(f"el asesinado fue el becerro de {asesinado}")
    else:
        continue

enumerate (mamaguevos, start= 1)w
