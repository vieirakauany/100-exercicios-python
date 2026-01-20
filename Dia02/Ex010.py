#Desafio 1009: Salário com Bônus


'''Faça um programa que leia o nome de um vendedor, o seu salário fixo e o total de vendas efetuadas por ele no mês(em dinheiro). 
Sabendo que este vendedor ganha 15% de comissão sobre suas vendas efetuadas, informar o total a receber no final do mês, 
com duas casas decimais.'''

nome = input().strip() # a função input já e do tipo str e o comando strip remove espaços no ínicio e final do tetxo.
salario = float(input())
valor_vendas = float(input())
salario_final =  salario + (0.15 * valor_vendas)
print(f"TOTAL = R$ {salario_final:.2f}")