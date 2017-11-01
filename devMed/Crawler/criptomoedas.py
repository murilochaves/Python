#coding: utf-8

from urllib2 import urlopen

criptomoedas = raw_input('Quais as moedas que gostaria de verifica o preço? (se n>1 coloque apenas espaço)\n')

criptomoedas = criptomoedas.split()

#print criptomoedas

print '\n### Cotação ###'
for i in range(len(criptomoedas)):

    moeda = str(criptomoedas[i])

    print moeda

    if moeda == 'dolar':
        conteudo = urlopen('http://dolarhoje.com/').read()
    elif moeda == 'bitcoin':
        conteudo = urlopen('http://dolarhoje.com/bitcoin').read()
    elif moeda == 'bitcoin-cash':
        conteudo = urlopen('http://dolarhoje.com/bitcoin-cash-hoje').read()
    elif (moeda == 'ethereum') or (moeda == 'ether') or (moeda == 'eter'):
        conteudo = urlopen('http://dolarhoje.com/ethereum').read()
    elif moeda == 'litecoin':
        conteudo = urlopen('http://dolarhoje.com/litecoin').read()
    elif moeda == 'monero':
        conteudo = urlopen('http://dolarhoje.com/monero').read()
    elif moeda == 'zcash':
        conteudo = urlopen('http://dolarhoje.com/zcash').read()

    conteudo = str(conteudo)
    
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
print '\n'