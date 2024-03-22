#librerias
import os

#Definicion de funcion ingresar_numeros
def ingresar_numeros():
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))
    return num1, num2

#Preguntamos al usuario que operacion desea realizar
while True:
    print("\n\t\tMENU DE OPCIONES: \n")
    print("\t\t1. Suma")
    print("\t\t2. Resta")
    print("\t\t3. Multiplicación")
    print("\t\t4. División")
    print("\t\t5. Salir")

    opcion_str = input("\n\t\tOpción: ")
    opcion = int(opcion_str)

    os.system('cls')

    if opcion == 1:
        num1,num2 = ingresar_numeros()
        print("\n\t\tLa suma de ", num1,"+",num2, "=", num1+num2)
    elif opcion == 2:
        num1,num2 = ingresar_numeros()
        print("\n\t\tLa resta de ", num1, "-",num2, "=", num1-num2)
    elif opcion == 3:
        num1,num2 = ingresar_numeros()
        print("\n\t\tEl producto de ", num1,"*",num2, "=", num1*num2)
    elif opcion == 4:
        num1,num2 = ingresar_numeros()
        if num2 != 0:
            print("\n\t\tEl cociente de ", num1,"/", num2, "=", num1/num2)
        else:
            print("\n\t\tERROR: No se puede hacer division entre 0\n")
    elif opcion == 5:
        print("\n\n\t\tHASTA LUEGO!!\n\n")
        break
    else:
        print("\n\t\tERROR: OPCIÓN NO VALIDA")
    
    input("Presiona Enter para continuar...")
    os.system('cls')