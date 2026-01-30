#Desafio 1160: Crescimento Populacional

'''O programa deve ler vários casos de teste.
Para cada caso, são dadas: População inicial de A e B (A < B) e Taxas de crescimento anual de A e B (G1 > G2).
O programa calcula quantos anos A levará para ultrapassar B em população.
Se isso ocorrer em até 100 anos, mostra o número de anos.
Se levar mais de 100 anos, mostra: Mais de 1 seculo.'''

t = int(input())
for _ in range(t):
    pa, pb, g1, g2 = map(float , input().split())
    anos = 0
    seculo = False
    while pa <= pb:
        pa += int(pa * (g1/100))
        pb += int(pb * (g2/100))
        anos += 1
        if anos > 100:
           seculo = True
           break
    if seculo:
        print("Mais de 1 seculo.")
    else:
        print(f"{anos} anos.")