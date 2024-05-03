from perceptron import Perceptron

class RedeNeural:
    def __init__(self,*, estrutura):
        self.estrutura_de_camadas = estrutura
        self.perceptrons = []

        # Criação dos perceptrons para cada camada
        for i_camada, num_perceptrons in enumerate(self.estrutura_de_camadas):
            perceptrons_na_camada = []

            if i_camada == 0:  # Primeira camada
                for _ in range(num_perceptrons):
                    perceptrons_na_camada.append(Perceptron(1,0))
            
            elif i_camada == len(self.estrutura_de_camadas) - 1:  # Última camada
                num_perceptrons_camada_anterior = self.estrutura_de_camadas[i_camada - 1]
                for _ in range(num_perceptrons):
                    perceptrons_na_camada.append(Perceptron(num_perceptrons_camada_anterior, 0))
            
            else:  # Outras camadas
                num_perceptrons_camada_anterior = self.estrutura_de_camadas[i_camada - 1]
                for _ in range(num_perceptrons):
                    perceptrons_na_camada.append(Perceptron(num_perceptrons_camada_anterior))
            
            self.perceptrons.append(perceptrons_na_camada)

    def ativa_rede(self, *, entrada, print_bool=False):
        for i_camada, perceptrons_na_camada in enumerate(self.perceptrons):
            if print_bool==True:
                print(f"== Camada {i_camada} | {len(perceptrons_na_camada)} perceptron(s) == \n")
            saidas_da_camada = []
            if i_camada == 0: # Primeira camada
                for i_perceptron, perceptron in enumerate(perceptrons_na_camada,1):
                    perceptron.input([entrada[i_perceptron-1]])
                    perceptron.ativa()
                    saidas_da_camada.extend(perceptron.saida)
                    if print_bool==True:
                        print(f"\tPerceptron {i_perceptron}: {perceptron}")
                        print(f"\t\tEntradas de {i_perceptron}:{perceptron.entradas}")
                        print(f"\t\tPesos de {i_perceptron}: {perceptron.pesos}")
                        print(f"\t\tBias de {i_perceptron} : {perceptron.bias}\n")
                entrada=saidas_da_camada
                if print_bool==True:
                    print(f"\tSaidas da camada {i_camada}: {saidas_da_camada}\n")

            elif i_camada == len(self.estrutura_de_camadas)-1: # Ultima camada
                saidas_da_camada = []
                for i_perceptron, perceptron in enumerate(perceptrons_na_camada,1):
                    perceptron.input(entrada)
                    perceptron.ativa()
                    saidas_da_camada.extend(perceptron.saida)
                    if print_bool==True:
                        print(f"\tPerceptron {i_perceptron}: {perceptron}")
                        print(f"\t\tEntradas de {i_perceptron}:{perceptron.entradas}")
                        print(f"\t\tPesos de {i_perceptron}: {perceptron.pesos}")
                        print(f"\t\tBias de {i_perceptron} : {perceptron.bias}\n")
                entrada=saidas_da_camada
                if print_bool==True:   
                    print(f"\tSaidas da camada {i_camada}: {saidas_da_camada}\n")

            else: # Outras camadas
                for i_perceptron, perceptron in enumerate(perceptrons_na_camada,1):
                    perceptron.input(entrada)
                    perceptron.ativa()
                    saidas_da_camada.extend(perceptron.saida)
                    if print_bool==True:
                        print(f"\tPerceptron {i_perceptron}: {perceptron}")
                        print(f"\t\tEntradas de {i_perceptron}:{perceptron.entradas}")
                        print(f"\t\tPesos de {i_perceptron}: {perceptron.pesos}")
                        print(f"\t\tBias de {i_perceptron} : {perceptron.bias}\n")
                entrada=saidas_da_camada
                if print_bool==True:
                    print(f"\tSaidas da camada {i_camada}: {saidas_da_camada}\n")
    
    def retropropagacao(self, *, print_bool=False):
        for i_camada, perceptrons_na_camada in enumerate(self.perceptrons):
            pass

    def __str__(self):
        return f'Rede Neural com {len(self.estrutura_de_camadas)} camadas: {self.estrutura_de_camadas}\n'

# == Fim da classe


'''
Para chamar a classe basta:

camadas = (2,3,1)
rede_neural = RedeNeural(camadas)

entrada = [1,2]

rede_neural.ativa_rede(entrada)

# Para printar informações relevantes do perceptron
for i_camada, perceptrons_na_camada in enumerate(rede_neural.perceptrons):
    print(f"== Camada {i_camada} contém ==\n")
    for i_peceptron, perceptron in enumerate(perceptrons_na_camada,1):
        print(f"Perceptron {i_peceptron}:\n{perceptron}")
        print(f"Entradas de {i_peceptron}:{perceptron.entradas}")
        print(f"Pesos de {i_peceptron}: {perceptron.pesos}")
        print(f"Bias de {i_peceptron} : {perceptron.bias}")
        print(f"Saida de {i_peceptron}: {perceptron.saida}\n")

O método rede_neural.perceptrons retorna a lista
com os perceptrons em cada camada

o método __str__ retorna parametros da rede
'''