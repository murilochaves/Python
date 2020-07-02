#include <stdio.h>

/*
URI Online Judge | 1012
Área

Escreva um programa que leia três valores com ponto flutuante de dupla precisão: A, B e C. Em seguida, calcule e mostre: 
a) a área do triângulo retângulo que tem A por base e C por altura. 
b) a área do círculo de raio C. (pi = 3.14159) 
c) a área do trapézio que tem A e B por bases e C por altura. 
d) a área do quadrado que tem lado B. 
e) a área do retângulo que tem lados A e B. 

Entrada

O arquivo de entrada contém três valores com um dígito após o ponto decimal.

Saída

O arquivo de saída deverá conter 5 linhas de dados. Cada linha corresponde a uma das áreas descritas acima, sempre com mensagem correspondente e um espaço entre os dois pontos e o valor. O valor calculado deve ser apresentado com 3 dígitos após o ponto decimal.
*/

int main() {
	double a, b, c, triangulo, circulo, trapezio, quadrado, retangulo;
    const double pi=3.14159;

    scanf("%lf %lf %lf", &a, &b, &c);

    // A por base e C por altura
    triangulo = (a*c) / 2;
    circulo = pi * ((c) * (c));
    trapezio = ((a + b) / 2) * c; 
    quadrado = b * b;
    retangulo = a * b;
	
    printf("TRIANGULO: %.3lf\n", triangulo);
    printf("CIRCULO: %.3lf\n", circulo);
    printf("TRAPEZIO: %.3lf\n", trapezio);
    printf("QUADRADO: %.3lf\n", quadrado);
    printf("RETANGULO: %.3lf\n", retangulo);
	
    return 0;
}
