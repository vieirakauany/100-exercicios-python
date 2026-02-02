#Desafio 1180: Menor e Posição

'''Faça um programa que leia um valor N. Este N será o tamanho de um vetor X[N]. 
A seguir, leia cada um dos valores de X, encontre o menor elemento deste vetor e a sua posição dentro do vetor, 
mostrando esta informação.'''

n = int(input())
x = list(map(int, input().split()[:n]))
# menor = min(x) 
# pos = x.index(menor) 
#As funções min e index fazem, respectivamente, a seleção do menor valor informado e a posição em que esse valor está armazenado.
menor = pos = 0
for i in range(n):
    if i == 0 or x[i] < menor:
        menor = x[i]
        pos = i

print(f"Menor valor: {menor}")
print(f"Posicao: {pos}")