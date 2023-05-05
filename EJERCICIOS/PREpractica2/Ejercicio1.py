#Crear un programa que permita ingresar una lista de numeros al usuario y muestre por pantalla el maximo entre ambos numeros.

#Nota : Hacerlo con la función max(a,b) y luego con una comparación

#INICIO

#con funcion max
numeros= input("Ingrese una lista de numeros")
numeros=list(map(int, numeros.split()))
maximo=max(numeros)
print("El numero maximo en la lista es", maximo)

numeros= input("Ingrese una lista de numeros")
numeros = list(map(int, numeros.split())) #Convertir la entrada del usuario en una lista de números enteros
maximo=numeros[0]
for numeros in numeros:
    if numeros>maximo:
        maximo=numeros
print("El numero maximo de la lista es:", maximo)




#FIN