"""
    Crear una lista con
    los primeros 10 números cuadráticos.
"""
squares = []
for value in range(0,11):
    square = value**2
    squares.append(square)
print(squares)
