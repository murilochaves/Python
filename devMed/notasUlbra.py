# Composicaoo de notas da minha faculdade - mudarei posteriormente para orientacao a objetos
G1 = 5.0
PPG1 = 2.0
MensalG1 = 2.0
SemiPresencialG1 = 1.0

G2 = 5.0
PPG2 = 2.0
Transversal = 1.0
MensalG2 = 1.0
SemiPresencialG2 = 1.0

notaG1 = G1 + PPG1 + MensalG1 + SemiPresencialG1
notaG2 = G2 + PPG2 + MensalG2 + SemiPresencialG2 + Transversal

grauFinal = ((notaG1 + notaG2 * 2) / 3)

if (grauFinal >= 6):
    print('Media Final: %.1f - APROVADO' % grauFinal)
elif (grauFinal >= 4) and (grauFinal <= 6):
    print('Media Final: %.1f - SUBSTITUTIVA' % grauFinal)
else:
    print('Media Final: %.1f - Reprovado' % grauFinal)