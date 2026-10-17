#importando bibliotecas:
# import "nome da bibilioteca"
#ou
#from "nome biblioteca" import "funcao expecifica"
import matplotlib.pyplot as plt 
"""

dados_x = ["Personagem 1", "Personagem 2", "Personagem 3"]

dados_y = [10, 100, 1020]



plt.title("Titulo do Gráfico")

plt.xlabel("Dados X")

plt.ylabel("Dados Y")

plt.bar(dados_x, dados_y)# bar = tipo do gráfico (gráfico de barras)

plt.show()

linguagens =["python","java","c++","JavaScript"]
alunos = [15,10,12,8]

plt.bar(linguagens, alunos)

plt.title("alunos por linguagem")
plt.xlabel("linguagem")
plt.ylabel("quantidade de alunos")

plt.show()

dias =["segunda","terça","quarta","quinta","sexta"]
vendas = [220,320,450,550,900]

plt.bar(dias, vendas)

plt.title("vendas da semana")
plt.xlabel("dias da semana")
plt.ylabel("quantidade de vendas")

plt.show()


import qrcode

texto = "estou ensinando python para a melhor turma :D"

imagem = qrcode.make(texto)

imagem.save("qrcode.png")
"""

import cv2

image = cv2.imread("planeta.jpg")

image_cinza = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow("image_cinza", image_cinza)

cv2.waitKey(0)

cv2.destroyAllWindows()


