#Desafio 1273: Justificador

'''pede para ler várias palavras e exibi-las alinhadas à direita, com base na maior palavra do conjunto. 
O programa deve processar vários casos de teste, cada um com um número N de palavras, e imprimir as palavras 
justificadas, deixando uma linha em branco entre cada conjunto, mas sem linha extra ao final da saída.'''


resultados = []
while True:
    n = int(input())
    if n == 0:
        break

    maior = 0
    palavras = []

    for _ in range(n):
        palavra = input()
        if len(palavra) > maior:
            maior = len(palavra)
        palavras += [palavra]
    
    bloco = "\n".join(f"{p:>{maior}}" for p in palavras)
    resultados.append(bloco)

# imprime tudo separado por uma linha em branco
print("\n\n".join(resultados))
