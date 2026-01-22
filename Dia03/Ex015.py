
'''Leia a hora inicial, minuto inicial, hora final e minuto final de um jogo. A seguir calcule a duração do jogo.

Obs: O jogo tem duração mínima de um (1) minuto e duração máxima de 24 horas.'''

#Explicação de algoritmos de conversão de tempo,como esse, no arquivo de aprendizados
hi, mi, hf, mf = map(int, input().split())
tempo_inical = hi * 60 + mi #calculo tempo inicial total em minutos
tempo_final = hf * 60 + mf #calculo tempo final total em minutos
tempo_total = tempo_final - tempo_inical #calculo quanto tempo durou o jogo
if tempo_total <= 0:
    tempo_total += 24 * 60 # Faço a compensação de um dia (24 horas em minutos) para jogos que começam em um dia e termina em outro
horat = tempo_total // 60 #Converto os minutos para horas
minut = tempo_total % 60 #Pego o restante dos minutos

print(f"O JOGO DUROU {horat} HORA(S) E {minut} MINUTO(S)")