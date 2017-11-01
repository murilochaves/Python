### Informações

Este programa será escrito em python para verificar plágio em atividades e códigos.

O mesmo representará a seguinte função:

- **Código**
```
MCOD = α × (COD1 + 2 × COD2 + 2 × COD3) / 5
```

- **Atividades**
```
MATI = α × (ATI1 + 2 × ATI2 + 2 × ATI3) / 5
```

- **Média Final**
```
MFIN = α × (MCOD + 2 × MATI) / 3
```

- **Condição**
```
se MCOD ≥ 5 e MATI ≥ 5
    MFIN = α × (MCOD + 2 × MATI) / 3
senao
    se MFIN ≥ 5
        aprovado
    se 3 ≤ MFIN < 5
        substitutiva
    se MFIN < 3
        reprovado
```

**α** = representa a conduta ética (inicia com 1 no início do semestre e em cada ocorrência de plágio, haverá uma redução de pelo menos 0,3 na sua nota α, podendo chegar a 0)