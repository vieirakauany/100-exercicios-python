#Desafio 1012: Área

'''Escreva um programa que leia três valores com ponto flutuante de dupla precisão: A, B e C. 
Em seguida, calcule e mostre:
a) a área do triângulo retângulo que tem A por base e C por altura.
b) a área do círculo de raio C. (pi = 3.14159)
c) a área do trapézio que tem A e B por bases e C por altura.
d) a área do quadrado que tem lado B.
e) a área do retângulo que tem lados A e B.'''


a , b , c = map(float, input().split())

tri = a * c / 2
cir = 3.14159 * c ** 2
tra =  (a + b) * c / 2
qua = b ** 2
ret = a * b
print(f'''TRIANGULO: {tri:.3f}
CIRCULO: {cir:.3f}
TRAPEZIO: {tra:.3f}
QUADRADO: {qua:.3f}
RETANGULO: {ret:.3f}''')
#As três aspas permite um print com  várias linhas.
#.3f => é uma formatação de valor em que o número é printado com 3 casas decimais (3f) depois da vírgula (ponto .)