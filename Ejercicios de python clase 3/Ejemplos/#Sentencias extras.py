#Sentencias extras
#break: esta sentencia rompe la ejecucion del bucle en el momento en que se ejecute

numeros = list(range[10])
for n in numeros:
    if(n==5):
        print("Rompemos el bucle")
        break
        print(n)
    
#La secuencia de ejecución seria: 0,1,2,3,4 Rompemos el bucle!
#continue: esta instruccion permite saltarnos una iteracion 

#Iteradores: para crear un iterador usamos la instruccion iter(Objeto) y se lo asignamos a una variable. Una vez creado,
#podemos visitar los selementos del objeto.

cadena = 'Hola'
iter(cadena)