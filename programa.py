# Bibliotecas
import cv2

# Prática da aula 01 - Manipuação de preparação de imagens
# Leitura da imagem
imagem = cv2.imread("mario.png")  # utilização de endereço local

# Mostra a imagem
cv2.imshow("Titulo", imagem) # o método imshow() mostra a imagem na tela
cv2.waitKey(2000) # o método waitKey() mantém a imagem na tela por 2000 milisegundos - obs: o argumento = 0 mantem a imagem, mas exige a interrupção da execução

# Como carregar com a imagem em tom de cinza
imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY) # o método cvtColor permite a exibição de acordo com os atributos fornecidos
cv2.imshow("Titulo_gray", imagem_cinza) # mostra a imagem resultante
cv2.waitKey(2000) # mantém na tela por 2000  milisegundos

# Como carregar a imagem em tom de cinza diretamente pelo método imread()
imagem_cinza2 = cv2.imread("mario.png", 0) # o parâmetro 0 define que a imagem coloriida seja convertida para cinza
cv2.imshow("Titulo_gray02", imagem_cinza2) # mostra a imagem em tom cinza
cv2.waitKey(2000) # por 2000  milisegundos







# a função waitkey() define o tempo de visualização da imagem em milisegundos.