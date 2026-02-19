#Desafio 1253 - Cifra de César

'''Júlio César usava um sistema de criptografia, agora conhecido como Cifra de César, que trocava cada letra pelo 
equivalente em duas posições adiante no alfabeto (por exemplo, 'A' vira 'C', 'R' vira 'T', etc.). 
Ao final do alfabeto nós voltamos para o começo, isto é 'Y' vira 'A'. Nós podemos, é claro, tentar trocar as 
letras com quaisquer número de posições.'''


alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
n = int(input())
for _ in range(n):
    codificada = input()
    deslocamento = int(input())
    decodificado = ""
    for i in codificada:
        pos = alfabeto.index(i) - deslocamento
        decodificado += alfabeto[pos]
        #As duas linhas acima poderiam ser substituidas por: nova_letra = chr(ord(i) + deslocamento)
        #A função old() transformaria um caractere da palvra em número, que seria somado com o deslocamento. E a função chr() transformaria esse valor no caractere equivalente.
    print(decodificado)
        
