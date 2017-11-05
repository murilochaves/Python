#coding: utf-8

# importanto biblioteca para verificar sequência de caracteres
from difflib import SequenceMatcher

# NUMERAL

# abrindo os arquivos para verificação
with open('/Users/muriloch/Documents/Git/GitHub/Python/sis-info/plagio/dataset/atividade/numeral/file1.txt') as arquivo1, open('/Users/muriloch/Documents/Git/GitHub/Python/sis-info/plagio/dataset/atividade/numeral/file3.txt') as arquivo2:
    # atribuindo em uma variável o txt do arquivo1
    arquivo1_conteudo = arquivo1.read()
    # modificando para tipo string
    arquivo1_conteudo = str(arquivo1_conteudo)
    #print arquivo1_conteudo
    arquivo2_conteudo = arquivo2.read()
    # atribuindo em uma variável o txt do arquivo2
    arquivo2_conteudo = str(arquivo2_conteudo)
    # verificando a porcentagem do plágio
    plagio = SequenceMatcher(None, arquivo1_conteudo, arquivo2_conteudo).ratio()
    # transformando em porcentagem
    plagio = plagio * 100
    # mostrando a porcentagem do plágio
    print ('Plágio: %.2f %%' % plagio)