import cv2
import numpy as np

points = []


def draw_points(event, x, y, flags, param):
    global points, img, img_aux

    if event == cv2.EVENT_LBUTTONDOWN:
        if len(points) < 3:
            points.append([x, y])
        else:
            points.clear()
            points.append([x, y])
            img = img_aux.copy()
    elif event == cv2.EVENT_LBUTTONUP:
        cv2.circle(img, (x, y), 5, (0, 0, 255), 2)


def insertar(img, imgx, pt2):
    # Hago transformacion en imgx
    cols, rows, ch = imgx.shape
    pt1 = np.float32([[0, 0], [rows - 1, 0], [0, cols - 1]])
    pt2 = np.float32(pt2)

    M = cv2.getAffineTransform(pt1, pt2)
    imga = cv2.warpAffine(imgx, M, (rows, cols))

    # Hago un hueco en img
    mascara = np.array([pt2[1], pt2[0], pt2[2],
                        pt2[2] + pt2[1] - pt2[0]], np.int32)

    cv2.fillPoly(img, [mascara], (0, 0, 0), cv2.LINE_AA)

    # Llevo imgx al tamaño de img
    cols, rows, ch = img.shape
    imga = imga[0:cols, 0:rows]

    # Sumo imagenes
    img = cv2.add(img, imga)
    return img


img = cv2.imread('messi.png')
img_aux = cv2.imread('messi.png')

cv2.namedWindow('imagen')
cv2.setMouseCallback('imagen', draw_points)

print("Con el mouse puede seleccionar los puntos donde insertar")
print("Con la letra \'a\' inserta una imagen en la otra")
print("Con la letra \'q\' finaliza la ejecucion del programa")

while True:
    cv2.imshow('imagen', img)
    key = cv2.waitKey(1)

    if key == ord('q'):
        break
    elif key == ord('r'):
        img = cv2.imread('messi.png')
    elif key == ord('a'):
        if len(points) < 3:
            print("\nDebe seleccionar 3 puntos primero")
        else:
            img = img_aux.copy()
            imgx = cv2.imread('copa_america.jpg')
            img = insertar(img, imgx, points)
            cv2.imwrite('output.jpg', img)

cv2.destroyAllWindows()
