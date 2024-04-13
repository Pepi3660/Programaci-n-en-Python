#Retornos de valores

#def potencia(base, exponente):
#    return(base**exponente)

#Usando docstring:

def potencia(base, exponente):
    """
    Funcion que calcula la potencia de dos numeros
    Argumentos:
    base -- base de la operacion
    exponente - exponente de la operacion 
    """
    return base**exponente

base = int(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente: "))

valorPotencia = potencia(base, exponente)
print("La potencia es: ", valorPotencia)