import tkinter as tk

# Inicializando o Tkinter
root = tk.Tk()
root.title("Rede interativa")
root.configure(bg="#2C2F33")  # Cor de fundo escura

# Configurações da tela
width, height = 800, 600
canvas = tk.Canvas(root, width=width, height=height, bg="#2C2F33")  # Cor de fundo escura
canvas_info = tk.Canvas(root, width=width/2, height=height/2, bg="#2C2F33")  # Cor de fundo escura
canvas.grid(row=0,column=0)
canvas_info.grid(row=0,column=1)

# Cores
BLACK = "#000000"
WHITE = "#FFFFFF"
GREEN = "#64C832"
DARK_GRAY = "#202225"
LIGHT_GRAY = "#3A3D41"


def criaPosicoes(*, camadas):
    # Cria a lista de posições com base no tamanho da tela
    lista_de_posicoes = []
    distancia_horizontal = int(width / (len(camadas) + 1))
    numero_max_perceptrons = None
    for indice_horizontal, numero_perceptrons in enumerate(camadas, 1):
        distancia_vertical = int(height / (numero_perceptrons + 1))
        for indice_vertical in range(numero_perceptrons):
            x = distancia_horizontal * indice_horizontal
            y = distancia_vertical * (indice_vertical + 1)
            posicao = (x, y)
            lista_de_posicoes.append(posicao)
    return lista_de_posicoes

def criaConexoes(*, camadas):
    # Cores para as conexões entre as camadas
    CORES_CONEXOES = ["#FF5733", "#FFC300", "#C70039", "#900C3F", "#581845"]  # Cores

    # Cria a lista de pares de pontos representando as conexões entre os círculos
    lista_de_pares = []
    for coluna_atual, numero_circulos in enumerate(camadas[:-1]):
        posicoes_coluna_atual = lista_de_posicoes[sum(camadas[:coluna_atual]):sum(camadas[:coluna_atual + 1])]
        posicoes_proxima_coluna = lista_de_posicoes[sum(camadas[:coluna_atual + 1]):sum(camadas[:coluna_atual + 2])]

        cor_conexao = CORES_CONEXOES[coluna_atual % len(CORES_CONEXOES)]  # Seleciona uma cor diferente para cada camada

        for posicao_atual in posicoes_coluna_atual:
            for posicao_proxima in posicoes_proxima_coluna:
                par_de_pontos = [posicao_atual[0], posicao_atual[1], posicao_proxima[0], posicao_proxima[1], cor_conexao]  # Adiciona a cor à lista de pares
                lista_de_pares.append(par_de_pontos)
    return lista_de_pares

# Função para desenhar o círculo
def desenhaCirculo(posicao_circulo, raio_circulo, texto_circulo):
    x, y = posicao_circulo
    circulo_id = canvas.create_oval(x - raio_circulo, y - raio_circulo, x + raio_circulo, y + raio_circulo, outline=BLACK, fill=DARK_GRAY)  # Usando cor escura para os círculos
    canvas.create_text(x, y, text=texto_circulo, fill=WHITE)
    canvas.tag_bind(circulo_id, '<Enter>', lambda event, item=circulo_id: on_hover_enter(event, item))  # Quando o mouse entra no círculo
    canvas.tag_bind(circulo_id, '<Leave>', lambda event, item=circulo_id: on_hover_leave(event, item))  # Quando o mouse sai do círculo

# Função para desenhar as ligações entre os perceptrons
def desenhaLigacoes():
    for par_linha in lista_de_pares:
        canvas.create_line(par_linha[0], par_linha[1], par_linha[2], par_linha[3], fill=par_linha[4], width=2)  # O índice 4 contém a cor da conexão

# Função para alterar a cor do círculo quando o mouse entra
def on_hover_enter(event, item):
    canvas.itemconfig(item, fill=LIGHT_GRAY)

# Função para alterar a cor do círculo quando o mouse sai
def on_hover_leave(event, item):
    canvas.itemconfig(item, fill=DARK_GRAY)

camadas = (2, 3, 4, 5, 1)

lista_de_posicoes = criaPosicoes(camadas = camadas)
lista_de_pares = criaConexoes(camadas = camadas)

print(f'posições:\n{lista_de_posicoes}\n\nligacoes:{lista_de_pares}')

desenhaLigacoes()

# Desenhar os elementos na tela
for i, posicao_circulo in enumerate(lista_de_posicoes):
    raio_circulo = 20  # Definindo o raio do círculo
    texto_circulo = f"{i}"
    desenhaCirculo(posicao_circulo, raio_circulo, texto_circulo)

# Loop principal
root.mainloop()
