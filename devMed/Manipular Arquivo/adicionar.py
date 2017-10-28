# Ler o arquivo
arquivo = open('teste.txt', 'r')

# criando uma lista com as linhas
conteudo = arquivo.readlines()

# imprimindo
print conteudo

# criando uma nova linha
conteudo.append('\n')

# abrindo o arquivo para gravação
arquivo = open('teste.txt', 'w')

# adicionando a quebra de linha
arquivo.writelines(conteudo)

# escrevendo em linha (no caso, criada anteriormente)
arquivo.write('teste')

# encerrando o arquivo
arquivo.close