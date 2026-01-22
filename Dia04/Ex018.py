# Deafio 1051: Imposto de Renda

'''No país imaginário Lisarb, os habitantes pagam impostos conforme a renda, de forma justa e sem corrupção. 
O programa deve ler o salário de uma pessoa e calcular quanto ela deve pagar de imposto de renda, 
segundo as faixas da tabela. Apenas a parte do salário que ultrapassa cada faixa é tributada.

    Renda (R$)                  | Imposto de Renda
    ----------------------------|-----------------
    de 0.00 até 2000.00         | Isento
    de 2000.01 até 3000.00      | 8%
    de 3000.01 até 4500.00      | 18%
    acima de 4500.00            | 28%
'''

salario = float(input())
imposto = 0

if salario <= 2000:
    print("Isento")
else:
    if salario > 4500:
        imposto += (salario - 4500) * 0.28  # Calcula 28% apenas sobre a parte do salário que ultrapassa R$ 4500
        salario -= salario - 4500 # Atualiza o salário, removendo a parte já tributada, para calcular as faixas anteriores
        # O mesmo raciocínio é aplicado nas outras faixas de imposto, 
        # exceto na faixa até R$ 2000, que é isenta de tributação.
        
    if salario > 3000:
        imposto += (salario - 3000) * 0.18
        salario -= salario - 3000

    if salario > 2000:
        imposto += (salario - 2000) * 0.08
    
    print(f"R$ {imposto:.2f}")
