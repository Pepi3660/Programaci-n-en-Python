import math

def perimetro(radio):
    return 2*math.pi*radio

def area(radio):
    return math.pi * radio**2


radio = float(input("Ingrese el radio: "))
P = perimetro(radio)
A = area(radio)

print("El perimetro de la circunferencia es: ", P)
print("El area de la circunferencia es: ", A)