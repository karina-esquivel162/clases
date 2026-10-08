# Trabajo con listas
print("\n\tel día de hoy voy a aprender a trabajar con listas".upper())
# vamos a crear una lista de puros strings con nombres de magos
magicians = ['harry', 'ron', 'hermione', 'snape']
print(magicians)

print(magicians[0], magicians[1], magicians[2], magicians[3])

print("\n\tcliclo for".upper())
for magician in magicians:
        print(magician)

# Imprime cada mago 
# A esto se le conoce como looping

# for dog in dogs
# for cat in cats
# for item in items

# Argumento para quitar el salto de línea que tiene automaticamente el print()
# print(magicians, end= " ")

# Ahora vamos a imprimir un mensaje para cada mago
for magician in magicians:
        print(f"{magician.title()}: ¿Han visto una rana? La perdió un niño llamado nabel.")
        print(f"Oh, estas haciendo magea, continúa. {magician.upper()}\n") 
        print("Gran espectaculo")

# Identación
"""
        Python utiliza la identación para determinar
        cuando una línea de código está conectada a la
        línea de código anterior.

        Básicamente, se utilizan 4 espacios en blanco para
        obligarnos a escribir un código ordenado y estructurado.
"""
# No olvidemos identar
magicians = ["alice", "david", "caroline"]
# for magician in magicianss:
# print(magician) Identation error

# Error de lógica - Logic Error - IdentationError
for magician in magicians:
        print(magician)
print(f"No puedo esperar a ver el siguiente truco,{magician}") # Este print debería tener identación para que se repita con el ciclo for

# Identación innecesaria
message = "Hello world python!"
#        print(message)

# No olvidar los dos puntos - Syntax Error
#for magician in magicians
#        print(magician)