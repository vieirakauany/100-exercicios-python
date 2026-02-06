#Desafio 1018: Cédulas

'''Leia um valor inteiro. A seguir, calcule o menor número de notas possíveis (cédulas) no qual o valor pode ser 
decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2 e 1. A seguir mostre o valor lido e a relação de notas 
necessárias.'''

cedulas = [100, 50, 20, 10, 5, 2, 1]
num = int(input())
print(num)
for i in cedulas: #Percorre diretamente cada valor do vetor cedulas
    cont = num // i
    num -= cont * i
    print(f"{cont} nota(s) de R$ {i},00")