#coding: utf-8

# importando módulo tk inter e chamamos o pacote com tk (apelido)
import tkinter as tk

# criar uma variável, janela principal do programa.
# tk = apelido da biblioteca tkinter e Tk nome da classe que estamos fazendo
janela = tk.Tk()

# atribuind nome para a janela
janela.title('Janela Principal')

# mexendo na cor de fundo podemos usar bg ou background
janela['bg'] = 'green'

# definindo tamanho e local de criação da janela na tela do computador
# LxA+E+T ou seja => 300x300+100+100; podemos também usar somente LxA ou +E+T
# largura da janela= L
# por = x
# altura da janela= A
# definir instância = +
# esquerda = E
# topo = T
janela.geometry('800x300+100+100')

# executar programa e mostrar a tela principal
# enquanto a janela estiver sendo exibida não executará nada abaixo por isso é o mainloop ele sempre verifica as ações da janela
janela.mainloop()