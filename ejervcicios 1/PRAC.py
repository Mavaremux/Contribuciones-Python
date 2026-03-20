usuario = input(f'Escriba su nombre:')
print(f'Hecho, su nombre de usuario es { usuario}')




contrasena = input (f"Escribe tu contrasena (Minimo 5 caracteres)")
contar_caracteres = len(contrasena)

if contar_caracteres > 5:
    
    
 print('Buena contrasena')

else: 
 print('Contrasena invalida')
 
repetircontrasena = input(f'Repite la contrasena: ')

if contrasena == repetircontrasena:
    print('Cuenta creada con exito')

else:
    print('Registro invalido, vuelva a intentarlo mas tarde')
