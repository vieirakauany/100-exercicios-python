# Desafio 1021 - Notas e Moedas

'''Leia um valor de ponto flutuante com duas casas decimais. Este valor representa um valor monetário. 
A seguir, calcule o menor número de notas e moedas possíveis no qual o valor pode ser decomposto. 
As notas consideradas são de 100, 50, 20, 10, 5, 2. As moedas possíveis são de 1, 0.50, 0.25, 0.10, 0.05 e 0.01. 
A seguir mostre a relação de notas necessárias.'''


cedulas = [100, 50, 20, 10, 5, 2, 1, 0.50, 0.25, 0.10, 0.05, 0.01]
n = float(input()) * 100  #Multiplicamos por 100 para remover as casas decimais e facilitar os cálculos.
print("NOTAS:")
palavra = "nota"
for i in cedulas:
    if i == 1:
        print("MOEDAS:")
        palavra = "moeda"
    cont = int(n //(i * 100) ) #Multiplicamos por 100 para remover as casas decimais e facilitar os cálculos.
    print(f"{cont} {palavra}(s) de R$ {i:.2f}")
    n -= cont * i * 100 #Multiplicamos por 100 para remover as casas decimais e facilitar os cálculos.
