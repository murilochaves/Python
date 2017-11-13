#coding: utf-8

class McCullochPitts():

    # esta classe tem como objetivo facilitar as operações de um neurônio básico de McCulloch-Pitts (1943)

    # construtor padrão, passamos o número de conexão que ele terá (isso dá plasticidade para o neurônio)
    # é criada então um objeto neurônio com pesos sinapticos respectivos para as entradas e um limiar default
    def __init__(self, n_conexoes):
        self.w = [0] * n_conexoes
        self.limiar = 0

    # essa função é utilizada para setar/alterar os valores dos pesos sinápticos.
    # é necessário falar o valor primeiro (5) e depois colocamos a posição do peso, se ele corresponde a w0, w1, ..., wn
    def set_w(self, w, i):
        self.w[i] = w

    # operação principal de um neurônio
    # passamos como argumento a matriz de entrada e então a função percorre pegando os valores e fazendo o somatório
    # u = Σ wkj . xj
    # depois realizamos a função de ativação para cada linha executada verificando se o neurônio foi ativado ou não
    # a fim de bater os valores com a tabela da verdade
    # passamos como argumuento para essa função a matriz x de entrada depois usamos a matriz w para a soma ponderada
    def soma(self, x, t):
        print(' Data \t t \t y \t u')
        # tentando adaptar para camadas:
        y = []

        for k in range(len(x)):
            u = 0
            for j in range(len(self.w)):
                u += x[k][j]*self.w[j]
            print(x[k], '\t', t[k], '\t', self.ativacao(u), '\t', u)

            # tentando adaptar para camadas:
            y.append(self.ativacao(u))

        print(y)

    # adaptação da soma porém para neurônios em camada escondida
    def somatorio(self, x, t):
        print(' Data \t t \t y \t u')
        y = []
        for k in range(len(x)):
            u = 0
            for j in range(len(self.w)):
                u += x[k][j]*self.w[j]
            print(x[k], '\t', t[k], '\t', self.ativacao(u), '\t', u)
            y.append(self.ativacao(u))
        return y

    # função para definir o limiar manualmente, passamos então o valor desejável
    def set_limiar(self, limiar):
        self.limiar = limiar

    # função para distinguir se o neurônio foi ativado ou não, para isso utilizamos a função degrau
    # onde: se u (resultado do somatório) for > limiar temos o número 1 (ativado)
    # caso o somatório não alcance o limiar é retornado 0 (não ativado)
    def ativacao(self, u):
        if u >= self.limiar:
            return 1
        else:
            return 0

# realizado para verificar os colunas de uma matriz de entrada à fim de distinguir a quantidade de conexões
def get_conexao(x):
    return len(x[0])

# aqui é realizado a separação da matriz de entrada para uma outra matriz separada somente as entradas
def separar_entrada(entrada):
    x = []
    for i in range(len(entrada)):
        x.append(entrada[i][:-1])
    return x

# aqui é realizado a separação da matriz de entrada para uma outra matriz separada somente as saídas desejadas (target)
def separar_saida(entrada):
    t = []
    for i in range(len(entrada)):
        t.append(entrada[i][-1])
    return t

###########
## TESTE ##
###########

entrada = [[0, 0, 0], [0, 1, 0], [1, 0, 0], [1, 1, 1]]

x = separar_entrada(entrada)
t = separar_saida(entrada)

n_conexoes = get_conexao(x)

neuronio1 = McCullochPitts(n_conexoes)
neuronio1.set_w(2, 0)
neuronio1.set_w(1, 1)
neuronio1.set_limiar(3)

neuronio1.soma(x, t)