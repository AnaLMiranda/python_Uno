# Calcular el perímetro y área de un rectángulo dada su base y su altura.

base = float(input("ingrese la base"))

altura = float(input("ingrese la altura"))

perimetro = base *2 + altura *2
print(f"El perimetro es {perimetro:.1f}")

area = base * altura /2
print(f"El area es {area:.1f}")