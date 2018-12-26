#!/usr/bin/python3
#coding:utf-8

"""
Gerador de código de barra desenvolvido em Python para múltiplos produtos, com duas linhas de descrição.

Modelo: PIMACO A4251 (13 linhas X 5 colunas)
Documento: A4 (21.0cm x 29.7cm)
Tamanho útil: 21,2mm x 38,2mm
Qtd. Etiquetas/Folha: 65

Requirements:
Python==3.7.0
Pillow==5.3.0
reportlab==3.5.9

Autor: JAYME, M. C.
Última modificação: 13 de novembro de 2018
"""

import sys
import json
import os, os.path

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.units import cm
from reportlab.graphics.barcode import code128

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

def switchCase_desc(desc):

    if (len(desc) > 27):
        desc = desc[:27]

    desc = desc[:27]
    tamanhoString = str(len(desc))

    return {
        '1' : 57,
        '2' : 56,
        '3' : 54,
        '4' : 53,
        '5' : 50,
        '6' : 48,
        '7' : 50,
        '8' : 47,
        '9' : 46,
        '10' : 45,
        '11' : 43,
        '12' : 42,
        '13' : 41,
        '14' : 38,
        '15' : 37,
        '16' : 35,
        '17' : 33,
        '18' : 31,
        '19' : 29,
        '20' : 27,
        '21' : 26,
        '22' : 23,
        '23' : 21,
        '24' : 21,
        '25': 16,
        '26': 16,
        '27': 19,
    } [tamanhoString]

def switchCase_barCode(barCode):

    tamanhoBarCode = str(len(barCode))

    return {
        '1' : 25,
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
        '14' : 7,
    } [tamanhoBarCode]

def switchCase_code(cod):

    tamanhoCod = str(len(cod))

    return {
        '1' : 56,
        '2' : 56,
        '3' : 54,
        '4' : 53,
        '5' : 51,
        '6' : 49,
        '7' : 48,
        '8' : 46,
        '9' : 44,
        '10' : 42,
    } [tamanhoCod]

def switchCase_preco(preco):

    tamanhoPreco = str(len(preco))

    return {
        '4' : 49,
        '5' : 48,
        '6' : 46,
        '7' : 44,
        '8' : 43,
        '9' : 41,
    } [tamanhoPreco]

def constituir(arquivo = "etiqueta.pdf", pagesize = A4, idCliente = 0, margemX = 0, tamHorizontal = 0, margemY = 0, tamanhoVertical = 0, larguraEtiqueta = 0, alturaEtiqueta = 0, imprimirGrade = False):
    diretorio = os.path.dirname(os.path.realpath(__file__))

    if not os.path.exists("/var/www/storage/midia/%s/" % idCliente):
        os.makedirs("/var/www/storage/midia/%s" % idCliente)

    #if not os.path.exists("./novo/var/www/storage/midia/%s/" % idCliente):
    #    os.makedirs("./novo/var/www/storage/midia/%s" % idCliente)

    PDF = canvas.Canvas("/var/www/storage/midia/%s/etiquetas.pdf" % idCliente, pagesize)
    
    #PDF = canvas.Canvas("./novo/var/www/storage/midia/%s/etiquetas.pdf" % idCliente, pagesize)

    #PDF.setFont("Helvetica", 6)

    PDF.setFont("Helvetica", 5)
    
    if (imprimirGrade != False):
        PDF.grid(range(int(margemX), int(tamHorizontal), int(larguraEtiqueta + (margemX / 2))), range(int(margemY), int(tamanhoVertical), int(alturaEtiqueta)))
    
    return PDF

def plotar(PDF, margemXInicial = 0, tamanhoVertical = 0, margemYInicial = 0, larguraEtiqueta = 0, alturaEtiqueta = 0, qtdTotalEtiquetas = 0, lista = []):

    print('\n### Plotando ###\n')

    print('\t* Qtd. total de Etiquetas: ', qtdTotalEtiquetas)

    if (qtdTotalEtiquetas <= 5):
        qtd_linhas = 1
        qtd_colunas = qtdTotalEtiquetas
        coluna_final = qtdTotalEtiquetas
    elif (qtdTotalEtiquetas > 5):
        qtd_linhas = (int(qtdTotalEtiquetas / 5))
        if ((qtdTotalEtiquetas % 5) != 0):
            qtd_linhas = qtd_linhas + 1
        qtd_colunas = 5
        coluna_final = qtdTotalEtiquetas % 5

    if (coluna_final == 0):
        coluna_final = 5

    if (qtd_linhas > 13):
        paginasDocumento = qtd_linhas / 13
        if (paginasDocumento != int):
            paginasDocumento = (int(paginasDocumento) + 1)
    elif(qtd_linhas <= 13):
        paginasDocumento = 1

    print('\t* Qtd. Linhas: ', qtd_linhas)
    print('\t* Qtd. Colunas: ', qtd_colunas)
    print('\t* Qtd. da Coluna Final: ', coluna_final)
    print('\t* Qtd. de paginas: ', paginasDocumento)

    def plotarEtiquetas(object, coluna, linha):
        
        # Descrição do Produto
        desc = object.getDesc()

        duasLinhas = False
        
        # Particionando a String
        if (len(desc) <= 27): 
            desc = desc[:27]
        if (len(desc) > 27):
            duasLinhas = True

            # Separando primeira parte de string
            descPart1 = desc[:27]
            # Separando a segunda parte da String
            descPart2 = desc[27:54]

            partesString = [descPart1, descPart2]

        ajuste_desc = switchCase_desc(desc)


        # BarCode do Produto
        barCode = object.getBarcode()
        
        if (len(str(barCode)) > 14):
            print('Tamanho excede 14 digitos, perdendo centralizacao')
        
        ajuste_barCode = switchCase_barCode(str(barCode))
        
        barCode = code128.Code128(barCode)


        # Cod
        cod = str(object.getCod())
        
        if (len(cod) > 10):
            print('Codigo excede 10 digitos')
        
        ajuste_cod = switchCase_code(cod)


        # Preço
        preco = str(object.getValor()[:-1])
        ajuste_preco = switchCase_preco(preco)


        # Verificar se a descrição é para ser escrito em duas Strings
        if duasLinhas == True:

            ajusteLinha = 0.35
            
            # Imprimindo as duas linhas da Descrição
            for i in range(2):

                ajuste_desc = switchCase_desc(partesString[i])

                PDF.drawString(
                    x = margemXInicial + ajuste_desc + ((larguraEtiqueta + 0.2 * cm) * coluna), 
                    y = tamanhoVertical - margemYInicial - (ajusteLinha * cm) - (alturaEtiqueta * linha), 
                    text = partesString[i]        
                )

                ajusteLinha += 0.25

            # Imprimindo o código de barras
            barCode.drawOn(
                PDF, 
                x = margemXInicial + ajuste_barCode + ((larguraEtiqueta + 0.2 * cm) * coluna), 
                y = tamanhoVertical - margemYInicial - (1.4 * cm) - (alturaEtiqueta * linha)
            )

            # Plotando o Código numeral
            PDF.drawString(
                x = margemXInicial + ajuste_cod + ((larguraEtiqueta + 0.2 * cm) * coluna), 
                y = tamanhoVertical - margemYInicial - (1.65 * cm) - (alturaEtiqueta * linha), 
                text = cod
            )

            # Plotando o preço do produto
            PDF.drawString(
                x = margemXInicial + ajuste_preco + ((larguraEtiqueta + 0.2 * cm) * coluna), 
                y = tamanhoVertical - margemYInicial - (2 * cm) - (alturaEtiqueta * linha), 
                text = 'R$ ' + preco
            )
        
        # Se tiver somente uma linha
        elif duasLinhas == False:

            # Imprimindo a descrição do produto
            PDF.drawString(
                x = margemXInicial + ajuste_desc + ((larguraEtiqueta + 0.2 * cm) * coluna), 
                y = tamanhoVertical - margemYInicial - (0.5 * cm) - (alturaEtiqueta * linha),
                text = desc
            )

            # Imprimindo o código de barras
            barCode.drawOn(
                PDF, 
                x = margemXInicial + ajuste_barCode + ((larguraEtiqueta + 0.2 * cm) * coluna), 
                y = tamanhoVertical - margemYInicial - (1.3 * cm) - (alturaEtiqueta * linha)
            )

            # Plotando o Código numeral
            PDF.drawString(
                x = margemXInicial + ajuste_cod + ((larguraEtiqueta + 0.2 * cm) * coluna), 
                y = tamanhoVertical - margemYInicial - (1.55 * cm) - (alturaEtiqueta * linha),
                text = cod
            )

            # Plotando o preço do produto
            PDF.drawString(
                x = margemXInicial + ajuste_preco + ((larguraEtiqueta + 0.2 * cm) * coluna), 
                y = tamanhoVertical - margemYInicial - (1.9 * cm) - (alturaEtiqueta * linha), 
                text = 'R$ ' + preco
            )
 

    def rodar(qtd_linhas, qtd_colunas, coluna_final, lista):
        aux = 0
        etiquetasGeradas = 0
        auxiliar_etiqueta = 0
        objeto = 0

        for linha in range(qtd_linhas):
            aux = aux + 1
            #print(linha)

            if (aux >= 14):
                PDF.showPage()
                PDF.setFont("Helvetica", 5)
                aux = 1

            if (linha + 1 != qtd_linhas):
                if(qtd_colunas > 5):
                    qtd_colunas = 5
            elif (linha + 1 == qtd_linhas):
                qtd_colunas = coluna_final

            for coluna in range(qtd_colunas):
                auxiliar_etiqueta = auxiliar_etiqueta + 1

                if (etiquetasGeradas == lista[objeto].getQtd()):
                    objeto = objeto + 1

                    etiquetasGeradas = 0
                                    
                etiquetasGeradas = etiquetasGeradas + 1

                plotarEtiquetas(lista[objeto], coluna, aux - 1)

        print('\n### Etiquetas Geradas com sucesso! ###')

    rodar(qtd_linhas, qtd_colunas, coluna_final, lista)

    PDF.showPage()
    PDF.save()

def main():

    '''
    Esta função tem como objetivo executar todo o escopo do algoritmo.

    É passado os argumentos do console para ter seu conteúdo separado para ser utilizado no decorrer do fluxo.
    '''

    print('Versao 13/nov/2018 14h22 v1')

    # imprimindo processo no console
    print('\n### Iniciando ###\n')

    contJSON = sys.argv
    print('\t* Args:', contJSON)

    # setando uma variável com todo o conteúdo do JSON
    carrJSON = json.loads(contJSON[1])
    # imprimindo processo no console
    print('\t* JSON:', carrJSON)
    
    # setando uma variável com o id do cliente por meio do arg
    cliente = json.loads(contJSON[2])
    # imprimindo processo no console
    print('\t* Cliente:', cliente)

    # setando uma variável com o total de etiquetas a serem geradas
    qtd_Total_etiquetas = carrJSON["total"]
    # imprimindo processo no console
    print('\t* Total de Etiquetas:', qtd_Total_etiquetas)
    
    # setando um array com todos os produtos do JSON
    produtos = carrJSON["prod"]
    # imprimindo processo no console
    print('\t* Total de produtos:', len(produtos))
    
    # criando um array para embarcar cada conteúdo da etiqueta
    lista_produtos = []
    
    # laço de repetição com objetivo de percorrer todos os produtos informados no JSON e criando um objeto com as informações 
    for item in produtos:
        # imprimindo processo no console
        print(item)
        
        # adicionando objeto com as informações na lista de produtos
        lista_produtos.append(
            # criando o objeto com as informações selecionadas do JSON
            Entidade(
                desc = item['pro_desc'],
                barcode = item['cod_bar'],
                cod = item['cod_bar'],
                valor = item['pro_vlr'],
                qtd = item['qtd']
            )
        )
    
    # imprimindo processo no console
    print('\n\t* Vetor de Objetos criados:', lista_produtos)

    # definindo todos os ajustes referentes à impressão da página da etiqueta (obtido no proprio site da PIMACO)
    
    # dimensão vertical da folha
    tamanhoX = 21.0 * cm
    # dimensão horizontal da folha
    tamanhoY = 29.7 * cm

    # dimensão da margem superior
    margemSuperior = 1.07 * cm
    # dimensão da margem lateral (esquerda)
    margemLateral = 0.45 * cm

    # dimensão da altura da própria etiqueta em questão
    alturaUtilEtiqueta = 2.12 * cm
    # dimensão da largura da própria etiqueta em questão
    larguraUtilEtiqueta = 3.82 * cm
    
    # criando o PDF passando todos os argumentos para facilitar a manipulação posteriormente
    PDF = constituir(
        arquivo = 'etiqueta.pdf', 
        pagesize = (tamanhoX, tamanhoY), 
        idCliente = cliente,
        margemX = margemLateral, 
        tamHorizontal = tamanhoX, 
        margemY = margemSuperior, 
        tamanhoVertical = tamanhoY,
        larguraEtiqueta = larguraUtilEtiqueta,
        alturaEtiqueta = alturaUtilEtiqueta,
        imprimirGrade = False
        )

    # plotando todas as informações no documento
    plotar(
        PDF,
        margemXInicial = margemLateral,
        tamanhoVertical = tamanhoY,
        margemYInicial = margemSuperior,
        larguraEtiqueta = larguraUtilEtiqueta,
        alturaEtiqueta = alturaUtilEtiqueta,
        qtdTotalEtiquetas = qtd_Total_etiquetas,
        lista = lista_produtos
        )

if __name__ == '__main__':

    '''
    Esta função tem como objetivo  chamar o programa principal.
    '''
    main()

    # $ python3 novaEtiqueta13-nov-2018.py '{ "prod":[ { "pro_desc":"TESTE", "cod_bar":1878, "pro_un":"KG", "pro_vlr":"110.000", "qtd":17 }, { "pro_desc":"adoro_SNACKS_CAES_MINI/FILHOTE_80G_produz_do_na_china_volumoso_para_plotar", "cod_bar":3013, "pro_un":"UN", "pro_vlr":"3.970", "qtd":32 }, { "pro_desc":"GATOS BOLAS DE PELOS 80G","cod_bar":3012, "pro_un":"UN", "pro_vlr":"6.250", "qtd":21 }, { "pro_desc":"ALCON BOTTON FISH 50G", "cod_bar":1894, "pro_un":"PT", "pro_vlr":"6.690", "qtd":22 }, { "pro_desc":"BANHEIRO CAT TOILETTE 56X40X38CM - 96301", "cod_bar":3790, "pro_un":"UN", "pro_vlr":"104.000", "qtd":7 } ], "config":{ "pageWidith":29.7, "pageHeight":21, "marginLeft":0.7, "marginRight":0.3, "barCodeBase":"pro_cod_pro", "cols":3, "fontSize":7 }, "total":99 }' 1236
