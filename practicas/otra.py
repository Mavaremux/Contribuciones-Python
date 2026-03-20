import hashlib

encontrada = 0
input_hash = input('Contrasena hasheada: ')
pass_doc = input('INserte el diccionario: ')

try:
    pass_file = open(pass_doc , 'r')
except:
    print('Error:' + pass_doc + 'no ha sido encontrada')

for palabra in pass_file:
    palabra_cifrada = palabra.encode('utf-8')
    palabra_hasheada = hashlib.md5(palabra_cifrada.strip())
    digest = palabra_hasheada.hexdigest()
    
    if digest == input_hash:
     print('Contrasena Encontrada!!!! \n La contrasena es: ' + palabra)
    encontrada = 1
    break

if not encontrada:
    print('Contrasena no encontrada en el archivo' + pass_doc)
    

    
    