#Dicionario (dicc)
#Coleccion de datos mutable, heterogenea
#con estructura de clave:valor
#Nota:Las claves no puede ser tipos de datos mutables
#Como valor podemos poner cualquier tipo de dato

mi_diccionario = {"Mesa":2300,"Lampara":98.90, "Sillas":20.99}
mi_segundo_diccionario = {(1,2,3):2000, "Cadena": 2000}

agenda ={"Eduardo": ["5445544444", "34254254"], "Mar": ["232323"]}

agenda ={"Eduardo": {"Telefono(s)": ["3232323"], "Correo": "eduardo@gmail.com"}}


print(mi_diccionario["Lampara"])
print(mi_segundo_diccionario[(1,2,3)])
elemento_eliminado = mi_diccionario.pop ("Mesa", "No se encuentra el elemento")
print(mi_diccionario)
print(elemento_eliminado)

print(agenda["Eduardo"]["Correo"])