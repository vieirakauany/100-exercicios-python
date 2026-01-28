#Desafio 1155: Sequência S

'''Escreva um algoritmo para calcular e escrever o valor de S, sendo S dado pela fórmula:
S = 1 + 1/2 + 1/3 + … + 1/100'''

s = 1
div = 2
while True:
    s += 1/div
    if div == 100:
        break
    div += 1
print(f"{s:.2f}")