#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""
Código Python para facilitar a execução de códigos em C.
gcc -o file_directory/file file_directory/file.c && ./file_directory/file && rm file_directory/file
"""

from sys import argv
from re import search, compile
from os import system

if __name__ == "__main__":
    # variáveis de escopo
    shell_command = ''
    file_directory = []
    new_file_directory = ''
    file_name_pattern = r''
    file_name = ''

    # regex para encontrar apenas o nome do aquivo
    file_name_pattern = r'\/([A-Za-z0-9_-]*).c'
    file_dir_pattern = r'([A-Za-z0-9\/_\-.\\ ]*)[A-Za-z0-9]{4}.c'
    
    # comando padrão de execução com o GCC
    shell_command = 'gcc -o {1}{0} {1}{0}.c && ./{1}{0} && rm {1}{0}'

    # capturando argumentos de console em forma de tokens
    file_directory = argv[1].split()

    # tratamento de erro para verificar se foi passado a extensao .c
    if file_directory[1][-2:] != '.c':
        # se não for, é incrementado para evitar erros
        file_directory[1] += '.c'

    # para cada itemo dos tokens do file
    for item in file_directory:
        # incrementando a string
        new_file_directory += '{0}'.format(item)
        # verificando se não é a última posição 
        if item != file_directory[-1]:
            # para incluir o '\ ' no lugar dos espaços do caminho path
            new_file_directory += '\ '
    
    # capturando os valores do regex e sobrescrevendo
    file_name = search(file_name_pattern, file_directory[-1]).group(1)
    file_directory = search(file_dir_pattern, new_file_directory).group(1)

    # sobrescrevendo o comando shell com os valores para execução
    shell_command = shell_command.format(file_name, file_directory)

    # executando comando via terminal
    system(shell_command)

    # fim do programa
    exit()
