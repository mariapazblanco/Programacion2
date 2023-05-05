#Crear un programa que utilice la estructura try - catch. El usuario debe de ingresar dos numeros y mostrar por pantalla
#el resultado de la división entre ambos numeros.

#En caso de que el divisor sea 0 utilizar la excepción ZeroDivisionError y mostrar el error por pantalla.


#INICIO

try:
    num1 = float(input("Ingrese el primer numero:"))
    num2 = float(input("Ingrese el segundo numero:"))


    resultado= num1 / num2

    print("El resultado de la division es", resultado)

except ZeroDivisionError:
    # Manejar la excepción ZeroDivisionError y mostrar un mensaje de error por pantalla
    print("Error: no se puede dividir entre cero.")


#FIN