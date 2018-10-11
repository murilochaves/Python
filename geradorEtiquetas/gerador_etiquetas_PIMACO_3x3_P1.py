#coding: utf-8

import os
from reportlab.graphics.barcode import code128
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from reportlab.graphics.shapes import Drawing 

def main(cod, nome_Produto, cod_interno, preco, qtd_linhas, qtd_colunas):
    
    diretorio = os.path.dirname(os.path.realpath(__file__))
    
    pdf = canvas.Canvas("%s/etiquetas.pdf" % diretorio)
    pdf.setFont("Helvetica", 10)

    codigo_barra = code128.Code128(cod)

    x = 1 * mm
    y = 285 * mm

    ajuste_coluna = 0
    ajuste_linha = 33

    def gerar(aux_extra_linha):
        pdf.drawString(x = x + 38 + ajuste_coluna, y = y - aux_extra_linha, text=nome_Produto)
        codigo_barra.drawOn(pdf, x + 38 + 10 + ajuste_coluna, y = y - 27 - aux_extra_linha)
        pdf.drawString(x = x + 38 + 10 + 35 + ajuste_coluna, y = y - 27 - 15 - aux_extra_linha, text=cod_interno)
        pdf.drawString(x = x + 38 + 30 + ajuste_coluna, y = y - 27 - 15 - 20 - aux_extra_linha, text=preco)

    for i in range(qtd_linhas):

        for j in range(qtd_colunas):
            gerar(ajuste_linha)

            ajuste_coluna += 192
        
        ajuste_coluna = 0

        ajuste_linha += 110
    
    pdf.save()

if __name__ == '__main__':
    main(cod = '17892413450', nome_Produto = 'AZEITE DE OLIVA PORTUGUES', cod_interno = '936', preco = 'R$ 328,90', qtd_linhas = 7, qtd_colunas = 3)