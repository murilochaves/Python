#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Gerador de código de barra desenvolvido em Python para múltiplos produtos

Modelo: PIMACO A4251 (13 linhas X 5 colunas)
Tamanho útil: 21,2mm x 38,2mm
Qtd. Etiquetas/Folha: 65

Requirements:
Python==3.7.0
Pillow==5.3.0
reportlab==3.5.9

Autor: JAYME, M. C.
Última modificação: 18 de outubro de 2018
"""

import sys
import json
import os

from reportlab.graphics.barcode import code128
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from reportlab.graphics.shapes import Drawing

class Entidade:

    """
    Implementação de classe com objetivo de realizar a abstração de uma entidade - no caso, um obj etiqueta.

    Modo de uso com a declaração de seus args[]:
    nomeEtiqueta = Entidade(
        descrição = 'descricao ou nome do produto', barcode = 'número do código de barro à ser gerado', 
        codigo = 'número do código para ser impresso na tela', 
        valor = 'preço do produto'
        )
    """

    # Construtor
    def __init__(self, desc = None, barcode = None, cod = None, valor = None, qtd = None):
        self.desc = desc
        self.barcode = barcode
        self.cod = cod
        self.valor = valor
        self.qtd = qtd

    # Setters
    def setDesc(self, desc):
        self.desc = desc
    
    def setBarcode(self, barcode):
        self.barcode = barcode

    def setCod(self, cod):
        self.cod = cod
    
    def setValor(self, valor):
        self.valor = valor

    def setQtd(self, qtd):
        self.qtd = qtd

    # Getters
    def getDesc(self):
        return self.desc

    def getBarcode(self):
        return self.barcode

    def getCod(self):
        return self.cod

    def getValor(self):
        return self.valor

    def getQtd(self):
        return self.qtd

def rodar(lista_produtos, qtd_Total_etiquetas, imprimir = False):
    # 1º Passo - Constituir o PDF
    diretorio = os.path.dirname(os.path.realpath(__file__))
    PDF = canvas.Canvas("%s/etiquetasJSON.pdf" % diretorio)
    PDF.setFont("Helvetica", 6)

    # 2º Passo - Popular o PDF
    PDF.drawString(x = 200, y = 100, text="Ola mundo!")

    # 3º Passo - Salvar PDF
    PDF.save()

def main():

    # PARTE DA LEITURA DO JSON
    # Coletando conteúdo JSON passado como argumento no terminal
    # python3 nome_arq.py 
    contJSON = sys.argv

    # Criando um dicionário em python populando com o conteúdo do JSON
    carrJSON = json.loads(contJSON[1])

    # Podando o JSON para obter somente os produtos
    produtos = carrJSON["prod"]
    print('\n### JSON dos produtos:\n', produtos)
    print('\n### Qtd. de produtos: ', len(produtos))

    # Criando um vetor para embarcar os objetos do JSON
    lista_produtos = []

    # Percorrendo os produtos do JSON para criar todos os objetos produtos
    for item in produtos:
        print(item)
        #print('pro_desc:', item['pro_desc']) 
        #print('cod_bar:', item['cod_bar']) 
        #print('pro_un:', item['pro_un']) 
        #print('pro_vlr:', item['pro_vlr']) 
        #print('qtd:', item['qtd'], '\n') 
        lista_produtos.append(
            Entidade(
                desc = item['pro_desc'],
                barcode = item['cod_bar'],
                cod = item['cod_bar'],
                valor = item['pro_vlr'],
                qtd = item['qtd']
            )
        )
    
    print('\n### Vetor de objetos:\n', lista_produtos)
    
    # Pegando o total de etiquetas à serem geradas
    qtd_Total_etiquetas = carrJSON["total"]
    print('\n### Qtd. totais de etiquetas: ', qtd_Total_etiquetas)

    rodar(lista_produtos, qtd_Total_etiquetas)


if __name__ == '__main__':
    main()
