#Desafio 1006: Média 2
#Leia três notas (A, B e C), calcule a média ponderada com pesos 2, 3 e 5, respectivamente.
# Considerando notas de 0 a 10 com uma casa decimal.

a = float(input())
b = float(input())
c = float(input())
media = (a*2 + b*3 + c*5) / 10
print(f"MEDIA = {media:.1f}")