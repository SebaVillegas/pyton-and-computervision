#Calcular y mostrar en pantalla los numeros primos de forma recursiva

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


        
        

        
        


            



cant= int(input("Ingrese cantidad de numeros primos a mostrar: "))

print(numPrimos(cant))