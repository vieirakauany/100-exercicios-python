#Desafio 1046: Tempo de Jogo

'''Leia a hora inicial e a hora final de um jogo. 
A seguir calcule a duração do jogo, sabendo que o mesmo pode começar em um dia e terminar em outro, 
tendo uma duração mínima de 1 hora e máxima de 24 horas.'''


tempoi, tempof = map(int, input().split())
tempo_duracao = tempof - tempoi
if tempo_duracao <= 0: # Se começar em um dia e terminar em outro dia a duração da negativa ou zero precisando dessa compensação de 24 horas
    tempo_duracao += 24
print(f"O JOGO DUROU {tempo_duracao} HORA(S)")
