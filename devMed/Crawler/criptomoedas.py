#coding: utf-8

from urllib2 import urlopen

criptomoedas = raw_input('Quais as moedas que gostaria de verifica o preço? (se n > 1 coloque apenas espaço)\n')

criptomoedas = criptomoedas.split()

print '\n### Cotação ###'
for i in range(len(criptomoedas)):
    conteudo = urlopen('http://dolarhoje.com').read()
    conteudo = str(conteudo)
    
    procurar1 = '<span class="symbol">'
    posicao1 = int(conteudo.index(procurar1) + len(procurar1))
    moeda1 = conteudo[posicao1 : posicao1 + 3]

    procurar2 = '<span class="symbol">'
    posicao2 = int(conteudo.index(procurar2) + len(procurar2))
    moeda2 = conteudo[posicao2 : posicao2 + 3]

    procurar3 = '<input type="text" id="nacional" value="'
    posicao3 = int(conteudo.index(procurar3) + len(procurar3))
    valor = conteudo[posicao3 : posicao3 + 4]
    
    print(moeda1 + ' 1,00 ' + 'vale ' + moeda2 + ' ' + valor)
print '\n'