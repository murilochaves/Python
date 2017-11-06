class McCullochsPitts:

    def __init__(self, n_conexoes):
        self.w = [[0]] * n_conexoes
        self.limiar = 0
    
    def set_w(self, w, i):
        self.w[i] = [w]

    def set_limiar(self, limiar):
        self.limiar = limiar

    def soma(self, x):
        y = 0
        for i in range(len(x)):
            print(x[i], y)
            for j in range(len(x[0])):
                x_neuronio = x[i][j]
                w_axonio = self.w[j][0]
                y += x_neuronio * w_axonio
        return y

    def ativacao(self, x):
        s = self.soma(x)
        if s >= self.limiar:
            return 1
        return 0

###########
## TESTE ##
###########

# quebrando linha
print('\n')

# mostrando sobre mcculloch
print('### Neurônio de McCulloch-Pitts')

# criando neurônio mcculloch-pitts com 2 entradas x1 e x2
neuronio = McCullochsPitts(2)

# mostrando os valores default
print('# Default')

# mostrando valores default dos pesos sinapticos
print ('w\' =', neuronio.w)

# mostrando o valor default do limiar
print('Limiar\': ', neuronio.limiar)

# mostrando os valores personalizados
print('\n# Personalizados')

# alterando manualmente os pesos sinapticos
neuronio.set_w(5, 0)
neuronio.set_w(5, 1)

# mostrando valores alterados dos pesos sinapticos
print ('w\'\' =', neuronio.w)

# definindo o limiar de ativação
neuronio.set_limiar(5)

# mostrando o valor do limiar alterado
print('Limiar\'\': ', neuronio.limiar)

# definindo a entrada do neurônio
entrada = [[0, 0], [0, 1], [1, 0], [1, 1]]

# Ativando 
print('\n# Ativação')

# executando ativação de neurônio
print(neuronio.ativacao(entrada))

# quebrando linha para encerrar o código
print('\n')