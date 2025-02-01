#Realice un programa que pregunte aleatoriamente una multiplicación. El programa debe indicar si 
#la respuesta ha sido correcta o no (en caso que la respuesta sea incorrecta el programa debe indicar cuál es la correcta).
#El programa preguntará 10 multiplicaciones, y al finalizar mostrará el número de aciertos.


import random

# Inicializar contador de aciertos
aciertos = 0

# Ciclo para realizar 10 multiplicaciones
for i in range(10):
    # Generar dos números aleatorios entre 1 y 10
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    
    # Calcular el resultado correcto de la multiplicación
    resultado_correcto = num1 * num2
    
    # Preguntar al usuario el resultado de la multiplicación
    print(f"Pregunta {i + 1}: ¿Cuánto es {num1} x {num2}?")
    respuesta_usuario = int(input("Tu respuesta: "))
    
    # Verificar si la respuesta es correcta
    if respuesta_usuario == resultado_correcto:
        print("¡Correcto!")
        aciertos += 1
    else:
        print(f"Incorrecto. La respuesta correcta es {resultado_correcto}.")
    print()  # Línea en blanco para claridad

# Mostrar el número total de aciertos al final
print(f"Has acertado {aciertos} de 10 multiplicaciones.")









# Obtener el cuadrado de todos los elementos en la lista.

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Calcular el cuadrado de cada número 
cuadrados = [numero**2 for numero in numeros]

print("Lista original:", numeros)
print("Cuadrados de los elementos:", cuadrados)








 Obtener la cantidad de elementos mayores a 5 en la tupla.

numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

mayores_a_5 = sum(1 for numero in numeros if numero > 5)

# resultado
print(f"La cantidad de elementos mayores a 5 es: {mayores_a_5}")






# Obtener la suma de todos los elementos en la lista.

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Calcular la suma de los elementos
suma_total = sum(numeros)

# Mostrar el resultado
print(f"La suma de todos los elementos en la lista es: {suma_total}")