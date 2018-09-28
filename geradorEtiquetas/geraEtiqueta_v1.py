
import os
from reportlab.graphics.barcode import code39, code128, code93
from reportlab.graphics.barcode import eanbc, qr, usps
from reportlab.graphics.shapes import Drawing 
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas
from reportlab.graphics import renderPDF
 
def gerarCodigo(codigo, qtd_linhas, qtd_colunas):

    diretorio = os.path.dirname(os.path.realpath(__file__))

    pdf = canvas.Canvas("%s/etiquetas.pdf" % diretorio)
 
    codigo_barra = codigo
  
    codigo = code128.Code128(codigo_barra)
 
    x = 1 * mm
    y = 285 * mm
    #x1 = 6.4 * mm
 
    produto = 'AZEITE DE OLIVA PORTUGUES'
    codigo_interno = '936'
    preco_produto = 'R$ 328,90'

    pdf.setFont("Helvetica", 10)

    #qtd_linhas = 2
    #qtd_colunas = 1

    ajuste_coluna = 0

    def rodar():
        pdf.drawString(x= x+38+ajuste_coluna, y=y-33-ajuste_linha, text=produto) # NAO MEXER !!!!!!!!
        codigo.drawOn(pdf, x+38+10+ajuste_coluna, y-33-27-ajuste_linha) # NAO MEXER/ MAIS OU MENOS
        pdf.drawString(x= x+38+10+35+ajuste_coluna, y=y-33-27-15-ajuste_linha, text=codigo_interno) # MAIS OU MENOS
        pdf.drawString(x= x+38+30+ajuste_coluna, y=y-33-27-15-20-ajuste_linha, text=preco_produto)
        
    def rodar2(aux_extra_linha):
        pdf.drawString(x= x+38+ajuste_coluna, y=y-aux_extra_linha, text=produto)
        codigo.drawOn(pdf, x+38+10+ajuste_coluna, y=y-27-aux_extra_linha)
        pdf.drawString(x= x+38+10+35+ajuste_coluna, y=y-27-15-aux_extra_linha, text=codigo_interno)
        pdf.drawString(x= x+38+30+ajuste_coluna, y=y-27-15-20-aux_extra_linha, text=preco_produto)

    ajuste_linha = 33

    for i in range(qtd_linhas):

        for j in range(qtd_colunas):
            rodar2(ajuste_linha)

            ajuste_coluna += 192
        
        ajuste_coluna = 0

        ajuste_linha += 110
    
    pdf.save()

    def gerarQR():
        '''
        Esta função tem como objetivo gerar QR code.
        '''
        qr_code = qr.QrCodeWidget('conteudo')
        bounds = qr_code.getBounds()
        width = bounds[2] - bounds[0]
        height = bounds[3] - bounds[1]
        d = Drawing(45, 45, transform=[45./width,0,0,45./height,0,0])
        d.add(qr_code)
        renderPDF.draw(d, pdf, 15, 405)
 
if __name__ == "__main__":
    gerarCodigo("17892413450", qtd_linhas=7, qtd_colunas=3)