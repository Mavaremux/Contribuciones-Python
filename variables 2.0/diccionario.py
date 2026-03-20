#creando diccionarios con dict()
diccionario = dict(nombre = 'Lucas', apellido = 'Dalto')

#las listas n pueden ser claves y usamos frozenset para meter conjuntos

diccionario = {frozenset(['dalto','rancio' ]): 'jasjas'}


#creando diccionarios con fromkeys()

diccionario = dict.fromkeys(['nombre','apellido'],'nose')
print(diccionario)
