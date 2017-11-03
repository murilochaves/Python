#coding: utf-8

from urllib2 import urlopen

conteudo = urlopen('http://dolarhoje.com/bitcoin').read()

procurar1 = '<span class="symbol">'
posicao1 = int(conteudo.index(procurar1) + len(procurar1))
moeda1 = conteudo[posicao1 : posicao1 + 3]

procurar2 = '<span class="symbol">'
posicao2 = int(conteudo.index(procurar2) + len(procurar2))
moeda2 = conteudo[posicao2 : posicao2 + 3]

procurar3 = '<input type="text" id="nacional" value="'
posicao3 = int(conteudo.index(procurar3) + len(procurar3))
valor = conteudo[posicao3 : posicao3 + 8]

print(moeda1 + ' 1,00 ' + 'vale ' + moeda2 + ' ' + valor)
print ('\n')