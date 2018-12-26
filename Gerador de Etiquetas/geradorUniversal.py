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
    def __init__(self, desc = None, barcode = None, codigo = None, valor = None, quantidade = None):
        self.desc       = desc
        self.barcode    = barcode
        self.codigo     = codigo
        self.valor      = valor
        self.quantidade = quantidade

    # getters
    def getDesc(self):
        return self.desc

    def getBarcode(self):
        return self.barcode

    def getCodigo(self):
        return self.codigo

    def getValor(self):
        return self.valor

    def getQuantidade(self):
        return self.quantidade

    # setters
    def setDesc(self, desc):
        self.desc = desc

    def setBarcode(self, barcode):
        self.barcode = barcode

    def setCodigo(self, codigo):
        self.codigo = codigo

    def setValor(self, valor):
        self.valor = valor

    def setQuantidade(self, quantidade):
        self.quantidade = quantidade

# variáveis globais

# constituindo um array para embarcar os objetos 'etiqueta' com todas as informações pertinentes para o script
lista_produtos = []

# facilitar o debug para o desenvolvedor
def printarDevMod(devMod, string):

    '''
    Esta função tem como objetivo facilitar a mostragem de informativos e erros do sistema, caso a função devMod esteja ativo
    '''
    
    # caso o modo de desenvolvimento esteja ativo, é mostrado o informativo/erro referente ao fluxo
    if devMod == True:
        print(
            string
        )

# criando o documento
def criarDocumento(devMod):

    '''
    Esta função tem como objetivo facilitar e centralizar a criação do documento PDF à ser utilizado pelo script.
    '''

    # para facilitar os testes de erro
    try:
        # capturando o caminho do diretório atual
        diretorio = os.path.dirname(os.path.realpath(__file__))

        # mostrando no console o fluxo referente
        printarDevMod(
            devMod,
            '\n* diretorio: %s (inf-010)' % diretorio
        )

        # definindo os ajustes de paginação referentes à criação do PDF

        # Configurações da Página

        # dimensão vertical do documento
        alturaDocumento  = 21.0 * cm
        # dimensão horizontal do documento
        larguraDocumento = 29.7 * cm
        # margem superior
        margemSuperior = 1.52 * cm
        # margem esquerda
        margemEsquerda = 0.72 * cm

        # mostrando no console o fluxo referente
        printarDevMod(
            devMod,
            '\n* configurações da página (inf-011): \nAltura : %s cm [%s] x Largura : %s [%s] \nMargem Superior : %s \nMargem Esquerda : %s' % (alturaDocumento/cm, alturaDocumento, larguraDocumento/cm, larguraDocumento, margemSuperior, margemEsquerda)
        )

        # Configurações da Etiqueta

        # altura útil da etiqueta
        alturaEtiqueta  = 3.81 * cm
        # lalrgura útil da etiqueta
        larguraEtiqueta = 6.35 * cm

        # qtd de linhas perante a etiqueta
        qtdLinhas  = 7
        # qtd de Colunas perante a etiqueta
        qtdColunas = 3

        # mostrando no console o fluxo referente
        printarDevMod(
            devMod,
            '\n* configurações da etiqueta (inf-012): \nAltura útil : %s cm [%s] x Largura útil : %s [%s] \nQtd. Linhas : %s \nQtd. Colunas: %s' % (alturaEtiqueta/cm, alturaEtiqueta, larguraEtiqueta/cm, larguraEtiqueta, qtdLinhas, qtdColunas)
        )

    except:
        # caso o fluxo da criação do PDF dê errado, é mostrado no console o erro
        printarDevMod(
            devMod,
            '\n* Erro na constituição do PDF (erro-002)'
        )

# manipulando o JSON
def manipularJSON(devMod):
    
    '''
    Esta função tem como objetivo facilitar e centralizar a manipulação do JSON passado como argumento para o script.
    '''

    # para facilitar os testes de erro
    try:
        # atribuindo à uma variável o conteúdo do JSON que é passado via console
        contJSON = sys.argv
        
        # mostrando no console o fluxo referente
        printarDevMod(
            devMod,
            '\n* argv: %s (inf-003)' % contJSON
        )

        # capturando as informações sobre os produtos do JSON
        varJSON = json.loads(contJSON[1])

        # mostrando no console o fluxo referente
        printarDevMod(
            devMod,
            '\n* Conteúdo JSON: %s (inf-004)' % varJSON
        )

        # capturando o ID do cliente do JSON
        idCliente = json.loads(contJSON[2])

        # mostrando no console o fluxo referente
        printarDevMod(
            devMod,
            '\n* id do cliente: %s (inf-005)' % idCliente
        )

        # capturando a quantidade total de etiquetas à serem geradas pelo script
        qtd_Total_etiquetas = varJSON["total"]

        # mostrando no console o fluxo referente
        printarDevMod(
            devMod,
            '\n* qtd total de etiquetas: %s (inf-006)' % qtd_Total_etiquetas
        )

        # constituindo um array somente com as informações dos produtos do JSON
        produtos = varJSON["prod"]

        # mostrando no console o fluxo referente
        printarDevMod(
            devMod,
            '\n* qtd de produtos: %s (inf-007)\n' % len(produtos)
        )

        # laço de repetição que tem como objetivo percorrer o array de produtos (var produtos) e ir adicionando um objeto com todas as informações pertinentes
        # para cada item que estiver no produto (repetirá perante a inf-007)
        #for item in produtos:
        for i in range(len(produtos)):
            # mostrando no console o fluxo referente
            printarDevMod(
                devMod,
                '* item %s: %s (inf-008)' % (i+1, produtos[i])
            )

            # adicionando o objeto com as informações no array lista_produtos
            lista_produtos.append(
                # parte da criação do objeto
                Etiqueta(
                    desc       = produtos[i]["pro_desc"],
                    barcode    = produtos[i]["cod_bar"],
                    codigo     = produtos[i]["cod_bar"],
                    valor      = produtos[i]["pro_vlr"],
                    quantidade = produtos[i]["qtd"]
                )
            )

        # mostrando no console o fluxo referente
        printarDevMod(
            devMod,
            '\n* vetor de objetos criado com sucesso: %s (inf-009)' % lista_produtos
        )

    except:
        # caso o fluxo da manipulação do JSON dê errado, é mostrado no console o erro
        printarDevMod(
            devMod,
            '\n* Erro na manipulação do JSON (erro-001)'
        )

# main
def main(devMod = True):
    '''
    Esta função tem como objetivo centralizar o principal fluxo do script.

    O argumento devMod é para possibilitar visualizar todo o processo do script, à fim de encontrar os fluxos e refinar alguma funcionalidade
    '''

    print('\n### Iniciando o processo de Plotar as Etiquetas ### (inf-001)')

    # imprimindo no console a versão do script
    printarDevMod(
        devMod, 
        '\n### devMode ativado ###' + 
        '\n* Versão do Gerador: 05.dez.2018/17:11h (inf-002)'
    )

    # manipulando o JSON que é passado como argumento via console para o script
    manipularJSON(devMod)

    # criando o arquivo PDF
    criarDocumento(devMod)

    
    

# tratativas
if __name__ == "__main__":

    '''
    Esta condição tem como objetivo chamar o fluxo principal.
    '''

    main()


# abaixo, um exemplo de JSON passado como argumento
'''
    $ python3 geradorUniversal.py '{ "prod":[ { "pro_desc":"TESTE", "cod_bar":1878, "pro_un":"KG", "pro_vlr":"110.000", "qtd":17 }, { "pro_desc":"adoro_SNACKS_CAES_MINI/FILHOTE_80G_produz_do_na_china_volumoso_para_plotar", "cod_bar":3013, "pro_un":"UN", "pro_vlr":"3.970", "qtd":32 }, { "pro_desc":"GATOS BOLAS DE PELOS 80G","cod_bar":3012, "pro_un":"UN", "pro_vlr":"6.250", "qtd":21 }, { "pro_desc":"ALCON BOTTON FISH 50G", "cod_bar":1894, "pro_un":"PT", "pro_vlr":"6.690", "qtd":22 }, { "pro_desc":"BANHEIRO CAT TOILETTE 56X40X38CM - 96301", "cod_bar":3790, "pro_un":"UN", "pro_vlr":"104.000", "qtd":7 } ], "config":{ "pageWidith":29.7, "pageHeight":21, "marginLeft":0.7, "marginRight":0.3, "barCodeBase":"pro_cod_pro", "cols":3, "fontSize":7 }, "total":99 }' 1236

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
