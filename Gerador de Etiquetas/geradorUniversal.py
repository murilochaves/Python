#!/usr/bin/python3
#coding:utf-8

"""
Gerador de etiquetas escrita em Python3

Requirements:
Python==3.7.0
Pillow==5.3.0
reportlab==3.5.9

Autor: JAYME, M. C.
Última modificação: 05 de dezembro de 2018
"""

# libs de sistema requeridas para o funcionamento do script

# compreender argumentos informados pelo console
import sys 
# compreendimento de JSON
import json
# manipulação de diretórios para criar o arquivo da etiqueta
import os, os.path

# libs do python requeridas para o funcionamento do script

# criação de PDF
from reportlab.pdfgen import canvas
# padrão do documento
from reportlab.lib.pagesizes import letter, A4
# manipulação de margens absolutas
from reportlab.lib.units import cm
# criação de códigos de barra
from reportlab.graphics.barcode import code128

# abstração de um objeto etiqueta
class Etiqueta:

    '''
    Esta classe tem como objetivo possibilitar a abstração de uma etiqueta para objetos, à fim de facilitar
    a manipulação das informações referente aos diversos tipos de produtos que serão gerados à partir desta.

    Para utilizar esta classe, deverá ser compreendida da seguinte forma, para possibilitar um correto uso:

    nomeEtiqueta = Etiqueta(
        desc = 'descrição/nome do produto',
        barcode = 'código para a transposição para o código de barras',
        codigo = 'código para plotar abaixo do código de barra - podendo ser o mesmo valor para o barcode'
        valor = 'preço do produto em questão'
        qtd = 'quantidade de etiquetas para aquele determinado produto'
    )
    '''

    # construtor
    def __init__(self, desc = None, barcode = None, codigo = None, valor = None, qtd = None):
        self.desc = desc
        self.barcode = barcode
        self.codigo = codigo
        self.valor = valor

    # getters
    def getDesc(self):
        return self.desc

    def getBarcode(self):
        return self.barcode

    def getCodigo(self):
        return self.codigo

    def getValor(self):
        return self.valor

    def getQtd(self):
        return self.getQtd

    # setters
    def setDesc(self, desc):
        self.desc = desc

    def setBarcode(self, barcode):
        self.barcode = barcode

    def setCodigo(self, codigo):
        self.codigo = codigo

    def setValor(self, valor):
        self.valor = valor

    def setQtd(self, qtd):
        self.getQtd = qtd

# criando o documento
def criarDocumento():
    
    # capturando o caminho do diretório atual
    diretorio = os.path.dirname(os.path.realpath(__file__))

    print(diretorio)

# main
def main(devMod = False):
    '''
    Esta função tem como objetivo centralizar o principal fluxo do script.

    O argumento devMod é para possibilitar visualizar todo o processo do script, à fim de encontrar os fluxos e refinar alguma funcionalidade
    '''

    if devMod == True:
        print('Versão do Gerador: 05.dez.2018/17:11h')

# tratativas
if __name__ == "__main__":

    '''
    Esta condição tem como objetivo chamar o fluxo principal.
    '''

    main()


# abaixo, um exemplo de JSON passado como argumento
'''
    $ python3 geradorEtiqueta.py '{ "prod":[ { "pro_desc":"TESTE", "cod_bar":1878, "pro_un":"KG", "pro_vlr":"110.000", "qtd":17 }, { "pro_desc":"adoro_SNACKS_CAES_MINI/FILHOTE_80G_produz_do_na_china_volumoso_para_plotar", "cod_bar":3013, "pro_un":"UN", "pro_vlr":"3.970", "qtd":32 }, { "pro_desc":"GATOS BOLAS DE PELOS 80G","cod_bar":3012, "pro_un":"UN", "pro_vlr":"6.250", "qtd":21 }, { "pro_desc":"ALCON BOTTON FISH 50G", "cod_bar":1894, "pro_un":"PT", "pro_vlr":"6.690", "qtd":22 }, { "pro_desc":"BANHEIRO CAT TOILETTE 56X40X38CM - 96301", "cod_bar":3790, "pro_un":"UN", "pro_vlr":"104.000", "qtd":7 } ], "config":{ "pageWidith":29.7, "pageHeight":21, "marginLeft":0.7, "marginRight":0.3, "barCodeBase":"pro_cod_pro", "cols":3, "fontSize":7 }, "total":99 }' 1236

    Na anatomia do JSON, a primeira parte é passada todas as informações referentes aos produtos, e na segunda, o código do cliente.

    Caso tenha dúvidas do JSON, verifique o exemplo do JSON formatado.
'''

# abaixo, um exemplo de JSON formatado
'''
    {  
        "prod":[  
            {  
                "pro_desc":"TESTE",
                "cod_bar":1878,
                "pro_un":"KG",
                "pro_vlr":"110.000",
                "qtd":17
            },
            {  
                "pro_desc":"adoro_SNACKS_CAES_MINI/FILHOTE_80G_produz_do_na_china_volumoso_para_plotar",
                "cod_bar":3013,
                "pro_un":"UN",
                "pro_vlr":"3.970",
                "qtd":32
            },
            {  
                "pro_desc":"GATOS BOLAS DE PELOS 80G",
                "cod_bar":3012,
                "pro_un":"UN",
                "pro_vlr":"6.250",
                "qtd":21
            },
            {  
                "pro_desc":"ALCON BOTTON FISH 50G",
                "cod_bar":1894,
                "pro_un":"PT",
                "pro_vlr":"6.690",
                "qtd":22
            },
            {  
                "pro_desc":"BANHEIRO CAT TOILETTE 56X40X38CM - 96301",
                "cod_bar":3790,
                "pro_un":"UN",
                "pro_vlr":"104.000",
                "qtd":7
            }
        ],
        "config":{  
            "pageWidith":29.7,
            "pageHeight":21,
            "marginLeft":0.7,
            "marginRight":0.3,
            "barCodeBase":"pro_cod_pro",
            "cols":3,
            "fontSize":7
        },
        "total":99
    }
'''
