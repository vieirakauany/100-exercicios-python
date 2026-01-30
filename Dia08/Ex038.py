#Desafio 1101: Sequência de Números e Soma 

'''Leia um conjunto não determinado de pares de valores M e N (parar quando algum dos valores for menor ou igual a zero).
 Para cada par lido, mostre a sequência do menor até o maior e a soma dos inteiros consecutivos entre eles (incluindo o 
 N e M).'''



m, n = map(int, input().split())
while m > 0 and n > 0:
    if m > n:
        m,n = n,m
    soma = 0
    for i in range(m, n+1):
        soma += i
        print(i, end=" ")
    print(f"Sum={soma}")

    m, n = map(int, input().split())
