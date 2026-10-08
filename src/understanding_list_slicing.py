players = ["charly", "juan", "iancarlo", "lisandro"]
print("lista original: ", players)

#Slicing
print(players[0:2]) # ["charly", "juan"]

# El slicing me permite trabajar con un grupo
# específico de una lista: al resultado se le conoce como
# "un slice"

print("1:4", players[1:4]) # ["juan", "iancarlo", "lisandro"]
print(":3", players[:3]) # Es como poner ceero, desde el inicio hasta la posición indicada en este caso
print("2:", players[2:]) # Toma como desde la posición dos hasta el final
print("[-3]", players[-3:]) # Va de atrás hacia adelante, tomando el último elemento como el número 1

print("\n\tCasos especiales")
# players = ["charly", "juan", "iancarlo", "lisandro"]
print(players[1:6]) # Cuando se pone un número de elemento el cuál no tenemos simpliemente lo pone hasta el final, sin SintaxError, solo funciona en slicing
print(players[6:1]) # Lista vacía, solo funciona cuando el segundo número es mayor, no cuando el primero es mayor
print(players[:0]) # Lista vacía

# Looping through a slice3
print("\n\tLooping through a silce")
students = ["charly", "juan", "iancarlo", "lisandro"]
# Slicing [::] - tarea
for student in students[2:4]:
    print(f"El estudiante {student}, va a pasar la materia.")

print(students)



# ¿Cómo podemos copiar una lista?
my_food = ["pizza", "sushi", "flautas"]                               # Ambas son la
my_friend_food = my_food  # Manera errónea de copiar una lista        # misma lista

# Tres maneras de copiar una lista
# método 1 - utilizando el método slicing
my_friend_food = my_food[:]
# Método 2 - utilizando el método de las listas .copy()
my_friend_food = my_food.copy()
# Método 3 - utilizando el método build-in list()
my_friend_food = list(my_food)
