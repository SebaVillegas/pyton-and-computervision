import cv2              #Importamos libreria para leer imagen, obtener tamaño, transformarla y mostrarla
import numpy as np      #Importamos libreria para funciones trigonometricas y arreglos

def transf_afin(img, puntos_orig, puntos_transf):

    (h, w, d) = img.shape   #Obtenemos el tamaño

    M = cv2.getAffineTransform(puntos_orig, puntos_transf)

    img_transf = cv2.warpAffine(img, M, (w, h))     #Aplicamos la transformacion

    return img_transf   #Devolvemos la imagen transformada

img = cv2.imread("messi.png")   #Cargamos la imagen
(h, w, d) = img.shape   #Obtenemos el tamaño

#En particular para este práctico, se decidió arbitrariamente aplicar un espejado horizontal y vertical

puntos_orig = np.float32([[0,0], [w-1,0], [0,h-1]]) #Se eligen como puntos originales la esquina superior izquierda, la esquina superior derecha y la esquina inferior izquierda
puntos_transf = np.float32([[w-1,h-1], [0,h-1], [w-1,0]]) #Al realizar un espejado tanto vertical como horizontal, 
                                                        # el punto correspondiente a la esquina superior izquierda, es la esquina inferior derecha; 
                                                        # las otras 2 esquinas se intercambian entre sí

imagen = transf_afin(img, puntos_orig, puntos_transf)
print("hola")
cv2.imshow("Imagen transformada", imagen)   #Mostramos la imagen transformada
cv2.waitKey(5000)       #Esperamos 5 segundos

cv2.destroyAllWindows()     #Cerramos todas las ventanas abiertas
