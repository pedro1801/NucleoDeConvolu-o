
# Núcleo de Convolução

# Descrição do Projeto

O projeto Núcleo de Convolução foi desenvolvido com o objetivo de realizar operações de convolução em imagens. A convolução é uma técnica amplamente utilizada em processamento de imagens para aplicar filtros e efeitos a uma imagem, transformando-a de acordo com um kernel especificado.

# O que é Convolução?

A convolução é uma operação matemática que combina duas funções para criar uma terceira. 
No contexto de processamento de imagens, ela envolve a sobreposição de um kernel (uma matriz numérica) sobre uma região da imagem e a multiplicação elemento a elemento, 
seguida da soma dos resultados. Esse processo é repetido em toda a imagem, resultando em uma nova imagem processada.

# Bibliotecas Utilizadas

O projeto faz uso das seguintes bibliotecas:

random: Usada para gerar números aleatórios, possivelmente útil na geração de kernels para convolução.
numpy: Utilizada para manipulação eficiente de matrizes e operações numéricas.
matplotlib.pyplot: Empregada para a exibição de imagens e gráficos.
cv2 (OpenCV): Usada para operações de processamento de imagens, incluindo a aplicação da convolução.
tkinter: Utilizada para a criação de uma interface gráfica que permite ao usuário interagir com o programa.
os: Usada para funcionalidades relacionadas ao sistema operacional, como manipulação de arquivos.
Modo de Uso
Execute o programa.
Selecione uma imagem utilizando a interface gráfica.
Adicione um número para ser o kernel da convolução.
Preencha este kernel na interface gráfica.
O efeito da convolução será aplicado à imagem, resultando em uma visualização do processamento.

# Instalção das bibliotecas

pip install numpy
pip install matplotlib
pip install opencv-python
