#include <stdio.h>

/*
URI Online Judge | 3043
Festa Junina


Conforme a tradição da sua escola, os alunos do último ano do ensino médio organizarão uma festa junina no colégio. Porém, o diretor da escola tem tido problemas nos últimos anos com a organização desta festa, e ele percebeu que a causa destes problemas é a presença de alunos que não se toleram na comissão organizadora. Assim, neste ano, o diretor resolveu que ele mesmo designaria a comissão organizadora da festa junina, de forma que não haja inimizades entre os membros da comissão. Para isto, o diretor distribuiu um formulário a todos alunos da turma; cada aluno deve listar os alunos com os quais ele não gostaria de participar da comissão organizadora. A partir destas informações, o diretor deseja montar uma comissão organizadora para a festa com o maior número possível de alunos, de forma a não sobrecarregar os seus integrantes.

Dadas as informações retiradas dos formulários de todos os alunos, sua tarefa é determinar qual o número máximo de alunos que a comissão organizadora pode ter.

Entrada

A entrada é composta de vários conjuntos de teste. A primeira linha de um conjunto de teste contém um número inteiro N, que indica o número de alunos na turma (N 20). Os alunos são identificados seqüencialmente pelos números de 1 a N. A seguir, para cada um dos N 0 ≤ N ≤ 20 (N = 0 apenas para indicar o fim da entrada) alunos, seguindo a ordem dos números de identificação, há uma linha contendo a lista dos alunos com os quais este aluno não gostaria de participar na comissão organizadora. O final de uma lista é indicado pelo número zero, e o final da entrada é indicado por um conjunto de teste com N = 0.

 

Saída

Para cada conjunto de teste da entrada seu programa deve produzir três linhas na saída. A primeira linha deve conter um identificador do conjunto de teste, no formato “Teste n”, onde n é numerado seqüencialmente a partir de 1. A segunda linha deve conter o número máximo de alunos que podem participar em uma mesma comissão organizadora, conforme calculado pelo seu programa.
*/

void print_matrix(matrix, lines) {
    for (int *i=0; *i < lines; i++) {
        printf("%d", matrix[i]);
    }
}

int main() {
	int n, teste=1, max_combination;

    // primeira coleta
    scanf("%d", &n);

    // N = 0
    while (n != 0) {
        int alunos[n][20];

        // 0 < N <= 20 
        if (n > 0 && n <=20) {

            for (int i=0; i < n; i++) {
                scanf("%d", &alunos[i][n]);
            };
            
            printf("\n");
            print_matrix(alunos, n);
            
            
        } else {
            return 0;
        };

        printf("Teste %d\n", teste);

        teste += 1;
        scanf("%d", &n);
    };
	
    return 0;
}
