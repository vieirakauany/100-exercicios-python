#Deafio 1019: Conversão de Tempo

'''Leia um valor inteiro, que é o tempo de duração em segundos de um determinado evento em uma fábrica, 
e informe-o expresso no formato horas:minutos:segundos.'''

tempo_seg = int(input())
tempo_hora = tempo_seg // 3600 
tempo_seg = tempo_seg % 3600
tempo_min = tempo_seg // 60
tempo_seg = tempo_seg % 60
#Começo descobrindo quantos segundos tem em uma hora depois faço uma relação em regra de três é hora = segundos // 3600
#Depois pego o tempo segundos e faço o resto de divisão por 3600 para decobrir quantos segundos ainda sobra para compor os minutos e segundo. E assim por diante.
# // => divisão exata, so pega os números antes da virgula
# % => módulo(resto) da divisão, por exemplo 2 % 2 = 0, 2 divido por 2 é 1 e resto é 0
print(f"{tempo_hora}:{tempo_min}:{tempo_seg}")