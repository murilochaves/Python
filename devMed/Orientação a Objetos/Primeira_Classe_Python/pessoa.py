class Pessoa:
    # construtor padrão
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    # métodos get e set
    def getNome(self):
        return self.nome

    def getIdade(self):
        return self.idade

    def setNome(self, nome):
        self.nome = nome
    
    def setIdade(self, idade):
        self.idade = idade