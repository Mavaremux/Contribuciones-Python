#creando una funcion que pida un numero y devuelva los numeros primos que estan antes de llegar a esa cantidad

def es_primi(num):
    for i in range(2,num -1):
        #colocamos 2 y -1 por que todos los numeros se pueden dividir entre uno y si mismos entonces se coloca que el bucle comience desde dos y le reste uno al numero que le mandamos para que no se divida por si mismo
        if num%i == 0: return False
        #el porcentaje al dividir va a devolver el resto y por eso todo numero que de resto de 0 es por que no es primo
    return True

def primos_hasta(num):
    
    primos = []
    for i in range(3, num+1):
        resultado = es_primi(i)
        if resultado == True: primos.append(i)
    return primos
    
resultado = primos_hasta(149)
print(resultado)