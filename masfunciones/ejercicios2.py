def obtener_companeros(cantidad_de_compas):
    compas = []
    
    for i in range (cantidad_de_compas):
       nombre =  print(input('Ingresa el nombre del compa: '))
       edad = int(input('Ingresa la edad del compa'))
       
    compa = (nombre,edad)
    
    compas.append(compa)
    #ordenando de mayor a menor
    compas.sort(key=lambda x: x[1])
    
    
    #compas[x] nos devuelve una tupla con nombre y edad y despues accedemos a la edad para definir el asistente y el profesor
    
    asistente = compas[0][0]
    
    profesor = compas[0][-1]
    
    return asistente,profesor

asistente,profesor = obtener_companeros(5)
print(f'El profesor de la clase es {profesor} y su asistente es {asistente}')




    


     
        