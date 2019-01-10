#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# -*- coding: utf-8 -*-

# Dado arquvios .txt fazer:
# verificar a incidencia das palavras no texto e mostrar via console

# libs requeridas para o script
import sys
from unidecode import unidecode

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
content = archive.readlines()[1:]

# fechando o arquivo
archive.close

# 2. remover todas as letras para minuscula e
# 3. remover todos os caracteres especiais atribuindo a uma otura string
# VERIFICAR COMO USAR AS EXPRESSO REGULARES PARA ALTERAR ESTA PARTE
content = unidecode(''.join(content).lower())

# separando as palavras da string em um array
content = content.split()

# limpando as palavras repetidas
# string_content_split_clean = set(string_content_split)

# contando a quantidade total de palavras
words_total = len(content)

# mostrando o informativo no console
print('\n\t* {}'.format(inf003.format(words_total)))

# 4. constituir um dicionario com as incidencias contendo:
# as palavras unicas armazenadas juntamente com o numero de repeticoes
word_counter = {}

# 5. main do script para realizar a contagem
for word in content:
    if word not in word_counter:
        word_counter[word] = 1
    else:

        word_counter[word] += 1

# contando a quantidade total de palavras diferentes
total_different_words = len(word_counter)

# mostrando o informativo no console
print('\n\t* {}'.format(inf004.format(total_different_words)))

# para mostrar as palavras e incidencias
print('\n\tCount \t Word')

# variavel auxiliar para validacao
words_classified = 0

# mostrando as palavras no console
for word, frequency in word_counter.items():
    print('\t{}\t{}'.format(frequency, word))

    words_classified += frequency

# mostrando a informacao no console
print('\n\t{}\t {}'.format(words_classified, len(word_counter)))

# mostrando o informativo no console
print('\n* {}'.format(inf005))
