from random import *

class Neuronio:
    def __init__(self, n):
        self.w = [0.0]*n
        self.b = 0.0
        self.limiar = 0.0

    def soma(self, x):
        y = 0.0

        for i in range(len(x)):
            y += x[i]*self.w[i]

        return y + self.b

    def ativacao(self, x):
        s = self.soma(x)

        if s >= self.limiar:
            return 1
        
        return -1

def treina_adaline(neuronio, entrada, t, alfa, tolerancia):
    for i in range(len(neuronio.w)):
        neuronio.w[i] = random()

    neuronio.b = 0.0

    epocas = 2000
    cont = 0
    erro = 1.0

    while erro > tolerancia and cont < epocas:
        print erro
        erro = 0
        for i in range(len(entrada)):
            x = entrada[i]
            y = neuronio.soma(x)

            for k in range(len(x)):
                neuronio.w[k] += alfa*(t[i] - y)*x[k]
                neuronio.b += alfa*(t[i] - y)

                erro += ((t[i] - y)*(t[i] - y))
            
            cont = cont + 1
            erro = erro/len(entrada)

#==========
# testes
#==========

entrada = [[1, 1], [1, -1], [-1, 1], [-1, -1]]

t = [1, -1, -1, -1]

n1 = Neuronio (2)

alfa = 0.025
tolerancia = 0.15

treina_adaline(n1, entrada, t, alfa, tolerancia)


for i in range(len(entrada)):
    print '%s \t %f \t %f'%(entrada[i], t[i], n1.ativacao(entrada[i]))