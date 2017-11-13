#coding: utf-8

class Semestre(object):

    # Esta classe visa ter o objetivo de organizar e separar as diversas matérias que terão neste período
    
    # ao utilizar esta classe, é gerado um arquivo semestre.pyc que é uma comilação do código interpretado

    # construtor que passo as informações básicas que acredito serem pertinentes.
    # Gostaria de adaptar uma sobrecarga de construtores futuramente
    def __init__(self, nome_semestre, referencia_semestre, inicio_semestre, fim_semestre):
        self.nome_semestre = nome_semestre
        self.referencia_semestre = referencia_semestre
        self.inicio_semestre = inicio_semestre
        self.fim_semestre = fim_semestre
        print '\nSemestre:\n' + self.nome_semestre + ' (' + self.referencia_semestre + ')' + ' criado com sucesso!'
        print 'Data início:', self.inicio_semestre
        print 'Data final:', self.fim_semestre, '\n'

    # Não sei se em python utilizamos Getters e Setters, mais por via das dúvidas até me adaptar, realizei isto
    
    # GETTERS
    def get_nome_semestre(self):
        return self.nome_semestre
    
    def get_referencia_semestre(self):
        return self.referencia_semestre

    def get_inicio_semestre(self):
        return self.inicio_semestre

    def get_fim_semestre(self):
        return self.fim_semestre

    # SETTERS
    def set_nome_semestre(self, nome_semestre):
        self.nome_semestre = nome_semestre

    def set_referencia_semestre(self, referencia_semestre):
        self.referencia_semestre = referencia_semestre

    def set_inicio_semestre(self, inicio_semestre):
        self.inicio_semestre = inicio_semestre

    def set_fim_semestre(self, fim_semestre):
        self.fim_semestre = fim_semestre


###########
## Teste ##
###########

#semestre_1 = Semestre('Oitavo Período', '1', '2')