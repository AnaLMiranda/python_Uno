#Escribe un programa Python que pida un número por teclado y que cree un diccionario cuyas
#claves sean desde el número 1 hasta el número indicado, y los valores sean los cuadrados de las claves.

numero = int(input("Introduce un número: "))

# Creamos un diccionario donde las claves son los números del 1 al 'numero'
# y los valores son los cuadrados de esas claves.
diccionario = {i: i**2 for i in range(1, numero + 1)}

# Mostramos el diccionario resultante
print("Diccionario:", diccionario)