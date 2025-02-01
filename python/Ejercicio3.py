#Vamos a crear un programa en Python donde vamos a declarar un diccionario para guardar los precios de las distintas frutas. 
# El programa pedirá el nombre de la fruta y la cantidad que se ha vendido y nos mostrará el precio final de la fruta
#  a partir de los datos guardados en el diccionario. 
# Si la fruta no existe nos dará un error. Tras cada consulta el programa nos preguntará si queremos hacer otra consulta.


numero = int(input("Introduce un número: "))

# Creamos un diccionario donde con números del 1 al 'numero'

diccionario = {i: i**2 for i in range(1, numero + 1)}

print("Diccionario:", diccionario)

precios_frutas = {
    'manzana': 2.5,
    'plátano': 1.8,
    'naranja': 3.0,
    'pera': 2.2,
    'uva': 4.0
}


def consultar_precio():
    
    fruta = input("Introduce el nombre de la fruta: ").lower()  # Convertimos a minúsculas para evitar errores
  
    if fruta in precios_frutas:
       
        cantidad = float(input(f"Introduce la cantidad de {fruta} vendida: "))
        
        precio_total = precios_frutas[fruta] * cantidad
        print(f"El precio final de {cantidad} {fruta}(s) es: {precio_total}€")
    else:
        print("Error: La fruta no está en el diccionario de precios.")

# Ciclo 
while True:
    consultar_precio() 
    otra_consulta = input("¿Quieres hacer otra consulta? (sí/no): ").lower()
    if otra_consulta != 'sí':
        print("Gracias por usar el programa. ¡Hasta luego!")
        break