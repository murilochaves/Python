#include <stdio.h>

/*
URI Online Judge | 1038
Lanche

Com base na tabela abaixo, escreva um programa que leia o código de um item e a quantidade deste item. A seguir, calcule e mostre o valor da conta a pagar.

Entrada

O arquivo de entrada contém dois valores inteiros correspondentes ao código e à quantidade de um item conforme tabela acima.

Saída

O arquivo de saída deve conter a mensagem "Total: R$ " seguido pelo valor a ser pago, com 2 casas após o ponto decimal.
*/

int main() {
	int id, quantity;
    double total, items[5];

    items[0] = 4.00;
    items[1] = 4.50;
    items[2] = 5.00;
    items[3] = 2.00;
    items[4] = 1.50;

    scanf("%d %d", &id, &quantity);

    total = items[id-1] * quantity;

	
    printf("Total: R$ %.2lf\n", total);
	
    return 0;
}
