# Abrir o arquivo para leitura
arquivo = open('teste.txt', 'r')

for linha in arquivo:
    print linha

arquivo.close