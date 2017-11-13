#coding: utf-8

# este arquivo objetiva a organização de datasets com as tabelas da verdade

def imprime_tabela(tabela):
    print('\n')
    for i in range(len(tabela)):
        print(tabela[i])

tabelaAnd = [
    [0, 0, 0], 
    [0, 1, 0], 
    [1, 0, 0], 
    [1, 1, 1]
]

tabelaOr = [
    [0, 0, 0], 
    [0, 1, 1], 
    [1, 0, 1], 
    [1, 1, 1]
]

tabelaNot = [
    [0, 1], 
    [1, 0]
]

tabelaNAnd = [
    [0, 0, 1], 
    [0, 1, 1], 
    [1, 0, 1], 
    [1, 1, 0]
]

tabelaNOr = [
    [0, 0, 1], 
    [0, 1, 0], 
    [1, 0, 0], 
    [1, 1, 0]
]

tabelaXor = [
    [0, 0, 0], 
    [0, 1, 1], 
    [1, 0, 1], 
    [1, 1, 0]
]

tabelaCoincidencia = [
    [0, 0, 1], 
    [0, 1, 0], 
    [1, 0, 0], 
    [1, 1, 1]
]