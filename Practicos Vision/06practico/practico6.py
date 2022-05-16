import cv2
import numpy as np
import math
import sys

drawing = False  # True if mouse is pressed
comprueba_recorte = False  # para habilitar la funcion de 'restaurar'
ix, iy = -1, -1
fx, fy = -1, -1


def seleccionar(event, x, y, flags, param):
    '''Esta funcion es la que permite dibujar
        un rectangulo sobre la imagen'''
    global ix, iy, fx, fy, img, drawing
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y  # guarda la coordenadas donde se habilita el evento
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing is True:
            # se lee la imagen original para que no se pinten
            # rectangulos constantemente
            img = cv2.imread(filename)
            cv2.rectangle(img, (ix, iy), (x, y), (0, 0, 255), 1)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        fx, fy = x, y


def guardar_recorte():
    global ix, iy, fx, fy, drawing, img, img_c
    img = np.copy(img_c)
# Se verifica que las coordenadas finales sean mayores que las iniciales
# Se ejecuta en caso de empezar a dibujar el rectángulo
# desde abajo o desde la derecha
    if ix > fx:
        aux = ix
        ix = fx
        fx = aux
    if iy > fy:
        aux = iy
        iy = fy
        fy = aux

    rec = np.zeros((fy-iy, fx-ix, 3), np.uint8)
# creeo una matriz negra con las dimensiones del recorte seleccionado
# voy asignado apartir de la matriz inicial los valor de la
# imagen original y los guardo
# en la matriz recortada. Me voy desplazando a medida que itero
    for i in range(fy - iy):  # recorro filas
        for j in range(fx - ix):  # recorro columnas
            rec[i, j] = img[iy + i][ix + j]

    cv2.imwrite('recorte.png', rec)
    cv2.imshow('recorte', rec)  # muestro el resultado
    cv2.waitKey(1000)
    cv2.destroyWindow('recorte')
    return rec


def transformada_euclidiana(angle=0, tx=0, ty=0, s=1):

    img = cv2.imread('recorte.png')  # Cargamos el recorte de imagen

    (h, w) = img.shape[:2]  # Obtenemos el ancho y largo de la imagen

    M = np.float32([[s * math.cos(angle), s * math.sin(angle), tx],
                    [-s * math.sin(angle), s * math.cos(angle), ty]])

    img_transf = cv2.warpAffine(img, M, (w, h))  # Aplicamos la transformacion

    cv2.imwrite('resultado.png', img_transf)
    cv2.imshow('rtransformacion', img_transf)  # muestro el resultado

    return img_transf


# se fija en elemento [1] de argv. ese es el nombre del
# archivo a procesar.el elemento[0] es el nombre del programa
if(len(sys.argv) > 1):
    filename = sys.argv[1]  # guarda el nombre del archivo
else:
    print("Pass a filename as first argument")
    sys.exit(0)  # sale del programa

img = cv2.imread(filename, cv2.IMREAD_COLOR)
img_c = np.copy(img)

cv2.namedWindow('image')
cv2.setMouseCallback('image', seleccionar)

print("Manteniendo el mouse apretado seleccione una porcion de la imagen a recortar")
print("\nCon la letra \'g\' guarda el recorte seleccionado")
print("\nCon la letra \'e\' aplica transformacion euclediana al recorte previamente seleccionado")
print("Con la letra \'q\' finaliza la ejecucion del programa")


while(1):
    cv2.imshow('image', img)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('g'):
        if ix == -1 and iy == -1 and fx == -1 and fy == -1:
            print("\nSe debe seleccionar una porcion de la imagen primero")
        else:
            img_recortada = guardar_recorte()
            print("\nPresione \'e\' para aplicar una transformacion.")
            comprueba_recorte = True
    elif k == ord('e'):
        if comprueba_recorte is False:
            print("\nSe debe  guardar una porcion de la imagen primero")
        else:
            sys.stdout.flush()  # limpia el buffer de entrada por las dudas che

            tx = int(input("Seleccione traslacion en x: "))  # Traslacion en x
            ty = int(input("Seleccione traslacion en y: "))  # Traslacion en y
            angle = int(input("Seleccione el angulo de traslacion: "))
            angle = angle*np.pi/180
            s = float(input("Seleccione la escala: "))  # escalado

            img_trans = transformada_euclidiana(angle, tx, ty, s)

            print('Se realizo existosamente la transformacion')
            print("Presione \'q\' para finalizar o realice una nueva transformacion")
    elif k == ord('q'):
        break

cv2.destroyAllWindows()
