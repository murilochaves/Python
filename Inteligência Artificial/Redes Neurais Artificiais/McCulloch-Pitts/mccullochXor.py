#coding: utf-8

from dataset import tabelaXor

class McCullochPitts():

    def __init__(self, n_conexoes):
        self.w = [0] * n_conexoes
        self.limiar = 0

    def set_w(self, w, i):
        self.w[i] = w

    def soma(self, x):
        print(' Data \t t \t y \t u')
        for k in range(len(x)):
            u = 0
            for j in range(n_conexoes):
                u += x[k][j]*self.w[j]
            print(x[k], '\t', t[k], '\t', self.ativacao(u), '\t', u)

    def set_limiar(self, limiar):
        self.limiar = limiar

    def ativacao(self, u):
        if u >= self.limiar:
            return 1
        else:
            return 0

entrada = tabelaXor

tem_target = True

if tem_target != False:
    t = []
    x = []
    for i in range(len(entrada)):
        x.append(entrada[i][:-1])
        t.append(entrada[i][-1])
    print('\n# Entrada\'\'\n', x)
    print('\n# Target\'\'\n', t)
else:
    x = entrada
    t = None
    print('\n# Entrada\'\n', x)

print('\n')

n_conexoes = len(x[0])

z = []

print('\n')