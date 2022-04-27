# Bibliotecas
import cv2

# Prática da aula 01 - Manipuação de preparação de imagens
# Leitura da imagem
imagem = cv2.imread("mario.png")  # utilização de endereço local

# Mostra a imagem
cv2.imshow("Titulo", imagem) # o método imshow() mostra a imagem na tela
cv2.waitKey(200) # o método waitKey() mantém a imagem na tela por 2000 milisegundos - obs: o argumento = 0 mantem a imagem, mas exige a interrupção da execução

# Como carregar com a imagem em tom de cinza
imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY) # o método cvtColor permite a exibição de acordo com os atributos fornecidos
cv2.imshow("Titulo_gray", imagem_cinza) # mostra a imagem resultante
cv2.waitKey(200) # mantém na tela por 2000  milisegundos

# Como carregar a imagem em tom de cinza diretamente pelo método imread()
imagem_cinza2 = cv2.imread("mario.png", 0) # o parâmetro 0 define que a imagem coloriida seja convertida para cinza
cv2.imshow("Titulo_gray02", imagem_cinza2) # mostra a imagem em tom cinza
cv2.waitKey(200) # por 2000  milisegundos

# Como trabalhar a imagem em HSV (eg. alteração de matiz, etc)
imagem = cv2.imread("mario.png") # carregamos a imagem
imagem_hsv = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV) # convertemos para o formato HSV
imagem_hsv = cv2.add(imagem_hsv, (200, 0, 0, 0)) # aqui, podemos realizar alterações na imagem como esta - "adicona 50 pt na matiz da image"
imagem = cv2.cvtColor(imagem_hsv, cv2.COLOR_HSV2BGR) # após as alterações, convertemos para imagem colorida
cv2.imshow("Titulo_hsv", imagem) # exibe a imagem colorida inicial com as alterações na sua matiz
cv2.waitKey(200)

# Como visualizar a imagem com apenas uma das cores RGB
# Por exemplo, manipularemos a imagem de modo que apenas a cor azul seja visualizada ( note que o azul corresponde ao canal de cor 0)
imagem = cv2.imread("mario.png") # carregamos a imagem
b = imagem.copy()  # fazemos uma cópia da imagem original
b[:, :, 1]= 0 # pegamos todos os pixels da linhas da matriz, todos os pixels das colunas da matriz e as cores verdes (canal de cor 1) e atribuímos o valor 0
b[:, :, 2]= 0 # pegamos todos os pixels da linhas da matriz, todos os pixels das colunas da matriz e as cores vermelhas (canal de cor 2) e atribuímos o valor 0
cv2.imshow("azul", b)
cv2.waitKey(100)

# Repetir a análise acima para a cor verde
g = imagem.copy() # fazemos uma copia da imagem original
g[:, :, 0] = 0 # atribuimos 0 para os pixels de cor azul
g[:, :, 2] = 0 # atribuimos 0 para os pixels de cor vermelha

cv2.imshow("verde", g)
cv2.waitKey(100)

# Repetir a análise acima para a cor vermelha
r = imagem.copy() # fazemos uma copia da imagem original
r[:, :, 0] = 0 # atribuimos 0 para os pixels de cor azul
r[:, :, 1] = 0 # atribuimos 0 para os pixels de cor verde

cv2.imshow("vermelha", r)
cv2.waitKey(100)

# Como realizar desenhos na imagem
imagem = cv2.imread("mario.png") # carregamos a imagem
cv2.rectangle(imagem,  pt1=(150,30), pt2=(300,120),  color = (255,0,0), thickness = 4) # pt1 vertice superior esquerdo e pt2 vértice inferior direito do retângulo
# inserir um retângulo nas coordenadas fornecidas
cv2.imshow("retangulo", imagem)  # inseri um retângulo nas coordenadas fornecidas
cv2.waitKey(2000)

# inserir um círculo nas coordenadas fornecidas
imagem = cv2.imread("mario.png") # carregamos a imagem
cv2.circle(imagem, center= (300,300), radius = 50, color=(0,0,255), thickness=4)
cv2.imshow("circulo", imagem)  # inseri um retângulo nas coordenadas fornecidas
cv2.waitKey(2000)

# inserir uma reta nas coordenadas fornecidas
imagem = cv2.imread("mario.png") # carregamos a imagem
cv2.line(imagem,pt1=(150,30), pt2=(300,120),  color = (255,0,0), thickness = 4)
cv2.imshow("reta", imagem)  # inseri um retângulo nas coordenadas fornecidas
cv2.waitKey(2000)


