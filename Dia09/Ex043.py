#Desafio 1174: Seleçao em Vetor I

'''Faça um programa que leia um vetor A[100]. No final, mostre todas as posições do vetor que armazenam um valor menor 
ou igual a 10 e o valor armazenado em cada uma das posições.'''

a = []
for _ in range(100):
    num = float(input())
    a += [num]

for i in range(100):
    if a[i] <= 10:
        print(f"A[{i}] = {a[i]:.1f}")