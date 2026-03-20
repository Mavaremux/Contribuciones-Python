usuario = input(f'Ingrese su nombre de usuario( Minimo 5 caracteres)')
if len(usuario)> 5:
   contrase = input(f'Usuario valido, ingrese su contrase;a (Minimo 5 caracteres y un numero): ')
else:
    print('Usuario invalido, ingrese un usuario valido')

if len(contrase)< 5:
    print('Clave invaida, intentelo de nuevo')
numeros = (1234567890)

if numeros  in contrase:
        print('Clave Valida, bienvenido al sistema')
else:
        print('Clave invalida, intentelo de nuevo')
        


