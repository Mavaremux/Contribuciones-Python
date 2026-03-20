frase = input('Decime una frase maestro y te calculo cuanto tardarias si tuvieras que decirlo : ')
palabras_separadas = frase.split(" ")
cantidad_de_palabras = len(palabras_separadas)
print(f'Dijiste {cantidad_de_palabras} palabras y tardarias {cantidad_de_palabras/2} segundos en decirlas ')
print(f'Alejandro lo diria en {cantidad_de_palabras *100 //2*1.3/100} segundos')
if cantidad_de_palabras > 100:
    print('Para, no te pedi la biblia')
    
else:
    print('esta bien tus palabras hermano')
