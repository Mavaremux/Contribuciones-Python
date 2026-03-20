frutas = ('banana' , 'manzana' , 'pera' , 'naranja' , 'granada')


print("VENTA DE FRUTAS")
for fruta in frutas:
    print(f"se vende {fruta}")
    #evitando que se coma una manzana con la sentencia continue
    if fruta == 'manzana':
        print("La manzana no esta en stock,lo siento")
        continue


        

       
   
stock= (len(frutas)) 
print (f"FIN DE LA VENTA, el stock vendido fue de {stock} variedades de frutas")