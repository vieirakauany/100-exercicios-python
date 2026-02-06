#Site: https://codeforces.com/
# Desafio 231A - Team
'''Três amigos decidem resolver problemas de programação. Para cada problema, 
se pelo menos dois deles tiverem certeza da solução, 
eles a implementam. O objetivo é contar quantos problemas serão resolvidos.'''

n = int(input())
quant_pro = 0
for _ in range(n):
    palpites = list(map(int, input().split()))
    cont = palpites.count(1)
    if cont >= 2:
        quant_pro += 1
print(quant_pro)