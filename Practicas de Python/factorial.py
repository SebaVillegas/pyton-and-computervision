#ejemplo para calcular el factorial de un numero con recursividad

def factorial(n):
    if n == 0 or n == 1:
        resultado = 1
    elif n<0:
        return -1
    else:
        resultado = n * factorial(n-1)
    return resultado

print(factorial(9))

#Otra forma de calcularlo sin usar recursvidad:

def otroFactorial(n):
    if n == 0 or n == 1:
        resultado = 1
    elif n<0:
        return -1
    
    resultado=1
    i=1
    while(n >= i):
        resultado = resultado * i
        i += 1
    return resultado

print(otroFactorial(9))