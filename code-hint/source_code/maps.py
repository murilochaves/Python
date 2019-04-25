#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Script para abrir uma página do google maps com o endereço que for passado
por argumento, e na ausência, ele tenta procurar pelo que está no clipboard.
"""

# começando com os imports
import webbrowser
import sys
import pyperclip

# se tiver informação de argumentos para o script
if len(sys.argv) > 1:
    # obtendo o endereço do argumento
    address = ' '.join(sys.argv[1:])
else:
    # obtendo o endereço do clipboard
    address = pyperclip.paste()

# abrindo o browser com o google maps
webbrowser.open('https://www.google.com/maps/place/' + address)
