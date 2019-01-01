x = open('notas1.txt')
cred = []
nota = []
sit = []
cr = 0
sumcred = 0
totcred = 237 #Total de créditos do curso.
aux = 0
for line in x:
    a = line.split(" ")
    cred += [int(a[0])]
    nota += [float(a[1])]
    sit += [(a[2])]
for i in cred:
    sumcred += sum([i]) #Calcula o somatório dos créditos cursados até o momento.
for i in range(len(nota)):
    if sit[i] == "aprovado\n" or "aprovado":
        aux += (cred[i]) #Calcula o somatório dos créditos nas matérias onde se obteve aprovação.
print(aux)
for i in range(len(cred)):
    cr += cred[i]*nota[i] #Faz a multiplicação da nota obtida em cada disciplina pela quantidade de créditos.
print("O seu coeficiente de rendimento acumulado (CR) é igual a:",(round((cr/sumcred),2)))
print("O percentual concluído até o momento é de:",(round(((aux/totcred)*100),2)),"%")