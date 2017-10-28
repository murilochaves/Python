#coding: utf-8

# Abrindo o arquivo para gravação
arquivo = open('teste.txt', 'w')

# Fazendo instrução for para preencher o txt
for i in range(0, 10):
    arquivo.write('Teste %d' % i)
    arquivo.writelines('\n')

# Encerrando o arquivo
arquivo.close