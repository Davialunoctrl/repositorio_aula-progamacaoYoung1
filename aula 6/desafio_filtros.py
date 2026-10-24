import cv2

image = cv2.imread("planeta.jpg")

print("opção 1=filtro cinza, opção 2=filtro borrado, opção 3=negativo")
filtros = input("escolha a opção:")

if filtros == "1": 
    image_filtro = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

elif filtros == "2": 
    image_filtro = cv2.GaussianBlur(image, (15, 15), 0)

elif filtros == "3":
    image_filtro = cv2.bitwise_not(image)

else:
   print( "invalido")

cv2.imshow("imagem_com_filtro", image_filtro)

cv2.waitKey(0)

cv2.destroyAllWindows()