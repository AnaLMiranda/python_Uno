# Obtener la cantidad de elementos mayores a 5 en la tupla.

numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

mayores_a_5 = sum(1 for numero in numeros if numero > 5)

# resultado
print(f"La cantidad de elementos mayores a 5 es: {mayores_a_5}")
