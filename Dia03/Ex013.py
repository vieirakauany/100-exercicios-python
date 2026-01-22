#Desafio 1044: Múltiplos

'''Leia 2 valores inteiros (A e B). Após, o programa deve mostrar uma mensagem 
"Sao Multiplos" ou "Nao sao Multiplos", indicando se os valores lidos são múltiplos entre si.'''

a, b = map(int, input().split())
if a > b: #Esse teste serve para definir qual variável, sempre, vai guardar o valor maior
    a,b = b,a #Neste caso coloquei a variável b. Então se a = 30 e b = 2, com essa linha os valores vão ser invertidos com a = 2 e b = 30

if b % a == 0:
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")