def tabelaAnd():
    tabelaE = [[0, 0], [0, 1], [1, 0], [1, 1]]
    print ('\nTabela And')
    print ('A \t B \t X')
    for i in range(len(tabelaE)):
        a = tabelaE[i][0]
        b = tabelaE[i][1]
        x = int(a and b)
        print(a, '\t', b, '\t', x)    

def tabelaOr():
    tabelaOu = [[0, 0], [0, 1], [1, 0], [1, 1]]
    print ('\nTabela Or')
    print ('A \t B \t X')
    for i in range(len(tabelaOu)):
        a = tabelaOu[i][0]
        b = tabelaOu[i][1]
        x = int(a or b)
        print(a, '\t', b, '\t', x)  

def tabelaNot():
    tabelaNao = [[0], [1]]
    print ('\nTabela Not')
    print ('A \t X')
    for i in range(len(tabelaNao)):
        a = tabelaNao[i][0]
        x = int(not a)
        print(a, '\t', x)