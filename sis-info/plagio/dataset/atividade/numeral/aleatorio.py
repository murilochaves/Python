from random import *

def gerarValores(inicial, final, txt):
    for i in range(inicial, final):
        adicionarValores(txt, i)

def geraValoresAleatorios(qtd):
    for i in range(0, qtd):
        numero = random()
        print numero

def lerArquivo(txt):
    arquivo = open(txt, 'r')
    for linha in arquivo:
        print linha
    arquivo.close

def gravarArquivo(txt, valor):
    arquivo = open('' + txt, 'w')
    arquivo.write ('' + valor)
    arquivo.close

def adicionarValores(txt, valor):
    arquivo = open('' + txt, 'r')
    conteudo = arquivo.readlines()
    conteudo.append(' ')
    arquivo = open('' + txt, 'w')
    arquivo.writelines(conteudo)
    valor = str(valor)
    arquivo.write('' + valor)
    arquivo.close

gerarValores(0, 10, 'file1.txt')