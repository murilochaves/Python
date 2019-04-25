# Capítulo 8

Lendo e escrevendo em arquivos do livro automatize tarefas maçantes com Python.

### 1. barra invertida no windows e barra pra frente os unix

    # importando biblioteca
    import os

    # criando apontamento correto para os sistemas
    path = os.path.join('usr', 'bin', 'spam')

### 2. unindo nomes de uma lista com nomes de arquivo no final

    # importando biblioteca
    import os

    # criando array do nome dos arquivos
    my_files = ['accounts.txt', 'details.csv', 'invite.docx']

    # para cada arquivo
    for filename in my_files:
        # mostrando em console o nome do arquivo
        print(os.path.join('usr', 'bin', filename))

### 3. diretório de trabalho atual

    # importando biblioteca
    import os

    # capturando o diretório de trabalho atual
    current_directory = os.getcwd()

    # alterando o diretório atual
    os.chdir('/usr/bin/python3')

### 4. criando novas pastas

    # importando biblioteca
    import os

    # criando um novo diretório
    os.makedirs('./nova_pasta')

### 5. diretório atual

    # importando biblioteca
    import os.path

    # coletando o caminho path atual
    os.path.abspath('.')

    # verificar se é um path absoluto
    os.path.isabs(path)

    # capturando o path realtivo
    os.path.realpath(path, início)