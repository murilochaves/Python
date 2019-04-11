#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Este script foi desenvolvido (10/04/2019) utilizando Python3 e tem como objetivo
remover páginas ímpares de um documento PDF.

Requeriments:
* PyPDF2: 1.26.0
"""

# começando com os imports
from PyPDF2 import PdfFileReader, PdfFileWriter

# criando o arquivo pdf para verificar a quantidade de páginas totais
pdf = PdfFileReader(open('arquivo_pdf.pdf','rb'))
# criando o pdf de saída
output = PdfFileWriter()

# percorrendo página por página
for page in range(0, pdf.getNumPages()):
    # se a página for par
    if (page % 2) == 0:
        # coletando a página
        get_page = pdf.getPage(page)
        # adicionando no documento para saída
        output.addPage(get_page)

# abrindo um arquivo novo
with open('new_file.pdf', 'wb') as f:
    # salvando o conteúdo do documento de saída
    output.write(f)