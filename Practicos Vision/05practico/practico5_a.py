import cv2              #Importamos libreria para leer imagen, obtener tamaño, transformarla y mostrarla
import numpy as np      #Importamos libreria para funciones trigonometricas y arreglos
import sys

def transformada_euclidiana(angle = 0, tx = 0, ty = 0):   #Rotación y traslacion a aplicar ; valores por defecto 0

    M = np.float32([ [np.cos(angle), np.sin(angle), tx], [-np.sin(angle), np.cos(angle), ty] ])  #Calculamos parte de la matriz H

    img = cv2.imread(filename)   #Cargamos la imagen
    
    #print(M[0,0],M[0,1])

    (h, w) = img.shape[:2]   #Obtenemos el ancho y largo de la imagen
    
    img_transf = cv2.warpAffine(img, M, (w, h))     #Aplicamos la transformacion
    
    return img_transf   #Devolvemos la imagen transformada

if(len(sys.argv) > 1): #se fija en elemento [1] de argv. ese es el nombre del archivo a procesar. el elemento [0] es el nombre del programa
    filename= sys.argv[1] #guarda en la variable filename el nombre de la imagen
else:
    print("Pass a filename as first argument") #hay que pasarle un archivo como argumento
    sys.exit(0) #sale del programa

tx = int(input("Seleccione traslacion en x: "))    #Traslacion en x
ty = int(input("Seleccione traslacion en y: "))    #Traslacion en y
angle = int(input("Seleccione el angulo de traslacion: "))
angle = angle*np.pi/180                             #Ángulo de rotación

imagen = transformada_euclidiana(angle, tx, ty)

cv2.imshow("Imagen transformada", imagen)   #Mostramos la imagen transformada
cv2.waitKey(0)      

cv2.destroyAllWindows()
