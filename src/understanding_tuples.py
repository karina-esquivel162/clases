"""
    TUPLAS

    Las tuplas son listas de elementos que no cambian de tamaño
    Las tuplas son listas inmutables

    Se utilizan paréntesis () para definir una tupla

    Ejemplo:

        Si tenemos un rectanuglo (largo, ancho) que siempre va
        a tener cierto tamaño, podemos asegurar que sus dimensiones
        no va cambiar si colocamos sus valores en una tupla.
(Se usan para optimizar espacio en la memoria)
"""

dimensions = (200, 50) # 200 de largo x 50 de ancho
print(dimensions)

# Vamos a imprimir elementos de una tupla
# Se realizan de la misma forma que con una
print(dimensions[0])
print(dimensions[1])

# Vamos modificar el valor de una lista
names = ["carlos", "charly", "juan", "wendy"]
print(names)
# names[0] = "mercury"
# names[1] = "mercury"
# names[2] = "mercury"
# print(names)



# dimensions[0] = 500        # Esta operación no esta permitida

# Looping through a tuple
for dimension in dimensions:
    print(dimension)

"""
    No podemos modificar una tupla,
    lo que si podemos hacer es cambiar
    la asignación de una variable que almacena
    una tupla.
"""
dimensions = (500, 1000, 20)
print("tupla re-definida:", dimensions)


"""
    MÉTODO dir() - nos muestran los métodos
print(dir(dimensions))

# Lista
dimensions_2 = [200, 50]
print(dir(dimensions_2))

# 
name = "charly"
print(dir(name))
"""

print(" ")
print("\n\tBooleanos")
# Tipos de datos booleanos
answer = True
print(answer)