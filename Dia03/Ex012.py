#Deafio 1036: Fórmula de Bhaskara

'''Leia 3 valores de ponto flutuante e efetue o cálculo das raízes da equação de Bhaskara. 
Se não for possível calcular as raízes, mostre a mensagem correspondente “Impossivel calcular”, 
caso haja uma divisão por 0 ou raiz de numero negativo.'''

from math import sqrt

a, b, c = map(float, input().split())
if a == 0 or b**2 < 4*a*c:
    print("Impossivel calcular")
else:
    delta = b ** 2 - 4 * a * c
    raiz1 = (-b + sqrt(delta)) / (2 * a)
    raiz2 = (-b - sqrt(delta)) /(2 * a)
    print(f"R1 = {raiz1:.5f}")
    print(f"R2 = {raiz2:.5f}")