#Desafio 1120 - Revisão de Contrato

'''o problema descreve uma situação em que um banco precisa corrigir contratos que foram impressos com um dígito 
incorreto em todos os valores. O programa deve ler o dígito errado e o número original, remover todas as ocorrências 
desse dígito e exibir o número corrigido, eliminando também possíveis zeros à esquerda. Caso o número resultante 
fique vazio ou valha zero, o programa deve imprimir apenas 0. A entrada termina quando ambos os valores forem zero.'''


while True:
    d, n = input().split() 
    if d == "0" and n == "0":
        break
    n = n.replace(d, "") #remove o dígito incorreto
    if n == "" or int(n) == 0: 
        print(0)
    else:
        print(int(n)) #evita zeros a esquerda
