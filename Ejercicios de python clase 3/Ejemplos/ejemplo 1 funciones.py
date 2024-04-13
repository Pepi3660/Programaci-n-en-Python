def area_triangulos(base,alutra):
    area = (base * altura)/2
    return area

base = int(input("Ingrese la base: "))
altura = int(input("Ingrese la altura: "))

area= area_triangulos(base,altura)
print("El area es: ", area)