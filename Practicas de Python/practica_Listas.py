#Crear la siguiente lista:
#   2 2 5 6
#   0 3 7 4
#   8 8 5 2
#   1 5 6 1

lista = [[2, 2, 5, 6],[0, 3, 7, 4],[8, 8, 5, 2],[1,5,6,1]]

for cols in lista:
    print(cols)
print("")

print("Seleccionar el subarray [8 8 5 2]:")
print(lista[2])
print("")

print("Poner la diagonal de la matriz en cero:")

for rows in range(len(lista)):
    for cols in range(len(lista)):
        if rows == cols:
            lista[rows][cols]= 0

for cols in lista:
    print(cols)
print("")


lista = [[2, 2, 5, 6],[0, 3, 7, 4],[8, 8, 5, 2],[1,5,6,1]]
print("Sumar todos los elementos del array:")
suma=0
for rows in range(len(lista)):
    for cols in range(len(lista)):
        suma= suma + lista[rows][cols]

print(f"La suma de todos los elementos es: {suma}")
print("")

lista = [[2, 2, 5, 6],[0, 3, 7, 4],[8, 8, 5, 2],[1,5,6,1]]

print("Setear en la matriz original los valores pares en 0 y los impares en 1:")
for rows in range(len(lista)):
    for cols in range(len(lista)):
        if lista[rows][cols] % 2 == 0:
            lista[rows][cols]=0
        else:
            lista[rows][cols]=1

for cols in lista:
    print(cols)