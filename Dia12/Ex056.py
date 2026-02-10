#Desafio 1182: Coluna na Matriz

'''Neste problema você deve ler um número que indica uma coluna de uma matriz na qual uma operação deve ser realizada, 
um caractere maiúsculo, indicando a operação que será realizada, e todos os elementos de uma matriz M[12][12]. 
Em seguida, calcule e mostre a soma ou a média dos elementos que estão na área verde da matriz, conforme for o caso. 
A imagem abaixo ilustra o caso da entrada do valor 5 para a coluna da matriz, demonstrando os elementos que deverão ser 
considerados na operação.
'''


col = int(input())
t = input()
soma = 0
matriz = []
for i in range(12):
    linha = []
    for j in range(12):
        num = float(input())
        if j == col:
            soma += num
        linha += [num]
    matriz += [linha]

if t == "S":
    print(f"{soma:.1f}")
else:
    media = soma / len(matriz)
    print(f"{media:.1f}")