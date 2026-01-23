#Desafio 1071: Soma de Impares Consecutivos I

'''
Leia 2 valores inteiros X e Y. A seguir, calcule e mostre a soma dos números impares entre eles.
'''

x = int(input())
y = int(input())
soma = 0
if x > y: #Sempre começo o laço a partir do menor valor informado, que está armazenado em x
    x,y = y,x #Caso o usuário informe um valor maior no x e um menor no y, inverto os valores das variáveis
for i in range(x+1, y):
    if i % 2 == 1:
        soma += i

print(soma)