#Desafio 1049: Aumento de Salário 

'''A empresa ABC resolveu conceder um aumento de salários a seus funcionários de acordo com a tabela abaixo:
        Salário	       | Percentual de Reajuste
    0 - 400.00         | 15%
    400.01 - 800.00    | 12%
    800.01 - 1200.00   | 10%
    1200.01 - 2000.00  | 7%
    Acima de 2000.00   | 4%

Leia o salário do funcionário e calcule e mostre o novo salário, 
bem como o valor de reajuste ganho e o índice reajustado, em percentual.'''

salario = float(input())
if salario <= 400:
    percentual = 15
    reajuste = salario * (percentual/100)
    novo_salario = salario + reajuste
elif 400 < salario <= 800:
    percentual = 12
    reajuste = salario * (percentual/100)
    novo_salario = salario + reajuste
elif 800 < salario <= 1200:
    percentual = 10
    reajuste = salario * (percentual/100)
    novo_salario = salario + reajuste
elif 1200 < salario <= 2000:
    percentual = 7
    reajuste = salario * (percentual/100)
    novo_salario = salario + reajuste
else:
    percentual = 4
    reajuste = salario * (percentual/100)
    novo_salario = salario + reajuste

print(f"Novo salario: {novo_salario:.2f}")
print(f"Reajuste ganho: {reajuste:.2f}")
print(f"Em percentual: {percentual} %")
