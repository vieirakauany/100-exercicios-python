# Desafio A. Lights Out (275A) - Codeforces

'''Você tem uma grade 3×3 de luzes, todas acesas no início.
Cada vez que uma luz é pressionada, ela e suas vizinhas diretas (cima, baixo, esquerda e direita) mudam de estado:
Se estava acesa (1) → apaga (0)
Se estava apagada (0) → acende (1)
Dada a quantidade de vezes que cada luz foi pressionada,
Seu objetivo é determinar o estado final (acesa ou apagada) de cada luz.'''


ligado = [[1, 1, 1], [1, 1, 1], [1,1,1]] #Criação da matriz inicial com todas as luzes acessas(1)
direcoes = [(0,0), (-1, 0), (1, 0), (0, -1), (0,1)] #Definição dos valores de operações de índices para acesso de posições vizinhas e própria celula. Explicação melhor em aprendizados.md
for i in range(3):
    linha = list(map(int, input().split())) #Leitura de cada linha que corresponde a quantas vezes uma determinada luz foi pressionada.
    for j in range(3):
        if linha[j] % 2 == 1: #Verifico se a quantidade de vezes pressionada é ímpar, pois isso indica que ocorreu uma alteração, ja que, ao apertar uma luz em vezes pares cancela o efeito (1ª muda, 2ª volta ao original),
            for dx, dy in direcoes: 
                ci , cj = i + dx, j + dy #Calculo a posição das celulas vizinhas e da própria
                if 0 <= ci < 3 and 0 <= cj < 3: #Verifico se essas posições existem
                    ligado[ci][cj] = 1 - ligado[ci][cj] #Altero o estado, sendo q se ela está desligada será ligada e vice-versa. Então 1-0 = 1 e 1-1=0.

for linha in ligado:
    print(''.join(map(str, linha))) #Transforma cada linha da matriz em um texto sem espaço pela função .join().
