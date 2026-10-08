# Let´s try to use variable
message = "this is my first program :), i´m verr¿y happy"
another_message = "Really, so so happy"

# build-in methods
print(message)
print(another_message)

print(message, another_message)
print(another_message, message)

message = "hi boys and girls"
print(message)

"""
    Reglas de python para nombrar variables
    los nombres de variables deben nombrarse solo con:

    -letras, números y guión bajo.
    -deben comenzar con una letra o guión bajo.
    -no utilizar espacios para separar palabras en variables(-)
    -no utilizar palabras reservadas en python o el nombre del archivo como nombre de variables.
    -los nombres...
    -en python se usa lower case para nombrar variables
    ejemplo:
    correcto: message_1, _message_1
    incorrecto: 1_message
"""

message = "hola amigo python"
print(message)

"""
    Traceback (most recent call last):
        File "C:\Users\Alumno\projects\programming_methodologies\src\understandin_variables.py"
            print(mesage)
                ^^^^
    NameError: name 'message' is not defined. Did you mean: 'message'?


    NameError: Ocurre cuando olvidamos definir
    el valor de una variable antes de utilizarla o
    cometimos un error (de ortografía) al ingresar
    el nombre de la variable.
"""