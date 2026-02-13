#Desafio 1534:  Matriz 123
'''Leia um valor inteiro N que é o tamanho da matriz que deve ser impressa conforme o modelo fornecido.'''
''' Lógica:
Diagonal principal:ocorre quando i == j; valor == 1
Diagonal secundária: ocorre quando i + j == N - 1; valor == 2
Todas as outras posições: valor == 3'''

while True:
    try:
        n = int(input())
        for i in range(n):
            linha = []
            for j in range(n):
                if i + j == n -1: #a ordem de teste aqui é importante pois caso a diagonal prinicpal == diagonal secundária o valor deve ser 2, eliminando todas as outras posições.
                    linha += ["2"]
                elif i == j:
                    linha += ["1"]
                else:
                    linha += ["3"]
            print("".join(linha))               
    except EOFError:
        break
