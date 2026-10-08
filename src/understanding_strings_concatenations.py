# Combinación o concatenación de STRING
first_name = 'karina'
last_name = "esquivel"
full_name = first_name + " " + last_name
print(full_name)

print(first_name.title() + " " + last_name.title())

message = "¡Hola, " + full_name.title() + "!"
print(message)

# WhiteSpace
"""
WhiteSpace se refiere a cualquier String
(caracter) que no se imprime, es decir,
un espacio (" "), tabuladores (\t) y
finales de linea (\n).

Los WhiteSpaces se utilizan comúnmente para organizar
las salidas de texto a usuario de tal manera que sea
más amigable de leer o ver para los usuarios.
"""

print("Python")
print("\tPython")
print("\t\tPython")
print("Lenguajes: \n\tPython \n\tC \n\tJavaScript")

# f-strings
famous_person = "jiniret"
message = f"{famous_person} una vez dijo: TABOM"
print(message)