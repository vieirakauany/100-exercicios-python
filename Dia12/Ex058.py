#Desafio 1183: Acima da Diagonal Principal

'''Leia um caractere maiúsculo, que indica uma operação que deve ser realizada e uma matriz M[12][12]. 
Em seguida, calcule e mostre a soma ou a média considerando somente aqueles elementos que estão acima da diagonal 
principal da matriz, conforme ilustrado abaixo (área verde).'''

t = input()
matriz = []
soma = cont = 0
for i in range(12):
    lista = []
    for j in range(12):
        num = float(input())
        if j > i: #Diagonal principal é dada quando os a posição i e j são igauis.
            soma += num
            cont += 1
        lista += [num]
    matriz += [lista]

if t == "S":
    print(f"{soma:.1f}")
else:
    media = soma / cont
    print(f"{media:.1f}")