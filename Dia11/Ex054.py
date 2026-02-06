#Site: https://codeforces.com/
# Desafio 405A - Virada por gravidade

'''O problema pede para simular o efeito de virar a gravidade em uma caixa com colunas de cubos.
Você recebe o número de colunas n e a quantidade de cubos em cada coluna.
Quando a gravidade é invertida, todos os cubos “caem” para a direita, fazendo com que as colunas 
fiquem ordenadas em ordem crescente.'''



n = int(input())
cubos = list(map(int, input().split()))
cubos.sort()
for i in cubos:
    print(i, end=" ")