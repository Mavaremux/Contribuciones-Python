#recorriendo la lista animales


animales = ['Perro','gato','loro','Cocodrilo']

for animal in animales:

    print(f'Ahora la variable animal es igual a {animal}')
    



#recorriendo la lista numeros y multiplicandolos por 10    
numeros = [57 , 8 , 9 , 20]
for numero in numeros:
     resultado = numero *10
     print(resultado)
        
    
for numero,animale in zip(numeros,animales):
    print(f'Recorriendo lista 1:{animale}')
    print(f'Recorriendo lista 2:{numero}')
    

#forma no optima de recorrer una lista
for num in range(len(numeros)):
    print(numeros[num])
    
    
#forma optim de recorrer una lista

for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    
    print(f'el indice es:{indice} y el valor es {valor}')
    
#usando el else

for numero in numeros:
    print(f'Ejecutando el ultimo bucle, el valor actual es {numero}')
else:
    print('El bucle termino')