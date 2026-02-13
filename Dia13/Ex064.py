#Desafio 1435: Matriz Quadrada I

'''Escreva um algoritmo que leia um inteiro N (0 ≤ N ≤ 100), correspondente a ordem de uma matriz M de inteiros, 
e construa a matriz de acordo com o exemplo abaixo.'''

""" Lógica geral:
Cada posição (i, j) da matriz depende da menor distância até as bordas.

Imagine que os índices vão de 0 a N-1.
Para um elemento da matriz na posição (i, j):
Distância até a borda superior: i
Distância até a borda esquerda: j
Distância até a borda inferior: N - 1 - i
Distância até a borda direita: N - 1 - j
O menor desses quatro valores indica em qual camada o número está."""

while True:
    n = int(input())
    if n == 0:
        break
    for i in range(n):
        linha = []
        for j in range(n):
            valor = min(i,j,(n-1-i), (n-1-j)) + 1
            linha += [f"{valor:3}"] #Armazena cada valor com 3 espaços vazios
        print(" ".join(linha))
    print()