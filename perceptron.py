import numpy as np

def funcaoAtivacao(z: float, ativacao: str = "sigmoid"):
    if ativacao=="sigmoid":
        return 1/(1.0+np.exp(-z))

def derivadaAtivacao(z: float):
    derivada = z*(1.0-z)
    return derivada

class Perceptron:
    def __init__(self, entradas=1, bias=0.5):
        self.entradas = np.zeros(entradas)
        self.pesos = np.random.rand(entradas)
        self.saida = np.zeros(1)
        self.bias = [bias]

        self.saida_derivada = np.zeros(1)
        self.erro=np.zeros(1)
        self.delta=np.zeros(1)

    def input(self, array_in):
        if len(array_in)>len(self.entradas):
            raise ValueError("Tamanho de entrada excede o tamanho suportado pelo perceptron")
        
        for i, x_i in enumerate(array_in):
            self.entradas[i] = x_i

    def ativa(self):
        self.saida = funcaoAtivacao(np.dot(self.pesos, self.entradas) + self.bias)
        self.saida_derivada = derivadaAtivacao(self.saida)
        return self.saida, self.bias, self.pesos

    def calculaErro(self, alvo):
        self.erro = alvo - self.saida
        self.delta =  self.erro * self.saida_derivada

    def atualizaPesos(self,taxa_de_aprendizado):
        self.pesos -= taxa_de_aprendizado*self.delta
'''
    def __str__(self):
        return f'Entradas:\n{perceptron.entradas}\n\nAlvo:\n{alvo}\n\nPesos:\n{perceptron.pesos}\n\nBias:\n{perceptron.bias}\n\nSaida:\n{perceptron.saida}\n\nErro:\n{perceptron.erro}\n\nDelta:\n{perceptron.delta}\n'

este método str entra em conflito com o print de debug que estou fazendo
no arquivo"rede_neural.py"então só devo retoma-lo quando tiver concluido

'''

# == Fim da classe


"""
Para chamar a classe:

perceptron = Perceptron(3) # Cria um perceptron com 3 entradas (e "sempre" uma saida)
entrada_e_alvo = [1,2,3,6] # Cria um vetor de entradas
entrada = entrada_e_alvo[:-1]          
alvo = entrada_e_alvo[-1:]
perceptron.input(entrada)  # Insere o vetor de entrada no perceptron
perceptron.ativa()         # Ativa o perceptron e retorna seus parâmetros
perceptron.calculaErro(alvo)

print(perceptron)

perceptron.atualizaPesos(0.5)

print(perceptron)


"""