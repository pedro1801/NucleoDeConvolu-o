import random
import numpy as np
import matplotlib.pyplot as plt
import cv2
from tkinter import filedialog as fd
import tkinter as tk
import os
from UI import UI
# Definição do núcleo de convolução
IMG_DIRECTORY=fd.askopenfilename(initialdir=os.getcwd(),title='Escolha a imagem para execucao',filetypes=(('todos os arquivos','*.*'),('jpeg','*.jpeg'),('jpg','*.jpg'),('png','*.png')))#Faz A leitura da Imagem em cinza
image = cv2.imread(IMG_DIRECTORY, cv2.IMREAD_GRAYSCALE)
kernel = UI().kernel
print("Núcleo de convolução criado:")
print(kernel)

# Função para aplicar a convolução
def aplicacao_convolucao(image, kernel):
    altura, largura = image.shape #Pega a altura e a largura da imagem
    kernel_size = kernel.shape[0]#Pega a dimensão da matriz de núcleo
    bordas = kernel_size // 2  # Adiciona padding para a borda da imagem

    # Aplica a convolução na imagem
    convolved_image =np.zeros_like(image,dtype=np.float32)#Cira uma matriz com o tamanho da imagem só que zerada
    for i in range(bordas, altura - bordas):
        for j in range(bordas, largura - bordas):
            pixel_sum = np.sum(image[i - bordas:i + bordas + 1, j - bordas:j + bordas + 1] * kernel)#Soma Todos os pixels da matriz
            #se o pixel_sum for maior que 255 ele ira fazer a normalização da imagem

            if pixel_sum > 255:
                pixel_sum = 255
            if pixel_sum < 0:
                pixel_sum =0

            convolved_image[i, j] = pixel_sum#passa o valor obtido para a imagem       
    return convolved_image


def normalize_image(image):
    min_val = np.min(image)
    max_val = np.max(image)
    normalized_image = (image - min_val) * (255 / (max_val - min_val))
    normalized_image = normalized_image.astype(np.uint8)
    return normalized_image


# Aplicação da convolução na imagem
convolved_image = aplicacao_convolucao(image, kernel)
normalized_imagem = normalize_image(convolved_image)

# Plotar a imagem original
plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Imagem original')

# Plotar a imagem convoluída
plt.subplot(1, 2, 2)
plt.imshow(convolved_image, cmap='gray')
plt.title('Imagem convoluída')

# Exibir os gráficos
plt.show()