#Desafio 1546: Feedback
'''O problema pede para criar um programa que classifique feedbacks enviados ao portal IRU e mostre qual membro da equipe será responsável por cada tipo.

As regras são:
1 → Rolien
2 → Naej
3 → Elehcim
4 → Odranoel

💡 Em resumo:Ler o tipo de feedback e exibir o nome do membro responsável correspondente.'''



responsaveis = ["Rolien", "Naej", "Elehcim", "Odranoel"]
n = int(input())
for _ in range(n):
    t = int(input())
    for _ in range(t):
        num = int(input())
        print(f"{responsaveis[num-1]}")