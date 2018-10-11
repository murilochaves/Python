#coding: utf-8

import os
from reportlab.graphics.barcode import code128
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from reportlab.graphics.shapes import Drawing 

def main(cod, nome_Produto, cod_interno, preco, qtd_linhas, qtd_colunas):
    
    diretorio = os.path.dirname(os.path.realpath(__file__))
    
    pdf = canvas.Canvas("%s/etiquetas.pdf" % diretorio)
    pdf.setFont("Helvetica", 6)

    codigo_barra = code128.Code128(cod)

    x = 1 * mm
    y = 285 * mm

    ajuste_coluna = 0
    ajuste_linha = 0

    def gerar(aux_extra_linha):
        pdf.drawString(x = x + 12 +  ajuste_coluna, y = y - aux_extra_linha, text=nome_Produto) # er a38

        if (len(cod) < 11):
            codigo_barra.drawOn(pdf, x + 22 + ajuste_coluna, y = y - 23 - aux_extra_linha)    
        elif (len(cod) == 11):
            codigo_barra.drawOn(pdf, x + 10 + ajuste_coluna, y = y - 23 - aux_extra_linha)
        
        pdf.drawString(x = x + 18 + 35 + ajuste_coluna, y = y - 20 - 9 - aux_extra_linha, text=cod_interno)
        pdf.drawString(x = x + 43 + ajuste_coluna, y = y - 20 - 18 - aux_extra_linha, text=preco)

    for i in range(qtd_linhas):

        for j in range(qtd_colunas):
            gerar(ajuste_linha)

            ajuste_coluna += 120 # v2
        
        ajuste_coluna = 0

        #ajuste_linha += 62
        ajuste_linha += 63
    
    pdf.save()

if __name__ == '__main__':
    main(cod = '91892787654', nome_Produto = 'AZEITE DE OLIVA PORTUGUES', cod_interno = '936', preco = 'R$ 328,90', qtd_linhas = 13, qtd_colunas = 5)