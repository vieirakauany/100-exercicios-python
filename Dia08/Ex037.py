# Desafio 1118: Várias Notas Com Validação

'''
O programa deve ler duas notas válidas (de 0 a 10), calcular a média e exibir o resultado.
Depois, deve perguntar se o usuário quer fazer um novo cálculo (1-sim / 2-não).

    Se digitar 1, repete o processo.
    Se digitar 2, o programa encerra.
    Qualquer outro valor deve ser rejeitado até o usuário digitar 1 ou 2.
'''

soma = cont = 0
while True:
    nota = float(input())
    if nota < 0 or nota > 10:
        print("nota invalida")
        continue #volta para o ínicio do laço, para ler um nova variável até que ela seja válida.
   
    soma += nota 
    cont += 1
    if cont == 2:
        media = soma / cont
        soma = cont =  0
        print(f"media = {media:.2f}")
        print("novo calculo (1-sim 2-nao)")
        resp = int(input())
        while resp not in [1, 2]: #verifica se resp é igual a 1 ou 2, se não ler um novo valor para ela.
            print("novo calculo (1-sim 2-nao)")
            resp = int(input())
        if resp == 2:
            break
   
    
    
