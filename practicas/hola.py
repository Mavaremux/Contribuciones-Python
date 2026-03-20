#Calcular promedio con registro

usuario = input(f'Ingrese su Nombre Y Apellido: ')
print(f'Bienvenido {usuario}, ingrese sus notas para calcular su promedio')

n1 = int(input(f'El total de su primera nota es: '))
n2 = int(input(f'El total de su segunda nota es: '))
n3 = int(input(f'El total de su tercera nota es: '))
n4 = int(input(f'El total de su cuarta nota es: '))

total = n1 + n2 + n3 + n4
promedio = total / 4

print(f'Su nota total es {total}')
if promedio < 10:
    print(f'El alumno {usuario} No ha aprobado')
elif promedio > 10:
    print(f'El Alumno {usuario} ha aprobado ')


