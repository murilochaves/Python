#coding: utf-8

class Semestre(object):

    def __init__(self, nome_semestre, referencia_semestre, inicio_semestre, fim_semestre):
        self.nome_semestre = nome_semestre
        self.referencia_semestre = referencia_semestre
        self.inicio_semestre = inicio_semestre
        self.fim_semestre = fim_semestre
        print '\nSemestre:\n' + self.nome_semestre + ' (' + self.referencia_semestre + ')' + ' criado com sucesso!'
        print 'Data início:', self.inicio_semestre
        print 'Data final:', self.fim_semestre, '\n'

###########
## Teste ##
###########

#semestre_1 = Semestre('Oitavo Período', '1', '2')