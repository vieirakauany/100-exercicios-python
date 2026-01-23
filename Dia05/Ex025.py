#Desafio 1143: Quadrado e ao Cubo

'''
Escreva um programa que leia um valor inteiro N (1 < N < 1000). 
Este N é a quantidade de linhas de saída que serão apresentadas na execução do programa.

Exemplo de Entrada	Exemplo de Saída
5

1 1 1
2 4 8
3 9 27
4 16 64
5 25 125
'''

num = int(input())
print("1 1 1")  # Imprime o primeiro termo fixo da sequência (1, 1², 1³)
for i in range(2, num+1): # Percorre de 2 até o número informado
    print(i, i**2, i**3) # Imprime o número, seu quadrado e seu cubo