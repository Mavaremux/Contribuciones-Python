#creando un conjunt con set()


conjunto = set(['Dato1' , ('datoentupla1' , 'datoentupla2')])

#metiendo un conjunto dentro de otro conjunto

conjunto1= frozenset(['dato1' , 'dato2'])
conjunto2 = {conjunto1 , 'dato3'}


#teoria de conjuntos

conjunto1 = {1,3,5,7}
conjunto2 = {2,4,8}

#verificando si es un subconjunto
resultado = conjunto1.issubset(conjunto2)

#verificando si es un superconjunto
resultado = conjunto2.issuperset(conjunto1)

#verificando si hay algun numero en comun

resultado = conjunto2.isdisjoint(conjunto1)
print(resultado)