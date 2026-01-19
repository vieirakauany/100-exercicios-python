#Desafio 1015 : Distância entre dois pontos

'''
Você deve ler as coordenadas de dois pontos no plano cartesiano e calcular a 
distância entre eles usando a fórmula da distância.
distância = √(x2−x1)²+(y2−y1)²
​
'''
from math import sqrt

x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())
distancia = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
print(f"{distancia:.4f}")