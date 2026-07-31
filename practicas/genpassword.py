import random
import string

dischar = string.ascii_letters + string.punctuation + string.digits
lenght = int(input("Introduce la longitud de la contraseña: "))
contrasena = "".join(random.choice(dischar) for i in range(lenght) )
print(contrasena)