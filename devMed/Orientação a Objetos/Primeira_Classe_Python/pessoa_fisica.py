# importar classe pai do arquivo
from pessoa import Pessoa

# declarando a herança, criando classe filha em base a classe pai
class PessoaFisica(Pessoa):

    def __init__(self, CPF, nome, idade):
        # invocar o construtor da classe pai, aproveitando os atributos
        super().__init__(nome, idade)
        # atributos próprios da classe filha
        self.CPF = CPF

    # métodos get e set da classe filha
    def getCPF(self):
        return self.CPF

    def setCPF(self, CPF):
        self.CPF = CPF