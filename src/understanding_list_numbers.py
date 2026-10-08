# Vistas de números
"""
    Las listas también pueden almacenar números. Python
    ofrece varias herramientas que ayudan a trabajar
    eficientemente con listas de números.
"""
# Método build-in rage()
"""
    El método range() nos ayuda a crear fácilmente
    series de números.

    Ejemplo
"""
for value in range(1,5):
    print(value) # Imprimira los números del 1 al 4

# Crear una lista de números utilizando range
numbers = list(range(0,10))
print(numbers)

# Lista de números pares
even_numbers = list(range(0,11,2))
print(even_numbers)