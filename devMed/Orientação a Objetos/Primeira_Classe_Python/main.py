# para instanciar
from pessoa_fisica import PessoaFisica
from pessoa_juridica import PessoaJuridica

a = PessoaFisica('012.345.678-90', 'Alfredo', 22)

print('\n### Primeiro Objeto ###')
print('Nome: ', a.getNome(), ',', a.getIdade(), 'anos, CPF:', a.getCPF())

b = PessoaJuridica('01.234.567/0001-00', 'DevMed', 2)

print('\n### Segundo Objeto ###')
print('Empresa: ', b.getNome(), ',', b.getIdade(), 'anos, CNPJ:', b.getCNPJ())