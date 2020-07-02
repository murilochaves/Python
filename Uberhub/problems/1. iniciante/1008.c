#include <stdio.h>

/*
URI Online Judge | 1008
Salário

Entrada

O arquivo de entrada contém 2 números inteiros e 1 número com duas casas decimais, representando o número, quantidade de horas trabalhadas e o valor que o funcionário recebe por hora trabalhada, respectivamente.

Saída

Imprima o número e o salário do funcionário, conforme exemplo fornecido, com um espaço em branco antes e depois da igualdade. No caso do salário, também deve haver um espaço em branco após o $.
*/

int main() {
	int id, value;
    double hours, salary;

    scanf("%d %d %lf", &id, &value, &hours);

    salary = value * hours;
	
    printf("NUMBER = %d\n", id);
    printf("SALARY = U$ %.2lf\n", salary);
	
    return 0;
}
