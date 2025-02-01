#1.-Almacenar en una coleccion los nombres de 10 productos
#Usamos una lista para almacenar los datos ya que posteriormente se eliminan datos
#2.-Usar un metodo para eliminar el ultimo producto
#3.-Usar un metodo para agregar dos productos nuevos
#4.- Eliminar todos los productos repetidos

productos = ["Refrescos", "Piñatas", "Globos", "Confeti", "Vasos", "Sillas", "Mesas", "Lonas", "Bebidas", 
"Platos" ]
print(f"La lista de productos es: {productos}")

#para eliminar el ultimo producto en una lista es con el metodo .pop()

#sin argumentos para que sea el ultimo elemento
productos.pop()
print(productos)

#Usar un metod para agregar dos uevso productos
#Como es una lista usamos el metodo .append() dos veces

productos.append("Piñatas")
productos.append("Comida")
print(f"La lista de productos despues de agragar {productos}")

#Eliminar los elementos repetidos
#Convertimos la lista a conjunto ya que los conjuntos no permiten valores repetidos

productos =set(productos)
print(f"conjunto {productos}")
productos = list(productos)

#para ordenar alfabeticamente
productos.sort()
print(f"Lista sin repetir ordenada: ")


