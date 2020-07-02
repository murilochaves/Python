#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""
Programa para criar um arquivo C padrão.
"""

from sys import argv
from os import system, chdir
from os.path import exists

# variável global
content = """#include <stdio.h>

/*

*/

int main() {
\t
\t
    printf("\\n", );
\t
    return 0;
}
"""

if __name__ == "__main__":
    # variáveis de escopo
    shell_command = ''
    file_directory = argv[1].split()
    file_name = argv[2]
    new_file_directory = ''
    root_dir = '/Users/murilochaves/Documents/github/uri-online-judge/'

    # para cada itemo dos tokens do file
    #for item in file_directory:
        # incrementando a string
     #   new_file_directory += '{0}'.format(item)
        #if item != file_directory[-1]:
            # para incluir o '\ ' no lugar dos espaços do caminho path
            #new_file_directory += '\\ '

    # comando padrão de execução com o GCC
    shell_command = 'touch {0}{1}.c'.format(new_file_directory, file_name)

    # trocando pro diretório informado via console
    new_file_directory = root_dir + argv[1]
    chdir(root_dir + argv[1])

    # verificando se o arquivo já existe
    if exists(file_name + '.c'):
        print('\nnão é possível criar um novo arquivo padrão, o próprio arquivo já existe!\n')
        # encerrando imediatamente o script
        exit()
    else:
        # executando o comando do terminal
        system(shell_command)

        # preenchendo com os valores padrões
        with open(file_name + '.c', 'w') as f:
            # anexando conteúdo
            f.writelines(content)

        # abrindo no visual studio code automaticamente
        system('code {0}.c'.format(file_name))
        

    # encerrando o script
    exit()