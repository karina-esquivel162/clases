# if statement
print("\n\tEjemplo de if")
cars = ["audi", "bwm", "subaru", "toyota"]
for car in cars:
    if car == "audi":
        print(car.upper())
    else:
        print(car)

print("\n\tCondicional del if")
# El condicional o condition
# El condicional es el corazón del if

# Condicional Verdadero
# Condicional True
truck = "ford"         # '=' asignación a la variable
print(truck == "ford") # '==' pregunta si es igual y responde verdadero o falso

# Condicional Falso
# Conditional False
print(truck == "audi")

# Distingue mayúsculas y minusculas
print(truck == "Ford".lower())

# Condicional de desigualdad !=
print(truck!="audi")     # Pregunta si lo que está dentro de truck es diferente o no es igual a audi, en este caso es True porque no es igual
print(truck!="ford")     # truck si trae ford por lo cual es false


# Comparaciones númericas
print("\n\tComparaciónes númericas")
age = 34
print(age==34) # True

answer = 17
if answer != 42:
    print("esa no es la respuesta correcta")
    
# conector menor que <
print("\n\tConectores <, >, <=, >=")
age = 19
print(age < 21) # True
print(age <= 21) # '<=' Menor o igual a 21 # True
print(age > 21) # False
print(age >= 21) # '>=' Mayor o igual a 21 # False


# Múltiple conditions
age_0 = 22
age_1 = 18
print("\n\tMultiple Conditions")
print("\n\toperación AND")
print(" ")
print(age_0>=21 and age_1 >= 21) # False
print(age_0>=21 and age_1 >= 18) # True

print("\n\tOperación OR")
print(age_0>=21 or age_1 >= 21) # True
print(age_0>=23 or age_1 >= 21) # False

print("\n\tIN")
# Cómo saber si un elemento está en una lista
food = ["cilaquiles", "flautas", "gorditas", "tamales"]
print("¿Nopales está en la lista?")
print("nopales" in food)
print("\n¿Gorditas está en la lista?")
print("gorditas" in food)

# Cómo saber si un elemento NO está en una lista?
banned_user = ["andrew", "carolina", "david"]
user = 'marie'
print(user not in banned_user) # True