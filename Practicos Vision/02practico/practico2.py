import cv2

img = cv2.imread('hojas.png' , 0 )

# Para resolverlo podemos usar dos for anidados


for row in range(len(img)) :
    for col in range(len(img)):
        if img[row][col] < 180:
            img[row][col]=0
        
cv2.imwrite('resultado.png', img)

res = cv2.imread('resultado.png')

cv2.imshow('Imagen resultado', res)
cv2.waitKey(0)
cv2.destroyAllWindows()