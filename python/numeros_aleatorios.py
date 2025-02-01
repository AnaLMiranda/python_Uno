#Importamos todo el modulo de numeros aleatorios llamado random
import random

lista_numeros_aleatorios = []
 
for i in range(10):
    # randint (1,10) genera un numero aleatorio entre 1 y 10
    numero_aleatorio = random.randint(1,10)
    lista_numeros_aleatorios.append(numero_aleatorio)
print(lista_numeros_aleatorios)

for numero in lista_numeros_aleatorios:
        print(f"El número es: {numero}, el cuadrado es: {numero ** 2}, el cubo es: {numero **3}")
