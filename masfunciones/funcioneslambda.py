#creando funcion lambda para saber si el numero es par o no
numeros = [ 1, 2 , 3 , 4 ,5 ,6,7,8,9,10,11,12,13]
numeros_pares = filter(lambda numero:numero % 2 == 0, numeros)



print(list( numeros_pares))