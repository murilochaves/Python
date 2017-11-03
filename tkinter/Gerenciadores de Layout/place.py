#coding: utf-8

import tkinter as tk

janela = tk.Tk()

# onde label esta contido e texto exibido, tudo está atribuido em uma variavel lb (label)
lb = tk.Label(janela, text='Texto ebixido')

# usabdo gerenciador de layout place
lb.place(x=100, y=100)

# w x h + l + t
janela.geometry('300x300+200+200')

janela.mainloop()