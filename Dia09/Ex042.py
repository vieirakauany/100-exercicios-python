#Desafio 1173: Preenchimento de Vetor I

'''Leia um valor e faça um programa que coloque o valor lido na primeira posição de um vetor N[10]. 
Em cada posição subsequente, coloque o dobro do valor da posição anterior. 
Por exemplo, se o valor lido for 1, os valores do vetor devem ser 1,2,4,8 e assim sucessivamente. 
Mostre o vetor em seguida.
'''

num = int(input())
vetor = []
for _ in range(10):
    vetor += [num]
    num = num * 2

for i in range(10):
    print(f"N[{i}] = {vetor[i]}")