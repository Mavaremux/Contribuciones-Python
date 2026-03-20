print("CALCULADORA")

try:
    print(20/5)


    list2 = [1,2,3,4,5,6,7]
    print(list2[9])
except Exception as e:

    print(f" Ha sucedido un error inesperado {e}")




def motopros(parameters: list):
    if len(parameters) < 2:
        raise IndexError
    elif parameters[1] == 0:
        raise ZeroDivisionError
    
    print(parameters[2])
    print(parameters[0] / parameters[2])

try:
    motopros([24 ,20,"kk" ,  1])

except IndexError as e:
        print("Ha ocurrido un error. Los parametros deben tener mas de dos elementos")

except ZeroDivisionError as e:
    print("Ha ocurrido un error, no se puede dividir por 0")

except Exception:
    print("Ha ocurrido un error inesperado")

else:
    print(" No se ha prdoucido ningun error")

finally:
    print("El programa finaliza")