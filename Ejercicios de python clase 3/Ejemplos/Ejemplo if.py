import os

while True:
    print("Ingresar valor o ingrese -1 para salir")
    number=int(input("Ingrese numero: "))
    if(number > 5):
        print("Soy mayor que 5")
    elif(number == 5):
        print("Soy igual a 5")
    elif(number < 5):
        print("Soy menor que 5")
    elif(number == -1):
        print("Saliendo del programa....")
        break
    else:
        print("Dato no válido")