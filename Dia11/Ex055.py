
'''Dado um vetor com as alturas dos soldados, encontre a posição do maior e do menor, e calcule o número mínimo de 
trocas necessárias para colocar o maior no início e o menor no fim da fila.'''

n = int(input())
soldados = list(map(int, input().split()[:n]))
menor = pos = 0
indice_maior = soldados.index(max(soldados)) # o índice do mais alto → o primeiro que aparece, se houver empates
for i in range(n-1, -1, -1):
    if i == n-1 or soldados[i] < menor:
        menor = soldados[i]
        indice_menor = i #o índice do mais baixo → o último que aparece, se houver empates, por isso faço um for invertido para encontrar o último menor valor

segundos = indice_maior + (n-1 - indice_menor) #Quanto o maior_indice preciso "andar" para chegar no ínicio da fila([0]) + quanto o menor_indice precisou se mover para chegar no último lugar da fila([n-1])
if indice_maior > indice_menor: #Se o mais baixo está à esquerda do mais alto, ao mover o mais alto para o início, o mais baixo será deslocado uma posição para a esquerda, então você precisa subtrair 1 movimento.
    segundos -= 1

print(segundos)