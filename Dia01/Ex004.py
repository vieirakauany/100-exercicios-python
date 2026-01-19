#Desafio 1010: Cálculo Simples

'''Leia o código, a quantidade e o valor unitário de duas peças diferentes. 
Em seguida, calcule e mostre o valor total a pagar.'''

cod1, num1, valor1 = map(float, input().split()) #estrutura map explicada em aprendizados
cod2, num2, valor2 = map(float, input().split())
valor_Total = num1 * valor1 + num2 * valor2 # multiplico a quantidade de peças pelo seu valor unitário e somo as duas peças. 
print(f"VALOR A PAGAR: R$ {valor_Total:.2f}")