#Desafio 1151: Fibonacci Fácil

'''A seguinte sequência de números 0 1 1 2 3 5 8 13 21... é conhecida como série de Fibonacci. 
Nessa sequência, cada número, depois dos 2 primeiros, é igual à soma dos 2 anteriores. 
Escreva um algoritmo que leia um inteiro N (N < 46) e mostre os N primeiros números dessa série.'''


n = int(input())
num = n - 2
n1 = cont = 0
n2 = 1
print("0 1 ", end='')
while cont < num:
    soma = n1 + n2
    if cont == num - 1:
        print(soma)
    else:
        print(soma, end=" ")
    n1 = n2
    n2 = soma
    cont += 1
