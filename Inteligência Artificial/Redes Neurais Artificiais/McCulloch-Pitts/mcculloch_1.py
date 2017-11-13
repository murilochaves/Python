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
    def soma(self, x):
        print(' Data \t t \t y \t u')
        for k in range(len(x)):
            u = 0
            for j in range(n_conexoes):
                u += x[k][j]*self.w[j]
            print(x[k], '\t', t[k], '\t', self.ativacao(u), '\t', u)

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

# definimos o vetor de entrada no caso uma função E (And)
entrada = [[0, 0, 0,], [0, 1, 0], [1, 0, 0], [1, 1, 1]]

# utilizei isto para facilitar 'a vida' caso tenhamos a última coluna como o target do programa, assim passamos
# True = a última coluna é o target
# False = não temos target e tudo é entrada para o neurônio
tem_target = True

# aqui é realizado a separação da matriz de entrada para x e a target para t
# a função é realizada caso o valor tem_target seja diferente de false
# assim, adicionaremos em x (entrada) todos os valores menos a última coluna
# enquanto em t (target) colocamos somente a última coluna
# caso o primeiro if não seja atendido e o valor tem_target for Falso, somente atribuímos as matrizes para normatização
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

# realizado para verificar os colunas de uma matriz de entrada à fim de distinguir a quantidade de conexões
n_conexoes = len(x[0])

# aqui é realizado as especificações do neurônio
# criamos um objeto neurônio com n conexões
# setamos limiar
# setamos os valores para w0 e w1 (no caso os pesos sinápticos)
neuronio = McCullochPitts(n_conexoes)
neuronio.set_limiar(10)
neuronio.set_w(5, 0)
neuronio.set_w(5, 1)

# impresso no console os valores atualizados do neurônio para os pesos sinápticos e limiar
print('\n## Neurônio')
print('w\':', neuronio.w)
print('θ:', neuronio.limiar)

# impresso no console e também é realizado a função do somatório juntamente com a ativação
# verificarei em breve para fazer ativação(soma), pois acredito que seria a maneira correta
# porém, por enquanto, a ativação é realizada dentro do somatório
print('\n## Somatório')
neuronio.soma(x)

# quebra linha para facilitar visualização no console
print('\n')