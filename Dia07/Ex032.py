#Desafio 1131: Grenais

'''O programa deve ler os gols do Inter e do Grêmio em vários Grenais.
Após cada jogo, perguntar se o usuário quer registrar outro (1-sim / 2-não).
Quando o usuário escolher 2, o programa mostra:

Quantos Grenais foram jogados;
Quantas vitórias teve o Inter;
Quantas vitórias teve o Grêmio;
Quantos empates houve;
E qual time venceu mais (ou "Não houve vencedor" em caso de empate).'''

cont = vi = vg = empate = 0
while True:
    pi, pg = map(int, input().split())
    cont += 1
    if pi > pg:
        vi += 1
    elif pg > pi:
        vg += 1
    else:
        empate += 1
    print("Novo grenal (1-sim 2-nao)")
    opcao = int(input())
    if opcao == 2:
        break

print(f'''{cont} grenais
Inter:{vi}
Gremio:{vg}
Empates:{empate}''')
if vi > vg:
    print("Inter venceu mais")
elif vg > vi:
    print("Gremio venceu mais")
else:
    print("Nao houve vencedor")
