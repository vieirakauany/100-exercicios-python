#Desafio 1117: Validação de Nota

'''Faça um programa que leia as notas referentes às duas avaliações de um aluno. 
Calcule e imprima a média semestral. Faça com que o algoritmo só aceite notas válidas 
(uma nota válida deve pertencer ao intervalo [0,10]). Cada nota deve ser validada separadamente.'''

valido = False
soma = cont = 0
while valido == False:
    nota = float(input())
    if 0 <= nota <= 10:
        soma += nota
        cont += 1
        if cont == 2:
            valido = True
            media = soma / cont
    else:
        print("nota invalida")
print(f"media = {media:.2f}")