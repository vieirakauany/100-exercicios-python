#Desafio 1020: Idade em Dias

'''Leia um valor inteiro correspondente à idade de uma pessoa em dias e informe-a em anos, meses e dias.
Todo ano com 365 dias e todo mês com 30 dias'''

#Mesma lógica do exercício 7

dias = int(input())
ano = dias // 365
dias = dias % 365
mes = dias // 30
dias = dias % 30
print(f"{ano} ano(s)")
print(f"{mes} mes(es)")
print(f"{dias} dia(s)")