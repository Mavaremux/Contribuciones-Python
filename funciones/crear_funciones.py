def saludar (nombre,sexo):
    sexo.lower()
    if (sexo == 'mujer'):
        adjetivo = 'reina'
    elif (sexo == 'hombre'):
     adjetivo = 'titan'
     
    else:
        adjetivo = 'amor'
        
    #print(f'Hola {nombre}, mi {adjetivo} , como andas?')
saludar('Camila', 'j')
        
    #crear una funcion que nos retorne valores
    
def crear_contrasena_random(num):
   chars = 'abcdefghij'
   num_entero = str(num)
   num = int(num_entero[0])
   c1 = num - 2
   c2 = num
   c3 = num - 5
   contrasena = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}"
   print(contrasena)
   
password = crear_contrasena_random(5)
frase = f"Tu contrasena es {password}"
print(frase)