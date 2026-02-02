# Desafio 1177: Preenchimento de Vetor II

'''Faça um programa que leia um valor T e preencha um vetor N[1000] com a sequência de valores de 0 até T-1 
repetidas vezes, conforme exemplo abaixo. Imprima o vetor N.'''

t = int(input())
a = 0
n = [i for i in range(t)] #Vetor com a sequência de valores
for i in range(1000):
    print(f"N[{i}] = {n[a]}") 
    a += 1
    if a == t:
        a = 0
    