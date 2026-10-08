# Agregando elementos a una lista
motorcycles = ["honda", "mortalica", "yahama"]
print(motorcycles) # ["honda", "mortalica", "yahama"]

# Método append - agrega elementos a la lista
motorcycles.append("kawasaki")
print(motorcycles) # Agrega kawasaki a la lista

"""
    El método append ayuda a crear listas
    fácilmente de manera dinámica.
"""
motorcycles_2 = "ducati"
motorcycles_2.append(motorcycles) # 1 elemento
motorcycles_2.append("yahama") # 2 elemento
motorcycles_2.append("suzuki") # 3 elemento
print(motorcycles_2)
motorcycle = "italika"
print(motorcycles_2)
motorcycles_2.append(motorcycle)
print(motorcycles_2)

# El método insert nos ayuda a agregar elemenetos
# a una lista en un índice específico.
motorcycles_3 = ["honda", "yahama", "suzuki"]
print("\n lista original")
print(motorcycles_3)
motorcycles_3.insert(0, "ducati")
print("\n lista despues del método insert")
print(motorcycles_3)


# Método .pop() Elimina el último elemento de una lista,
# pero nos permite utilizar el elemento después de eliminarlo.
print("\n\t Aquí aprendí a utilizar el método .pop()")
motorcycles_4 = ["honda", 'suzuki', 'hd', 'mortalica']
print(motorcycles_4)
# motorcycles_4.pop() # Eliminará 'mortalica'
# print(motorcycles_4)

# Mostrará la moto borrada
deleted_motorcycle = motorcycles_4.pop()
print(f"Tu motocicleta borrada es: {deleted_motorcycle}")  # f"-" es para concatenar 'Tu motocicleta...' y que no marque error
print(motorcycles_4)

# Se puede utilizar tambien para eliminar un elemento específico.
motorcycles_5 = ["honda", 'suzuki', 'hd', 'mortalica']
print(motorcycles_5)
motorcycles_5.pop(0)
print(motorcycles_5) # Lista sin honda

# Método .remove(), permite borrar elementos por su valor.
print("\n\t Aqui aprendí a usar el método .remove()")
motorcycles_6 = ["honda", 'yahama', 'suzuki', 'ducati']
print(motorcycles_6)
motorcycles_6.remove('yahama') # Borra yahama de la lista
print(motorcycles_6)

# Ordenar listas
cars = ['bwm','audi', 'toyota', 'subaru']
print(cars)
cars.sort() # Ordenar la lista de manera permanente
# Argumento opcional de sort es el (reverse=True)
print(cars)

several_items = [["meimei", "arnoldo"], ["subaru", "tsuru"]]
print(several_items[1][1])