#include <stdio.h>

/*
URI Online Judge | 1019
Conversão de Tempo

Leia um valor inteiro, que é o tempo de duração em segundos de um determinado evento em uma fábrica, e informe-o expresso no formato horas:minutos:segundos.

Entrada

O arquivo de entrada contém um valor inteiro N.

Saída

Imprima o tempo lido no arquivo de entrada (segundos), convertido para horas:minutos:segundos, conforme exemplo fornecido.
*/

int main() {
	int n, hours, minutes, seconds;

    scanf("%d", &n);

    hours = n / 3600;
    minutes = (n % 3600) / 60;
    seconds = (n % 3600) % 60;
	
    printf("%d:%d:%d\n", hours, minutes, seconds);
	
    return 0;
}
