#include <stdio.h>
#include <stdlib.h>

/*
URI Online Judge | 1013
O Maior

Faça um programa que leia três valores e apresente o maior dos três valores lidos seguido da mensagem “eh o maior”. Utilize a fórmula:



Obs.: a fórmula apenas calcula o maior entre os dois primeiros (a e b). Um segundo passo, portanto é necessário para chegar no resultado esperado.

Entrada

O arquivo de entrada contém três valores inteiros.

Saída

Imprima o maior dos três valores seguido por um espaço e a mensagem "eh o maior".
*/

int maiorxy(a, b){
    return (a + b + abs(a - b)) / 2;
}

int main() {
	int a, b, c, maiorAB, maior;

    scanf("%d %d %d", &a, &b, &c);

    // verificando ab
    maiorAB = maiorxy(a, b);
    maior = maiorxy(maiorAB, c);
	
    printf("%d eh o maior\n", maior);
	
    return 0;
}
