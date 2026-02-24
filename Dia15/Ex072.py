#Desafio  1234: Sentença Dançante

'''Dada uma frase, as letras devem ser convertidas alternando entre maiúsculas e minúsculas, ignorando os espaços. 
A primeira letra deve ser maiúscula, a segunda minúscula, a terceira maiúscula novamente e assim por diante, criando 
um efeito de “sentença dançante”. O programa deve processar várias linhas de entrada e exibir cada frase com essa 
formatação aplicada.'''

while True:
    try:
        sentenca = input()
        sent_dancante = ""
        ultimo = ""
        for c in sentenca:
            if c.isalpha(): #verifica se é uma letra
                if ultimo == "" or ultimo.islower(): #Se for a primeira letra da frase ou suceder uma letra minúscula, transformo em maiúscula
                    sent_dancante += c.upper()
                    ultimo = c.upper()
                else: #Senão transformo em minúscula
                    sent_dancante += c.lower()
                    ultimo = c.lower()
            else:
                sent_dancante += c
        print(sent_dancante)
    except EOFError:
        break