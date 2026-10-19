"""
    Realizar un programa que determine el costo
    de un boleto a partir de las siguientes condiciones:

    - costo para una persona menor o igual a 4 años: gratis
    - costo para una persona cuya edad es mayor a 4
        años pero menor a 18: $200
    - costo para una persona cuya edad es mayor a 18: $500
"""

age = input(" Ingresa tu edad: ")
# print(type(age)) # String
age = int(age)
print(type(age)) # int

print("\n\tEsto se realiza con el if normal")
if age <= 4:
    cost = 0

if age > 4 and age < 18:
    cost = 200

if age >= 18 and age < 65:
    cost =  500

if age >= 65:
    cost = 0

print(f"El costo de tu boleto es: ${cost}")

# if-elif-else
print("\n\tEsto se realiza con elbloque if-elif-else")

if age <= 4:
    cost = 0
elif age > 4 and age <= 18:
    cost = 200
elif age >= 18 and age < 65:
    cost = 500
elif age >= 65:
    cost = 0
# else:
#    cost = 0
# Cuando el if-elif contempla todas las opciónes el else esta de más

print(f"Tu entrada cuesta: ${cost}")