import cv2
import numpy as np
import sys
drawing = False #True if mouse is pressed
comprueba_recorte = False #con esta variable se habilita la funcion de 'restaurar'
ix, iy = -1, -1
fx, fy = -1, -1

def seleccionar(event, x, y, flags, param):
    global ix, iy, fx, fy, img, drawing
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y #guarda la coordenadas donde se habilita el evento
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing is True:
            img = cv2.imread(filename) #se lee la imagen original para que no se pinten rectangulos constantemente
            cv2.rectangle(img, (ix, iy), (x, y), (0, 0, 255), 1) 
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        fx, fy = x, y
    

def guardar_recorte():
    global ix, iy, fx, fy, drawing, img, img_c
    img = np.copy(img_c)
    if ix > fx:         # Se verifica que las coordenadas finales sean mayores que las iniciales
        aux = ix        # En caso contrario, se intercambian
        ix = fx         # Se ejecuta en caso de empezar a dibujar el rectángulo desde abajo o desde la derecha
        fx = aux
    if iy > fy:
        aux = iy
        iy = fy
        fy = aux
        
    rec = np.zeros((fy-iy, fx-ix, 3), np.uint8) #creeo una matriz negra con las dimensiones del recorte seleccionado
    
    for i in range(fy-iy): #recorro filas
        for j in range(fx-ix): #recorro columnas
            rec[i,j]=img[iy+i][ix+j] #voy asignado apartir de la matriz inicial los valor de la imagen original y los guardo
                                    #en la matriz recortada. Me voy desplazando a medida que itero
            
    cv2.imwrite('resultado.png', rec) #creo el archivo resultado.png apartir de lo obtenido en rec
    cv2.imshow('recorte', rec) #muestro el resultado
    

if(len(sys.argv) > 1): #se fija en elemento [1] de argv. ese es el nombre del archivo a procesar. el elemento [0] es el nombre del programa
    filename= sys.argv[1] #guarda en la variable filename el nombre del video
else:
    print("Pass a filename as first argument") #hay que pasarle un archivo como argumento
    sys.exit(0) #sale del programa
    
img = cv2.imread(filename, cv2.IMREAD_COLOR)
img_c=np.copy(img)

cv2.namedWindow('image')
cv2.setMouseCallback('image', seleccionar)

print("Manteniendo el mouse apretado seleccione una porcion de la imagen a recortar")

print("\nCon la letra \'g\' guarda el recorte seleccionado")
print("Con la letra \'r\' restaura la imagen original")
print("Con la letra \'q\' finaliza la ejecucion del programa")


while(1):
    cv2.imshow('image', img)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('g'):
        if ix == -1 and iy == -1 and fx == -1 and fy == -1:
            print("\nSe debe seleccionar una porcion de la imagen primero")
        else:
            guardar_recorte()
            comprueba_recorte = True
    elif k == ord('r'):
        if comprueba_recorte is True:
            cv2.destroyWindow('recorte') 
            comprueba_recorte = False
        else:  
            print("\nSe debe guardar un recorte primero")                 
    elif k == ord('q'):         
        break 
    
cv2.destroyAllWindows()
