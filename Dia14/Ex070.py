#Desafio 1235: De Dentro para Fora

'''Uma impressora com vírus está imprimindo as linhas de forma invertida: a metade esquerda é impressa do meio 
para a esquerda e a metade direita da direita para o meio. Dada uma frase embaralhada dessa forma, é preciso 
reconstruir a frase original.'''

n = int(input())
for _ in range(n):
    frase = input()
    decifrado = ""
    metade  = len(frase) // 2
    pl1 = frase[:metade] #Armazeno a primeira metade da frase
    pl2 = frase[metade:] #Armazeno a segunda metade da frase

    # Percorre a primeira metade de trás para frente, reconstruindo a parte inicial da frase
    for i in range(metade-1, -1, -1): 
        decifrado += pl1[i]
    
    # Percorre a segunda metade de trás para frente, reconstruindo a parte final da frase
    for i in range(len(pl2)-1, -1, -1):
        decifrado += pl2[i]
    
    print(decifrado)