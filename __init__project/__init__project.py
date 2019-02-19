#!/usr/bin/python3
# -*- coding: utf-8 -*-


"""
Este script tem como objetivo a criação de uma estrutura padrão do python
para diversos projetos à serem desenvolvidos.

Para utilizar basta realizar o comando:

$ python3 __init__project.py {caminho para criar estrutura} {nome_projeto_ingles}

Então ele retornará uma estruta parecida com:

|__ nome_projeto_ingles
|   |__ nome_projeto_ingles.py
|   |__ __init__.py
|__ README.md
|__ .gitignore
|__ LICENSE
|__ setup.cfg
|__ setup.py
|__ tests
    |__ __init__.py
    |__ tests.py

Note que: README.md; .gitignore; LICENSE e outros arquivos não são criados pelo script.
"""


# começando com os imports
import sys
import os
import pathlib


def structure_create():
    """
    Esta função tem como objetivo de criar a estrutura esquemática
    de um respectivo projeto em um diretório que é passado como
    arg para o script.
    """

    # coletando os argumentos
    from_directory_path, name_project = colect_args()

    # reunindo o diretório
    total_path = os.path.join(from_directory_path)
    
    # mudando o caminho para o diretório
    os.chdir(total_path)

    # criando programa principal
    create_main(name_project)

    # criando pasta dos testes
    create_tests()

    # criando arquivos de setup
    create_configs()


def create_main(name_project):
    """
    Esta função tem como objetivo criar a parte principal do programa
    """

    # criando a pasta principal
    os.mkdir(name_project)
    
    # criando os arquivos .py principais
    pathlib.Path('{}/__init__.py'.format(name_project)).touch()
    pathlib.Path('{0}/{0}.py'.format(name_project)).touch()


def create_tests():
    """
    Esta função tem como objetivo criar a parte de testes do programa
    """

    # criando a pasta de testes
    os.mkdir('tests')
    
    # criando os arquivos .py de testes
    pathlib.Path('tests/__init__.py').touch()
    pathlib.Path('tests/tests.py').touch()


def create_configs():
    """
    Esta função tem como objetivo criar a parte de configuração do script.
    """

    # criando o arquivo cfg
    pathlib.Path('setup.cfg').touch()

    # criando o arquivo de setup básico do python
    pathlib.Path('setup.py').touch()


def colect_args():
    """
    Esta função tem como objetivo retornar o conteúdo dos argumentos
    referentes à:

    sys.argv[1] = caminho do diretório para criar a estrutura
    sys.argv[2] = nome do projeto em questão (em inglês e reduzido)

    """

    # declarando e atribuindo valores nas variáveis de escopo
    from_directory_path = sys.argv[1]
    name_project = sys.argv[2]
    
    # nome do projeto em questão
    return from_directory_path, name_project


if __name__ == "__main__":
    # chamando o programa principal
    structure_create()