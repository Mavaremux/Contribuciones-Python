import random

chars = "abcdefghijklmnopqrstuvwxyz1234567890!#$%^&*(*)"

password = ""

for i in range(16):
    password += random.choice(chars)
    
print(f"Your password is:{password}")


lista = list([828238372 , 293928, 2938238])
lista.append(password)
lista.pop(0)
print(lista)