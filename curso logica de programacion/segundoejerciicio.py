#Todos los operadores e imprimirlos
#Operadores Aritmeticos

print(f"Suma de 10 + 3= {10+3}")
print(f"Resta de 10 - 3 = {10-3}")  
print(f"Multiplicacion de 10 * 3 = {10*3}")  
print(f"Division de 10 / 3 = {10/3}")  
print(f"Modulo de 10 % 3 = {10%3}")  
print(f"Division entera de 10 // 3 = {10//3}")  
print(f"Resta de 10 ** 3 = {10**3}")  


#Operadores de comparacion

num1 = 10
num2 = 10
num3 = 20
sumanum = num1 + num2 
print(sumanum == num3)
print(f"Igualdad 10 es igual a 3  {10==3}")
print(f"Desigualdad 10 es distinto a 3  {10!=3}")
print(f"Mayor 10 es mayor a 3  {10>3}")
print(f"Menor 10 es menor a 3  {10<3}")
print(f"Mayor 10 es mayor o igual a 3  {10>=3}")
print(f"Menor 10 es menor o igual a 3  {10<=3}")


#Operadores Logicos AND OR NOT

print(f"AND 10+3== 13 and 4+5 == 9 es {10+3== 13 and 4+5 == 9}")
print(f"OR 10+3 == 13 or 4+5 == 9 es {11+3== 13 or 6+5 == 9}")
print(f"NOT not 10+3==13 es {not 10+3== 13}")

#Operadores de asignacion

my_number = 11
print(my_number)
my_number += 1
print(my_number)
my_number*= 4
print(my_number)
my_number/= 3
print(my_number)
my_number%= 1
print(my_number)
my_number//= 3
print(my_number)


#Operadores de identidad

my_new_number = 1 + my_number
print(f"my newnumber is my number es {my_new_number is my_number}")

#Operadores de pertenencia

print(f"La letra d esta en Alejandro es {"u" in "Alejandro"}")
print(f"La letra b no esta en Alejandro es {"b" not in "Alejandro"}")

#Estructuras de control
#Condicionales
my_string = "Alejandro"
if my_string == "Alejandro":
    print("My string es alejandro")
elif my_string== "Mavares":
    print("My string es mavares")
else:
    print("My string no es alejandro")

#Iterativas

for i in range (12):
    print (i)

i = 0
while i<= 10:
    print(i)
    i +=1

#Manejo de excepciones

try:
    resultado = 10 / 0
    print(resultado)

except:
    print("Es invalido")

finally:
    print("Termino el manejo de errores")






for number in range(10,56):
    if number % 2 == 0 and number != 16 and number % 3 != 0:

        print(number)



