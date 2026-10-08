# Enteros
# Sumar +
# Restar -
# Multiplicar *
## Dividir /
## Division entera //
# Potencias **n
print(3**2) # 3^2
print(3**3) #3^3
print(10**6) #10^6
print(10%3) ##Módulo (mod)
age = 15
print(age)
name = "meimei"
print(name, age)
# name es tipo string porque son letras y age del tipo entero (int) porque se iguala a un número
#Floats (números con punto decimal)
"""
Python llama floats a cualquier número con punto
decimal.
"""

print(0.1+0.1)
print(0.2-0.2)
print(2*0.1)
print(2*0.2)

# Imprimir la edad de alguien
age = 18 #Variable de tipo Int
# message = "meimei tiene" + age + "años" ¡No se puede concatenar números y letras al mismo tiempo!
"""
TypeError: Python no puede reconocer el tipo de información que se está utilizando.
Se nescesita un Built-int "str()" - string
"""
message = "meimei tiene" + " " + str(age) + " " + "años"
print(message)
message_f = f"meimei tiene {age} años." # mejor utilizar este para no tener que poner str()
print(message_f)

print(type(age)) # Tipo de variable utilizada dentro de los parentesis de type
print(type(0.1))
print(type(message_f))
print(type(message_f), type(1+5), type(2+0.5))