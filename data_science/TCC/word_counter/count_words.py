#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# -*- coding: utf-8 -*-

# Dado arquvios .txt fazer:
# verificar a incidencia das palavras no texto e mostrar via console

# libs requeridas para o script
import sys
from unidecode import unidecode
from collections import Counter

# string para informativos do programa
inf001 = 'Iniciando processo de embarcar o texto. (inf-001)'
inf002 = 'O arquivo "{}" sera utilizado. (inf-002)'
inf003 = 'O texto possui {} palavras no total. (inf-003)'
inf004 = '{} são palavras diferentes entre si. (inf-004)'
inf005 = 'Programa finalizado. (inf-005)'

# 1. Embarcar o arquivo para captura do texto

# mostrando processo no console
print('\n* {}\n'.format(inf001))

# verificando se o argumento passado por console possui a extensao no
# final '.txt' / Caso não tenha, é adicionado para melhor funcionamento
# do script
if '.txt' not in sys.argv[1]:
    sys.argv[1] += '.txt'

# mostrando o arquivo utilizado no console
print('\t* {}'.format(inf002.format(sys.argv[1])))

# abrindo o arquivo (somente leitura) para a devida manipulação
archive = open('{}'.format(sys.argv[1]), 'r')

# capturando toda a parte util do arquivo (descartando a linha do link)
list_content = archive.readlines()[1:]

# fechando o arquivo
archive.close

# 2. remover todas as letras para minuscula e
# 3. remover todos os caracteres especiais atribuindo a uma otura string
string_content = unidecode(''.join(list_content).lower())

# separando as palavras da string em um array
string_content_split = string_content.split()

# limpando as palavras repetidas
string_content_split_clean = set(string_content_split)

# contando a quantidade total de palavras
words_total = len(string_content_split)

# contando a quantidade total de palavras diferentes
total_different_words = len(string_content_split_clean)

# mostrando o informativo no console
print('\n\t* {}'.format(inf003.format(words_total)))

# mostrando o informativo no console
print('\n\t* {}'.format(inf004.format(total_different_words)))

# 4. constituir um dicionario com as incidencias contendo:
# as palavras unicas armazenadas juntamente com o numero de repeticoes
dictionary_incidents = {}

# para mostrar as palavras e incidencias
print('\n\tCount \t Word')

# variavies auxiliares para validacao
words_classified = 0
total_count = 0

# 5. main do script para realizar a contagem
for word in string_content_split_clean:
    dictionary_incidents['{}'.format(word)] = string_content_split.count(word)
    print('\t{} \t {}'.format(dictionary_incidents[word], word))

    words_classified += 1
    total_count += string_content_split.count(word)

# mostrando a informacao no console
print('\n\t{}\t {}'.format(total_count, words_classified))

# mostrando o informativo no console
print('\n* {}'.format(inf005))
