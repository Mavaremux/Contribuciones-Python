def frase(nombre,apellido,adjetivo = "Tonto"):
    return f"Hola {nombre} {apellido}, sos muy {adjetivo}"

frase_resultante = frase('Alejandro' ,'Mavares' , 'Inteligente')
print(frase_resultante)