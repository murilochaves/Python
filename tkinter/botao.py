#coding: utf-8

import tkinter as tk

def bt_click():
    print ('bt_click')

    lb['text'] = 'Funcionou!'

janela = tk.Tk()

bt = tk.Button(janela, width=15, text='Ok', command=bt_click)
bt.place(x=50, y=100)

lb = tk.Label(janela, text='Teste')
lb.place(x=100, y=150)

janela.geometry('300x300+200+200')
janela.mainloop()