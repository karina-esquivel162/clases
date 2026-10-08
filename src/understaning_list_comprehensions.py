"""
    Una list comprehensions combina
    el for loop y la creación de nuevos
    elementos en una sola línea y automáticamente
    agrega cada nuevo elemento a la lista, es decir,
    sin utilizar el método append.
"""
squares =[value**2 for value in range(0,11)]
print(squares)