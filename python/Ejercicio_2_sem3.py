#Crea una lista e inicializarla con 5 cadenas de caracteres leídas por teclado. Copia los elementos de la lista en otra lista pero en orden inverso, y muestra sus elementos por la pantalla.

lista_cadenas = []
for i in range(5):
    cadena = input("Ingresa una cadena: ")
    lista_cadenas.append(cadena)
print(f"La lista es: {lista_cadenas}")
#Copia los elementos de la lista en otra lista pero en orden inverso, y muestra sus elementos por la pantalla.
lista_invertida = lista_cadenas[ : : -1]
print(f"La lista invertida es: {lista_invertida}")