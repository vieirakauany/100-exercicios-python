#Desafio 1153: Fatorial Simples

'''
Ler um valor N. Calcular e escrever seu respectivo fatorial. Fatorial de N = N * (N-1) * (N-2) * (N-3) * ... * 1.
'''


num = int(input())
fatorial = 1
for i in range(num, 0, -1):
    fatorial *= i
print(fatorial)