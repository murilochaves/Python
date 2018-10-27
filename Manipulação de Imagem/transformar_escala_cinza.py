#coding:utf-8

# requirements: Pillow
from PIL import Image

#DIDÁTICA

# abrir imagem colorida
img_colorida = Image.open('alan-turing-painting.jpg')

# converter a imagem para escala cinza "L"
img_escala_cinza = img_colorida.convert('L')

# salvando imagem em nova escala
img_escala_cinza.save('alan-turing-painting-cinza.jpg')

# FUNCIONAL
#img = Image.open('alan-turing-painting.jpg').convert('L')
#img.save('greyscale.png')