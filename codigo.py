import numpy as np
from perceptron import Perceptron
from rede_neural import RedeNeural

estrutura_de_camadas = (2,4,1)
rede_neural = RedeNeural(estrutura = estrutura_de_camadas)
print(rede_neural)

# Gera uma entrada aleatória para a primeira camada da rede
entrada = [4,7] # Essa entrada vem de um conjunto de dados

# Ativando a rede com a entrada fornecida
rede_neural.ativa_rede(entrada = entrada,
                       print_bool = True)