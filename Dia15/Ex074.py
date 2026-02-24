#Desafio 1241: Encaixa ou Não II

'''Paulinho tem em suas mãos um novo problema. Agora a sua professora lhe pediu que construísse um programa para, 
à partir de dois valores muito grandes A e B, se B corresponde aos últimos dígitos de A.
'''

n = int(input())
for _ in range(n):
    a, b = input().split()
    if a[len(a)-len(b):] == b: #verifica se o final da string a é igual à string b
        print("encaixa")
    else:
        print("não encaixa")