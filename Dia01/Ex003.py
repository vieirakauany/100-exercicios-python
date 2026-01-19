# Desafio 1017: Gasto de Combustível

'''Calcule quantos litros de combustível Joãozinho gastou em uma viagem, sabendo que o carro faz 12 km/L. 
O programa deve usar o tempo da viagem (horas) e a velocidade média (km/h) para calcular a distância e o consumo, 
exibindo o resultado com três casas decimais.'''

tempo = int(input())
velocidade_media = int(input()) 
distancia = velocidade_media * tempo # adaptação da fórmual de velocidade média (Vm = S/T ) para descobrir a distância percorrida
quant_litros =  distancia / 12 #uso da regra de três para relacionar 12km/L com a distância dada.
print(f"{quant_litros:.3f}")