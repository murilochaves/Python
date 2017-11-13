#coding: utf-8

import datetime

# estas funçõe stem como objetivo facilitar a utilização do padrão brasileiro dd/mm/aaaa
# ao utilizar este arquivo, é gerado um arquivo dataPersonalizada.pyc que é uma comilação do código interpretado

# funcao para adicionar a data em padrão brasileiro
def set_data(dia, mes, ano):
    return datetime.date(ano, mes, dia)

# ainda não funciona porém estou fazendo teste para formatar a saída da data em padrão brasileiro dd/mm/aaaa
def get_data(data):
    teste = datetime.date.strftime("%Y") 
    return teste

###########
## TESTE ##
###########

#teste = set_data(23, 1, 1992)

#print get_data(teste)