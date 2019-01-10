import sys
import os

"""
Este código, possui como objetivo facilitar a criação de uma quantidade de
pastas tendo um arquivo .txt em branco dentro de cada uma, visando uma
necessidade do dia-a-dia que tive. A quantidade de pastas é informada via
console: "python3 ...create_folders.py 12", assim ele criará 12 pastas com o
.txt desejado.
"""


def execute():
    """Esta função tem como objetivo centralizar o escopo do script"""

    folder_quantity = int(sys.argv[1])

    directory = os.path.dirname(os.path.realpath(__file__))

    for i in range(folder_quantity):
        os.makedirs('{}/{}./'.format(directory, i+1))
        file = open('{}/{}./texto.txt'.format(directory, i+1), 'w')
        file.close()

if __name__ == "__main__":
    execute()
