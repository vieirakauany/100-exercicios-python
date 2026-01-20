#Desafio 1008: Salário 
'''leia o número de um funcionário, seu número de horas trabalhadas, 
o valor que recebe por hora e calcula o salário desse funcionário. 
A seguir, mostre o número e o salário do funcionário, com duas casas decimais.'''

cod_fun = int(input())
horas_trabalhadas = int(input())
valor_hora = float(input())
salario = horas_trabalhadas * valor_hora #Pyhton não necessita de uma conversão númerica entre int (inteiro) e float (reais) para fazer operações entre esses dois tipos.
print(f"NUMBER = {cod_fun}")
print(f"SALARY = U$ {salario:.2f}")
