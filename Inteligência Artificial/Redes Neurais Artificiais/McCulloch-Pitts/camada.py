#coding: utf-8

class Camada():
    
    def __init__(self, n_neuronios, modelo_neuronio):
        self.camada = [modelo_neuronio] * n_neuronios

    def saida(self, x):