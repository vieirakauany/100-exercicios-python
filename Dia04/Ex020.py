#Desafio 1040: Média 3

'''
O programa lê quatro notas (N1, N2, N3, N4) com pesos 2, 3, 4 e 1, calcula a média ponderada e mostra o resultado.
    Se a média ≥ 7.0 → Aluno aprovado.
    Se a média < 5.0 → Aluno reprovado.
    Se 5.0 ≤ média ≤ 6.9 → Aluno em exame.
Nesse caso, o programa lê a nota do exame, mostra-a, recalcula a nova média:
    Se média final ≥ 5.0 → Aluno aprovado.
    Caso contrário → Aluno reprovado.
Por fim, exibe “Media final:” com o valor obtido.
'''


n1, n2, n3, n4 = map(float, input().split())
media = (n1 * 2 + n2 * 3 + n3 * 4 + n4 * 1) / 10
print(f"Media: {media:.1f}")

if media >= 7:
    print("Aluno aprovado.")
elif media < 5:
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")
    nota_exame = float(input())
    print(f"Nota exame: {nota_exame:.1f}")
    nova_media = (media + nota_exame) / 2
    if nova_media > 5:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print(f"Media final: {nova_media:.1f}")