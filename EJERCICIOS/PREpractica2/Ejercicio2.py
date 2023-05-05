#Crear un programa que permita al usuario ingresar una lista de numeros. De esa lista de numeros almacenar en otra lista los numeros impares.

#El programa debe de mostrar por pantalla la lista de numeros originales y la lista de numeros impares.

#INICIO

numeros= input("Ingrese una lista de numeros separados por espacio")
numeros = list(map(int, numeros.split()))
numeros_impares=[]
for numeros in numeros:
    if numeros % 2 != 0:
        numeros_impares.append(numeros)
print("La lista original es:", numeros)
print("La lista de numeros impares es:", numeros_impares)

#FIN