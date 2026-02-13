#Desafio: Beautiful Matrix (263A)

'''No problema, você recebe uma matriz 5x5 contendo apenas zeros e um único número 1.Seu objetivo é descobrir 
quantos movimentos são necessários para mover o número 1 até o centro da matriz (posição [3][3])'''

matriz = []
for i in range(5):
    linha = list(map(int, input().split()[:5]))
    matriz += [linha]
    for j in range(5):
        if matriz[i][j] == 1:
            valor_min = abs(2 - i) + abs(2 - j) 
print(valor_min)