#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# -*- coding: utf-8 -*-

# TODO: criar uma lista dos atores que apareceram no programa de televisão
# Flying Circus do Monty Python.

# Escreva uma função chamada create_cast_list, que recebe um nome de arquivo
# como entrada e retorna uma lista com o nome dos atores.

# Ela será executado sobre o arquivo flying_circus_cast.txt
# (essa informação foi recolhida de imdb.com).

# Cada linha do arquivo consiste no nome do ator, uma vírgula e algumas
# informações (desarrumadas) sobre os papéis em que eles atuaram no programa.

# Você precisará extrair apenas o nome e adicioná-lo a uma lista. Você pode
# usar o método .split() para processar cada linha.


def create_cast_list(filename):
    cast_list = []
    with open(filename, 'r') as f:
        for line in f:
            if 'Series Cast' not in line:
                name = line.split('\t')[0]
                cast_list.append(name)
    return cast_list

if __name__ == "__main__":
    cast_list = create_cast_list('source_data/flying_circus_cast.txt')
    for actor in cast_list:
        print(actor)
