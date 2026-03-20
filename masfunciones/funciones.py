#funciones propias

#hash de clave
#funciones propias

#hash de clave
def clave_random(num):
    chars = "abcdefghij"
    num_entero = str(num)
    num = int(num_entero[0])
    c1 = num
    c2 = num * 2
    c3 = num - 4
    
    clave = f'{chars[c1]}{chars[c2]}{chars[c3]}{num*2}'
    print(f'Tu clave es {clave}')
    

clave_random(20)

