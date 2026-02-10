#Desafio 1187: Área Superior

'''Leia um caractere maiúsculo, que indica uma operação que deve ser realizada e 
uma matriz M[12][12]. Em seguida, calcule e mostre a soma ou a média considerando 
somente aqueles elementos que estão na área superior da matriz, conforme ilustrado 
abaixo (área verde).
'''

t = input()
soma = cont = 0
for i in range(12):
    for j in range(12):
        num = float(input())
        if j > i and i + j < 11:
            soma += num
            cont += 1

if t == "S":
    print(f"{soma:.1f}")
else:
    media = soma / cont
    print(f"{media:.1f}")