#Crear una función adivinar que permita 
# adivinar un número generado en forma aleatoria
    #El número debe estar entre 0 y 100
    #Este número se genera adentro de la función
    #Además debe recibir un parámetro que sea la cantidad 
    # de intentos y en caso de que esta cantidad de 
    # intentos sea superada el programa debe terminar 
    # con un mensaje
    #Si el usuario adivina antes de superar el número de 
    # intentos máximo, se debe imprimir un mensaje con el 
    # número de intentos en los que adivinó
    #Después de crear la función, llamarla en el mismo 
    # archivo

import random

def adivinar(intentos):
    numero = random.randint(0,100)
    while intentos != 0:
        guess=int(input('Intente adivinar el numero: '))
        if numero != guess:
            print(f'Fallo! Le queda {intentos -1} intentos')
            intentos -= 1
        else:
            print('Excelente, adivino el numero correcto!')
            break
    else:
        print('No tiene mas intentos')
        print(f'El numero correcto era: {numero}')

print("Programa para adivinar un numero entre 0 y 100")
attemps=int(input('Cuantos intentos para adivinar quiere?: '))
    
while attemps <= 0:
    print('No puede ingresar un numero menor o igual a cero')
    attemps=int(input('Cuantos intentos para adivinar quiere?: '))
else:
    adivinar(attemps)

