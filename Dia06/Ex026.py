#Desafio 1113: Crescente e Decrescente

'''Leia uma quantidade indeterminada de duplas de valores inteiros X e Y. 
Escreva para cada X e Y uma mensagem que indique se estes valores foram digitados em ordem crescente ou decrescente.'''

x, y = map(int, input().split())
while x != y:
    if x < y:
        print("Crescente")
    else:
        print("Decrescente")
    x, y = map(int, input().split())