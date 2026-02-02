# Desafio 1172: Substituição em Vetor I

'''Faça um programa que leia um vetor X[10]. Substitua a seguir, todos os valores nulos e negativos do vetor X por 1. 
Em seguida mostre o vetor X.'''

x = []
for _ in range(10): #como o número da repetição não sera utilizado para operações no programa, declaro _ como uma variável.
    num = int(input())
    if num <= 0:
        x += [1] #Uma forma de inserir valores em um vetor
    else:
        x.append(num) #outra forma de inserir valores em um vetor

for i in range(10):
    print(f"X[{i}] = {x[i]}")
