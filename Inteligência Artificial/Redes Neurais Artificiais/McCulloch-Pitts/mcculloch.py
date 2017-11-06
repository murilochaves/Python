tabelaAnd = [[0, 0, 0], [0, 1, 0], [1, 0, 0], [1, 1, 1]]

entrada = tabelaAnd

print('x1', '\t x2', '\t t', '\t y')

for i in range(len(entrada)):
    x1 = entrada[i][0]
    x2 = entrada[i][1]
    #t = entrada[i][2]
    t = x1 and x2
    print(x1, '\t', x2, '\t', t, '\t')