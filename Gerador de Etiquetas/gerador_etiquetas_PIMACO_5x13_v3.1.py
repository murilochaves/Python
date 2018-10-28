#coding: utf-8

import os
from reportlab.graphics.barcode import code128
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from reportlab.graphics.shapes import Drawing

def main(cod, nome_Produto, cod_interno, preco, qtd_etiquetas, imprimir = False):
    
    diretorio = os.path.dirname(os.path.realpath(__file__))
    
    pdf = canvas.Canvas("%s/etiquetas.pdf" % diretorio)
    pdf.setFont("Helvetica", 6)

    codigo_barra = code128.Code128(cod)

    x = 1 * mm
    y = 285 * mm

    # Ajuste para sempre colocar os decimais
    if (preco.__contains__(',') == False):
        preco = preco + ',00'

    def gerarEtiquetas(ajuste_linha, ajuste_coluna):
        # DESCRIÇÃO DO PRODUTO - tratamento de erros para centralização
        if (len(nome_Produto) == 1):
            pdf.drawString(x = x + 55 + ajuste_coluna, y = y - ajuste_linha, text=nome_Produto)
        elif (len(nome_Produto) == 2):
            pdf.drawString(x = x + 54 + ajuste_coluna, y = y - ajuste_linha, text=nome_Produto)
        elif (len(nome_Produto) == 3):
            pdf.drawString(x = x + 52 + ajuste_coluna, y = y - ajuste_linha, text=nome_Produto)
        elif (len(nome_Produto) == 4):
            pdf.drawString(x = x + 51 + ajuste_coluna, y = y - ajuste_linha, text=nome_Produto)
        elif (len(nome_Produto) == 5):
            pdf.drawString(x = x + 48 + ajuste_coluna, y = y - ajuste_linha, text=nome_Produto)
        elif (len(nome_Produto) == 6):
            pdf.drawString(x = x + 46 + ajuste_coluna, y = y - ajuste_linha, text=nome_Produto)
        elif (len(nome_Produto) == 7):
            pdf.drawString(x = x + 48 + ajuste_coluna, y = y - ajuste_linha, text=nome_Produto)
        elif (len(nome_Produto) == 8):
            pdf.drawString(x = x + 45 + ajuste_coluna, y = y - ajuste_linha, text=nome_Produto)
        elif (len(nome_Produto) == 9):
            pdf.drawString(x = x + 44 + ajuste_coluna, y = y - ajuste_linha, text=nome_Produto)
        elif (len(nome_Produto) == 10):
            pdf.drawString(x = x + 43 + ajuste_coluna, y = y - ajuste_linha, text=nome_Produto)
        elif (len(nome_Produto) == 11):
            pdf.drawString(x = x + 41 + ajuste_coluna, y = y - ajuste_linha, text=nome_Produto)
        elif (len(nome_Produto) == 12):
            pdf.drawString(x = x + 40 + ajuste_coluna, y = y - ajuste_linha, text=nome_Produto)
        elif (len(nome_Produto) == 13):
            pdf.drawString(x = x + 38 + ajuste_coluna, y = y - ajuste_linha, text=nome_Produto)
        elif (len(nome_Produto) == 14):
            pdf.drawString(x = x + 36 + ajuste_coluna, y = y - ajuste_linha, text=nome_Produto)
        elif (len(nome_Produto) == 15):
            pdf.drawString(x = x + 35 + ajuste_coluna, y = y - ajuste_linha, text=nome_Produto)
        elif (len(nome_Produto) == 16):
            pdf.drawString(x = x + 33 + ajuste_coluna, y = y - ajuste_linha, text=nome_Produto)
        elif (len(nome_Produto) == 17):
            pdf.drawString(x = x + 31 + ajuste_coluna, y = y - ajuste_linha, text=nome_Produto)
        elif (len(nome_Produto) == 18):
            pdf.drawString(x = x + 29 + ajuste_coluna, y = y - ajuste_linha, text=nome_Produto)
        elif (len(nome_Produto) == 19):
            pdf.drawString(x = x + 27 + ajuste_coluna, y = y - ajuste_linha, text=nome_Produto)
        elif (len(nome_Produto) == 20):
            pdf.drawString(x = x + 25 + ajuste_coluna, y = y - ajuste_linha, text=nome_Produto)
        elif (len(nome_Produto) == 21):
            pdf.drawString(x = x + 23 + ajuste_coluna, y = y - ajuste_linha, text=nome_Produto)
        elif (len(nome_Produto) == 22):
            pdf.drawString(x = x + 21 + ajuste_coluna, y = y - ajuste_linha, text=nome_Produto)
        elif (len(nome_Produto) == 23):
            pdf.drawString(x = x + 19 + ajuste_coluna, y = y - ajuste_linha, text=nome_Produto)
        elif (len(nome_Produto) == 24):
            pdf.drawString(x = x + 17 + ajuste_coluna, y = y - ajuste_linha, text=nome_Produto)
        elif (len(nome_Produto) == 25):
            pdf.drawString(x = x + 14 + ajuste_coluna, y = y - ajuste_linha, text=nome_Produto)
        elif (len(nome_Produto) > 25): 
            print('Tamanho do descrição maior que 25 dígitos - não está mais centralizado')

        # CÓDIGO DE BARRAS - tratamento de erros para centralização
        if (len(cod) <= 2):
            codigo_barra.drawOn(pdf, x + 27 + ajuste_coluna, y = y - 23 - ajuste_linha)
        elif (len(cod) == 3):
            codigo_barra.drawOn(pdf, x + 22 + ajuste_coluna, y = y - 23 - ajuste_linha)
        elif (len(cod) == 4):
            codigo_barra.drawOn(pdf, x + 25 + ajuste_coluna, y = y - 23 - ajuste_linha)
        elif (len(cod) == 5):
            codigo_barra.drawOn(pdf, x + 19 + ajuste_coluna, y = y - 23 - ajuste_linha)
        elif (len(cod) == 6):
            codigo_barra.drawOn(pdf, x + 22 + ajuste_coluna, y = y - 23 - ajuste_linha)
        elif (len(cod) == 7):
            codigo_barra.drawOn(pdf, x + 16 + ajuste_coluna, y = y - 23 - ajuste_linha)
        elif (len(cod) == 8):
            codigo_barra.drawOn(pdf, x + 19 + ajuste_coluna, y = y - 23 - ajuste_linha)
        elif (len(cod) == 9):
            codigo_barra.drawOn(pdf, x + 13 + ajuste_coluna, y = y - 23 - ajuste_linha)
        elif (len(cod) == 10):
            codigo_barra.drawOn(pdf, x + 16 + ajuste_coluna, y = y - 23 - ajuste_linha)
        elif (len(cod) == 11):
            codigo_barra.drawOn(pdf, x + 10 + ajuste_coluna, y = y - 23 - ajuste_linha)
        elif (len(cod) == 12):
            codigo_barra.drawOn(pdf, x + 13 + ajuste_coluna, y = y - 23 - ajuste_linha)
        elif (len(cod) == 13):
            codigo_barra.drawOn(pdf, x + 7 + ajuste_coluna, y = y - 23 - ajuste_linha)
        elif (len(cod) == 14):
            codigo_barra.drawOn(pdf, x + 11 + ajuste_coluna, y = y - 23 - ajuste_linha)
        elif (len(cod) > 14): 
            print('Tamanho do código maior que 14 dígitos - não está mais centralizado')
        
        # CÓDIGO INTERNO DO PRODUTO - Tratamento de erro para centralizar
        if (len(cod_interno) == 1):
            pdf.drawString(x = x + 55 + ajuste_coluna, y = y - 29 - ajuste_linha, text=cod_interno)
        elif (len(cod_interno) == 2):
            pdf.drawString(x = x + 54 + ajuste_coluna, y = y - 29 - ajuste_linha, text=cod_interno)
        elif (len(cod_interno) == 3):
            pdf.drawString(x = x + 52 + ajuste_coluna, y = y - 29 - ajuste_linha, text=cod_interno)
        elif (len(cod_interno) == 4):
            pdf.drawString(x = x + 51 + ajuste_coluna, y = y - 29 - ajuste_linha, text=cod_interno)
        elif (len(cod_interno) == 5):
            pdf.drawString(x = x + 49 + ajuste_coluna, y = y - 29 - ajuste_linha, text=cod_interno)
        elif (len(cod_interno) == 6):
            pdf.drawString(x = x + 47 + ajuste_coluna, y = y - 29 - ajuste_linha, text=cod_interno)
        elif (len(cod_interno) == 7):
            pdf.drawString(x = x + 46 + ajuste_coluna, y = y - 29 - ajuste_linha, text=cod_interno)
        elif (len(cod_interno) == 8):
            pdf.drawString(x = x + 44 + ajuste_coluna, y = y - 29 - ajuste_linha, text=cod_interno)
        elif (len(cod_interno) == 9):
            pdf.drawString(x = x + 42 + ajuste_coluna, y = y - 29 - ajuste_linha, text=cod_interno)
        elif (len(cod_interno) == 10):
            pdf.drawString(x = x + 40 + ajuste_coluna, y = y - 29 - ajuste_linha, text=cod_interno)
        elif (len(cod_interno) > 10): 
            print('Tamanho do codigo interno maior que 10 dígitos - não está mais centralizado')

        # PREÇO - Tratamento de erro para centralizar
        if (len(preco) < 4):
            print('Preço errado')
        if (len(preco) == 4):
            pdf.drawString(x = x + 47 + ajuste_coluna, y = y - 20 - 18 - ajuste_linha, text= 'R$ ' + preco)
        if (len(preco) == 5):
            pdf.drawString(x = x + 45 + ajuste_coluna, y = y - 20 - 18 - ajuste_linha, text= 'R$ ' + preco)
        if (len(preco) == 6):
            pdf.drawString(x = x + 43 + ajuste_coluna, y = y - 20 - 18 - ajuste_linha, text= 'R$ ' + preco)
        if (len(preco) == 7):
            pdf.drawString(x = x + 41 + ajuste_coluna, y = y - 20 - 18 - ajuste_linha, text= 'R$ ' + preco)
        if (len(preco) == 8):
            pdf.drawString(x = x + 40 + ajuste_coluna, y = y - 20 - 18 - ajuste_linha, text= 'R$ ' + preco)
        if (len(preco) == 9):
            pdf.drawString(x = x + 38 + ajuste_coluna, y = y - 20 - 18 - ajuste_linha, text= 'R$ ' + preco)
        if (len(preco) > 9):
            print('Preço do produto é maior que 9 dígitos - não está otimizando para centralizar')
    
    # TRATAMENTO DE ERRO PARA QTD DE ETIQUETAS
    if (qtd_etiquetas <= 5):
        qtd_linhas = 1
        qtd_colunas = qtd_etiquetas
        coluna_final = qtd_etiquetas
    
    # TRATAMENTO DE ERRO PARA ÚLTIMA COLUNA DA ULTIMA LINHA
    if (qtd_etiquetas > 5):
        qtd_linhas = (int(qtd_etiquetas / 5))
        if ((qtd_etiquetas % 5) != 0):
            qtd_linhas = qtd_linhas + 1
        qtd_colunas = 5
        coluna_final = qtd_etiquetas % 5
        if (coluna_final == 0):
            coluna_final = 5

    # Tratamento para construir várias páginas
    if (qtd_linhas > 13):
        paginasDocumento = qtd_linhas / 13
        
        if (paginasDocumento != int):
            paginasDocumento = (int(paginasDocumento)+1)
    
    elif (qtd_linhas <= 13):
        paginasDocumento = 1
        
    # somente impressão de valores
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

    def rodar(qtd_colunas, ajuste_linha, ajuste_coluna):
        
        aux = 0
        
        for i in range(qtd_linhas):

            aux = aux + 1
            #print(aux)

            #print('\t\tvalor aux:', aux)
            if (aux >= 14):
                #print('entrou!', aux)
                pdf.showPage()
                pdf.setFont("Helvetica", 6)

                ajuste_linha = 0
                ajuste_coluna = 0
                
                aux = 1

            #if (i+1 != qtd_linhas):
            if (i+1 != qtd_linhas):
                if (qtd_colunas > 5):
                    qtd_colunas = 5
            #elif (i+1 == qtd_linhas):
            elif (i+1 == qtd_linhas):
                qtd_colunas = coluna_final

            for j in range(qtd_colunas):
                gerarEtiquetas(ajuste_linha, ajuste_coluna)

                ajuste_coluna += 120
            
            ajuste_coluna = 0

            #ajuste_linha += 62
            ajuste_linha += 63
                
            
    ajuste_coluna = 0
    ajuste_linha = 0

    rodar(qtd_colunas, ajuste_linha, ajuste_coluna)

    pdf.save()

if __name__ == '__main__':
    main(cod = '1', nome_Produto = 'AZEITE DE OLIVA PORTUGUES', cod_interno = '936', preco = '12.233', qtd_etiquetas = 196, imprimir=False)