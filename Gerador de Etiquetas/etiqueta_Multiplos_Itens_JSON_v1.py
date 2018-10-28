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

# Para controlar as impressões da etiqueta
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

# Para Reduzir um pouco de código dos elif
def switchCase_desc(desc):

    if (len(desc) > 25):
        desc = desc[:25]

    desc = desc[:25]
    tamanhoString = str(len(desc))

    return {
        '1' : 55,
        '2' : 54,
        '3' : 52,
        '4' : 51,
        '5' : 48,
        '6' : 46,
        '7' : 48,
        '8' : 45,
        '9' : 44,
        '10' : 43,
        '11' : 41,
        '12' : 40,
        '12' : 40,
        '13' : 38,
        '14' : 36,
        '15' : 35,
        '16' : 33,
        '17' : 31,
        '18' : 29,
        '19' : 27,
        '20' : 25,
        '21' : 23,
        '22' : 21,
        '23' : 19,
        '24' : 17,
        '25': 14,
    } [tamanhoString]

# Para Reduzir um pouco de código dos elif
def switchCase_barCode(barCode):

    tamanhoBarCode = str(len(barCode))

    return {
        '1' : 27,
        '2' : 27,
        '3' : 22,
        '4' : 25,
        '5' : 19,
        '6' : 22,
        '7' : 16,
        '8' : 19,
        '9' : 13,
        '10' : 16,
        '11' : 10,
        '12' : 13,
        '12' : 13,
        '13' : 7,
        '14' : 11,
    } [tamanhoBarCode]

# Para Reduzir um pouco de código dos elif
def switchCase_code(cod):

    tamanhoCod = str(len(cod))

    return {
        '1' : 55,
        '2' : 54,
        '3' : 52,
        '4' : 51,
        '5' : 49,
        '6' : 47,
        '7' : 46,
        '8' : 44,
        '9' : 42,
        '10' : 40,
    } [tamanhoCod]

# Para Reduzir um pouco de código dos elif
def switchCase_preco(preco):

    tamanhoPreco = str(len(preco))

    return {
        '4' : 47,
        '5' : 45,
        '6' : 43,
        '7' : 41,
        '8' : 40,
        '9' : 38,
    } [tamanhoPreco]

# Função específica para criar as etiquetas.
def executar(lista_produtos, qtd_Total_etiquetas, imprimir = False):
    
    # 1º Passo - Constituir o PDF
    diretorio = os.path.dirname(os.path.realpath(__file__))
    PDF = canvas.Canvas("%s/etiquetasJSON.pdf" % diretorio)
    PDF.setFont("Helvetica", 6)

    # 2º Passo - Inicializando a topologia para o PDF
    x = 1 * mm
    y = 285 * mm

    if (qtd_Total_etiquetas <= 5):
        qtd_linhas = 1
        qtd_colunas = qtd_Total_etiquetas
        coluna_final = qtd_Total_etiquetas
    elif (qtd_Total_etiquetas > 5):
        qtd_linhas = (int(qtd_Total_etiquetas / 5))
        if ((qtd_Total_etiquetas % 5) != 0):
            qtd_linhas = qtd_linhas + 1
        qtd_colunas = 5
        coluna_final = qtd_Total_etiquetas % 5
    
    if (coluna_final == 0):
        coluna_final = 5

    if (qtd_linhas > 13):
        paginasDocumento = qtd_linhas / 13
        if (paginasDocumento != int):
            paginasDocumento = (int(paginasDocumento) + 1)
    elif(qtd_linhas <= 13):
        paginasDocumento = 1

    if (imprimir == True):
        print('\n### Imprimindo valores pertinentes para configuração ###\n')
        print('Cód.:', cod)
        print('Desc. do Produto:', nome_Produto)
        print('Cód. Interno:', cod_interno)
        print('Preço:', preco)
        
        print('')
        
        print('Qtd. de etiquetas:', qtd_etiquetas)
        print('Qtd. linhas da etiqueta:', qtd_linhas)
        print('Qtd. colunas:', qtd_colunas)
        print('Valor da coluna final:', coluna_final)
        print('Qtd. Páginas:', paginasDocumento)

        print('')

    ajuste_coluna = 0
    ajuste_linha = 0

    def plotarEtiquetas(ajuste_linha, ajuste_coluna, object):

        # Descrição/Nome do produto
        desc = object.getDesc()
        # Limitando o tamanho da string para 25
        if (len(desc) > 25): 
            desc = desc[:25]
        # Definindo o valor referente à topologia da plotagem
        ajuste_desc = switchCase_desc(desc)
        # Plotando o nome do produto
        PDF.drawString(x = x + ajuste_desc + ajuste_coluna, y = y - ajuste_linha, text=desc)

        # BarCode
        barCode = object.getBarcode()
        # Verificando se o código tem até 14 caracteres
        if (len(str(barCode)) > 14):
            print('Tamanho excede 14 dígitos, perdendo centralização')
        ajuste_barCode = switchCase_barCode(str(barCode))
        # Plotando o código de barras
        barCode = code128.Code128(barCode)
        barCode.drawOn(PDF, x + ajuste_barCode + ajuste_coluna, y = y - 23 - ajuste_linha)

        # Cod
        cod = str(object.getCod())
        #Verificando o tamanho do código
        if (len(cod) > 10):
            print('Código excede 10 dígitos')
        ajuste_code = switchCase_code(cod)
        # Plotando o Código numeral
        PDF.drawString(x = x + ajuste_code + ajuste_coluna, y = y - 29 - ajuste_linha, text=cod)

        # Preço
        preco = str(object.getValor()[:-1])
        ajuste_preco = switchCase_preco(preco)
        # Plotando o preço do produto
        PDF.drawString(x = x + ajuste_preco + ajuste_coluna, y = y - 20 - 18 - ajuste_linha, text= 'R$ ' + preco)
    
    if (qtd_linhas > 13):
        paginasDocumento = qtd_linhas / 13

        if (paginasDocumento != int):
            paginasDocumento = (int(paginasDocumento) + 1)
    elif (qtd_linhas <= 13):
        paginasDocumento = 1

    if (imprimir == True):
        print('\n### Imprimindo valores pertinentes para configuração ###\n')
        print('Cód.:', cod)
        print('Desc. do Produto:', nome_Produto)
        print('Cód. Interno:', cod_interno)
        print('Preço:', preco)
        
        print('')
        
        print('Qtd. de etiquetas:', qtd_etiquetas)
        print('Qtd. linhas da etiqueta:', qtd_linhas)
        print('Qtd. colunas:', qtd_colunas)
        print('Valor da coluna final:', coluna_final)
        print('Qtd. Páginas:', paginasDocumento)

    # O PROBLEMA ESTA AQUI EM NÃO CONSEGUIR RODAR
    def rodar(qtd_colunas, ajuste_linha, ajuste_coluna):

        aux = 0
        etiquetasGeradas = 0
        auxiliar_etiqueta = 0
        objeto = 0

        for i in range(qtd_linhas):
            aux = aux + 1
            if (aux >= 14):
                PDF.showPage()
                PDF.setFont("Helvetica", 6)

                ajuste_linha = 0
                ajuste_coluna = 0

                aux = 1

            if (i + 1 != qtd_linhas):
                if(qtd_colunas > 5):
                    qtd_colunas = 5
            elif (i + 1 == qtd_linhas):
                qtd_colunas = coluna_final

            for j in range(qtd_colunas):
                
                auxiliar_etiqueta = auxiliar_etiqueta + 1

                print(etiquetasGeradas)

                print('\tObj', objeto)
                if (etiquetasGeradas == lista_produtos[objeto].getQtd()):
                    print(etiquetasGeradas, '     ', lista_produtos[objeto].getQtd())
                    objeto = objeto + 1

                    etiquetasGeradas = 0
                    
                    
                    print('objeto',objeto)

                etiquetasGeradas = etiquetasGeradas + 1

                plotarEtiquetas(ajuste_linha, ajuste_coluna, lista_produtos[objeto])

                ajuste_coluna += 120

            ajuste_coluna = 0

            ajuste_linha += 63


    ajuste_coluna = 0
    ajuste_linha = 0

    rodar(qtd_colunas, ajuste_linha, ajuste_coluna)

    # 4º Passo - Salvar PDF
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

    executar(lista_produtos, qtd_Total_etiquetas)


if __name__ == '__main__':
    main()
