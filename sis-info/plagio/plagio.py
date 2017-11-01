#coding: utf-8

# Abrir o arquivo para leitura
arquivo = open('padrao.doc', 'r')

for linha in arquivo:
    print linha

arquivo.close