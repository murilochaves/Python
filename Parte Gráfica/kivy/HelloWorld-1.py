#coding: utf-8

import kivy # importando o kivy propriamente dito
from kivy.app import App # essa classe kivy.app controla todo o ciclo de vida da aplicação
from kivy.uix.label import Label # elementos que compões a aplicação, estão em kivy.uix

kivy.require('1.9.1')

class PrimeiroApp(App):
    def build(self): # constroi o elemento raiz da aplicação
        return Label(text='Hello World, Kivy!') # criando um elemento do tipo label com o valor setado

if __name__ == '__main__':
    PrimeiroApp().run() # ponto inicial do programa, quando essa linha é executada, a aplicação entra em execução