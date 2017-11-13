#coding: utf-8

from urllib2 import urlopen

# atribuindo em uma variável o html da página o comando read é o responsável por retornar
conteudo = urlopen('http://dolarhoje.com/bitcoin-hoje/').read()

# convertendo para string o resultado
conteudo = str(conteudo)

# conteúdo próximo a informação
procurar = '<input type="text" id="nacional" value="'

# a posição onde realmente está o conteúdo
posicao = int(conteudo.index(procurar) + len(procurar))

# atribuindo o valor do bitcoin
bitcoin = conteudo[posicao : posicao + 8]

# retornando a informação obtida
print('Bitcoin: R$ ' + bitcoin)