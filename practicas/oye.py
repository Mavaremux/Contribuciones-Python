usuario = input(f'Coloque su nombre que sera visible en la plataforma(minimo 4 caracteres): ')
if len(usuario)< 4:
    print('Este usuario no es valido')
else:
    print('Buen Nombre')



contraseña = input(f'Ingrese su contraseña(debe tener minimo 8 caracteres y un numero): ')
len(contraseña)

if len(contraseña) < 8:
    print('Esta contraseña no es valida, intente de nuevo')

else:
    print(f'Su contraseña es:{contraseña}, esta seguro? Esta accion no se puede cambiar')

respuesta = input(f':')
if respuesta == 'Si':
    print('Bienvenido')

if respuesta == 'No':
    print('Intentelo mas tarde')

