#Desafio 1146: Sequências Crescentes

'''Este programa deve ler uma variável inteira X inúmeras vezes (deve parar quando o valor no arquivo de entrada for igual a zero). 
Para cada valor lido imprima a sequência de 1 até X, com um espaço entre cada número e seu sucessor.
Obs: cuide para não deixar espaço em branco após o último valor apresentado na linha ou você receberá Presentation Error.'''

while True:
    num = int(input())
    if num == 0:
        break
    for i in range(1, num):
        print(i, end=" ")
    print(num)