from neuronio import McCullochPitts, get_conexao, separar_entrada, separar_saida
from dataset import tabelaXor
from camada import Camada

entrada = tabelaXor

x = separar_entrada(entrada)
t = separar_saida(entrada)

n_conexoes = get_conexao(x)

camada = Camada(2, McCullochPitts(n_conexoes))

print(camada.camada)

# primeiro neurônio
z1 = camada.camada[0]

# segundo neurônio
z2 = camada.camada[1]

z1.set_limiar(2)
z1.set_w(2, 0)
z1.set_w(-1, 1)

z2.set_limiar(2)
z2.set_w(-1, 0)
z2.set_w(2, 1)

#print(z1.w, z2.w)

camada_saida = []

for i in range(len(camada.camada)):
    valor_saida = camada.camada[i].somatorio(x, t)
    camada_saida.append(valor_saida)

print(camada_saida)

#teste = []

#for i in range(len(camada_saida)):
    #aux = camada_saida[i][0]
    #teste.append(aux)
    #print(i)

#print(teste)

#neuronio_saida = McCullochPitts(2)
#neuronio_saida.set_w(2, 0)
#neuronio_saida.set_w(2, 1)
#neuronio_saida.set_limiar(2)

## AINDA NAO FINALIZADO