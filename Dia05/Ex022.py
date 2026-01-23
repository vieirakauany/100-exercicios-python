#Deafio 1064:Positivos e Média

'''Leia 6 valores. Em seguida, mostre quantos destes valores digitados foram positivos. Na próxima linha, 
deve-se mostrar a média de todos os valores positivos digitados, com um dígito após o ponto decimal.'''


positivos = quant_positivos = 0
for _ in range(6):
    num = float(input())
    if num >= 0:
        positivos += num
        quant_positivos += 1

media = positivos / quant_positivos
print(f"{quant_positivos} valores positivos")
print(f"{media:.1f}")
 