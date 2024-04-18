import os

from inventario import Inventario
from producto import Producto

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

inventario = Inventario()

while True:
    print("\n\t\t\tMENU\n")
    print("\t\t1. Agregar producto")
    print("\t\t2. Actualizar cantidad de producto")
    print("\t\t3. Eliminar producto")
    print("\t\t4. Mostrar productos")
    print("\t\t5. Salir")
    opcion_str = input("\n\tIngrese opción: ")

    try:
        opcion = int(opcion_str)
    except ValueError:
        opcion = 0

    if opcion not in range(1,6):
        print("\n\t\tERROR: Opcion incorrecta, intente nuevamente\n")
        print("\t\tPresione enter para continuar...\n\n")
        continue

    clear_screen()

    if opcion == 1:
        nombre = input("\n\t\tIngrese el nombre del producto: ")
        cantidad = int(input("\n\t\tIngrese la cantidad del producto: "))
        precio = float(input("\n\t\tIngrese el precio del producto: "))
        producto = Producto(nombre, cantidad, precio)
        inventario.add_productos(producto)
        input("\n\t\tPresione enter para continuar...\n\n")
    elif opcion == 2:
        nombre = input("\n\t\tIngrese el nombre del producto a actualizar: ")
        nueva_cantidad = int(input("\n\t\tIngrese la nueva cantidad: "))
        inventario.backup(nombre, nueva_cantidad)
        input("\n\t\tPresione enter para continuar...\n\n")
        clear_screen()
    elif opcion == 3:
        nombre = input("\n\t\tIngrese el nombre del producto a eliminar: ")
        inventario.delete(nombre)
        input("\n\t\tPresione enter para continuar...\n\n")
        clear_screen()
    elif opcion == 4:
        inventario.show()
        input("\n\t\tPresione enter para continuar...\n\n")
    elif opcion == 5:
        print("\n\t\tSaliendo del programa...\n\n")
        input("\n\t\tPresione enter para continuar...\n\n")
        break
    else:
        print("\n\t\tOpción no válida. Por favor, seleccione una opción válida.")
        input("\n\t\tPresione enter para continuar...\n\n")