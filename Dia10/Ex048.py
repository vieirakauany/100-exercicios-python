#Desafio: 1179: Preenchimento de Vetor IV

'''Você deve ler 15 números inteiros e separá-los em dois vetores:

um para os pares
outro para os ímpares

Cada vetor tem tamanho máximo de 5 posições.

Quando um vetor encher (chegar a 5 valores), você deve imprimir seu conteúdo e esvaziá-lo para continuar preenchendo com os próximos números.
Após ler todos os 15 valores, imprima o que sobrou em cada vetor — primeiro os ímpares, depois os pares.

💡 Em resumo:
Ler 15 números → separar em pares e ímpares → imprimir cada vez que um vetor enche → ao final, imprimir o restante.'''


impar = []
par = []
for _ in range(15):
    num = int(input())
    if num % 2 == 0:
        par += [num]
        if len(par) == 5:
            for i in range(len(par)):
                print(f"par[{i}] = {par[i]}")
            par = []
    else:
        impar += [num]
        if len(impar) == 5:
            for i in range(len(impar)):
                print(f"impar[{i}] = {impar[i]}")
            impar = []

for i in range(len(impar)):
                print(f"impar[{i}] = {impar[i]}")

for i in range(len(par)):
                print(f"par[{i}] = {par[i]}")