from neuronio import McCullochPitts, get_conexao, separar_entrada, separar_saida
from dataset import tabelaNot

entrada = tabelaNot

x = separar_entrada(entrada)
t = separar_saida(entrada)

n_conexoes = get_conexao(x)

neuronio = McCullochPitts(n_conexoes)
neuronio.set_limiar(0)
neuronio.set_w(-1, 0)

neuronio.soma(x, t)