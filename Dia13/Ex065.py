
'''Escreva um algoritmo que leia um inteiro N (0 ≤ N ≤ 100), correspondente a ordem de uma matriz M de inteiros, 
e construa a matriz de acordo com o exemplo abaixo.'''

""" Lógica geral:
A matriz é construída com base na distância entre as posições (i, j) e a diagonal principal.
O 1 sempre aparece na diagonal principal (onde i == j).
Os números aumentam 1 a cada passo que se afasta da diagonal principal, tanto para a direita quanto para a esquerda.
Se i e j são diferentes, o valor cresce de acordo com o valor absoluto da distância entre eles.
"""

while True:
    n = int(input())
    if n == 0:
        break
    for i in range(n):
        linha = []
        for j in range(n):
            valor = abs(i-j) + 1
            linha += [f"{valor:3}"]
        print(" ".join(linha))
    print()