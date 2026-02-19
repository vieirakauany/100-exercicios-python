#Desafio 1024: Criptografia

'''O programa realiza uma criptografia em três etapas para esconder o conteúdo de uma mensagem. 
Primeiro, todas as letras maiúsculas e minúsculas são deslocadas três posições à direita na tabela ASCII,
 enquanto os demais caracteres permanecem inalterados. Em seguida, a linha inteira é invertida, 
 deixando o texto de trás para frente. Por fim, todos os caracteres da metade final da mensagem são deslocados 
 uma posição para a esquerda na tabela ASCII. O resultado final é um texto completamente transformado, 
 que dificulta a leitura e garante uma codificação simples, porém eficaz.'''

n = int(input())
for _ in range(n):
    palavra = list(input())
    tam = len(palavra)

    #1ª Etapa
    for i in range(tam):
        if palavra[i].isalpha():
            palavra[i] = chr(ord(palavra[i]) + 3)

    #2ª Etapa
    palavra.reverse()
    
    #3ª Etapa
    for i in range(tam//2, tam):
        palavra[i] = chr(ord(palavra[i]) - 1)
    
    print("".join(palavra))
        
