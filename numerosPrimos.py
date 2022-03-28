#Calcular y mostrar en pantalla numeros primos de forma recursiva

def esPrimo(num, n=2):
    if n >= num:
        print(num)
        return True
    elif num%n != 0:
        esPrimo(num, n+1)
    else:
        return False

def numPrimos(cant):
    for i in range(2, cant+1):
        esPrimo(i) 

print("Se calcularan n numeros primos hasta el numero que usted ingrese")
cant= int(input("Ingrese un número: "))

print(numPrimos(cant))
