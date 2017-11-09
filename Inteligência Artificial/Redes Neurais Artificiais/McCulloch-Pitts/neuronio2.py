#coding: utf-8

class McCullochPitts():

    def __init__(self, n_conexoes):
        self.w = [0] * n_conexoes
        self.limiar = 0

    def soma(self, x):
        y = 0

        for i in range(len(x)):
            for j in range(len(x[0])):
                y += x[i][j] * self.w[i]

            return y

    def ativacao(self, x):
        u = self.soma(x)

        if u >= self.limiar:
            return 1
        
        return 0

    def set_w(self, w):
        self.w = w

    def set_limiar(self, limiar):
        self.limiar = limiar

    def imprime_dados(self):
        print(
            'Pesos Sinápticos:', self.w, '\n'
            'Limiar:', self.limiar
        )

###########
## TESTE ##
###########

entrada = [[0, 0], [0, 1], [1, 0], [1, 1]]

t = [0, 0, 0, 1]

n1 = McCullochPitts(2)
n1.set_w([0, 0])
n1.set_limiar(0)

n1.imprime_dados()

saida = []

for i in range(len(entrada)):
    saida.append(n1.ativacao(entrada))

print(saida)