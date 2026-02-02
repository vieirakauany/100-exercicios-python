#Desafio 1178: Preenchimento de Vetor III

'''Leia um valor X. Coloque este valor na primeira posição de um vetor N[100]. Em cada posição subsequente 
de N (1 até 99), coloque a metade do valor armazenado na posição anterior, conforme o exemplo abaixo. 
Imprima o vetor N.'''

x = float(input())
n = [x]
for i in range(100):
    print(f"N[{i}] = {n[i]:.4f}")
    n += [n[i] / 2]