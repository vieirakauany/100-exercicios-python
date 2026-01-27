
'''Faça um algoritmo para ler um número indeterminado de dados, contendo cada um, a idade de um indivíduo. 
O último dado, que não entrará nos cálculos, contém o valor de idade negativa. 
Calcular e imprimir a idade média deste grupo de indivíduos.'''

idade = int(input())
soma = cont = 0
while idade >= 0:
    soma += idade
    cont += 1
    idade = int(input())

media = soma / cont
print(f"{media:.2f}")