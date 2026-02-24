#Desafio 1239: Atalhos Bloggo

'''A questão 1239 – Atalhos Bloggo pede para converter textos que usam atalhos simples em suas versões HTML. 
No sistema Bloggo, trechos entre sublinhados (_) devem ser transformados em itálico, usando <i> e </i>, 
e trechos entre asteriscos (*) em negrito, com <b> e </b>. O programa deve ler várias linhas e substituir 
corretamente os pares de símbolos, garantindo que o texto final mantenha a formatação equivalente em HTML.'''

while True:
    try:
       texto = input()
       novo_texto = "" #variável usada para construir o novo texto, pois strings são imutáveis e não podem ser modificadas diretamente
       aber1 = aber2 = False #variáveis de controle da abertura e fechamento das tags.
       for letra in texto:
        if letra == "_": #verifico se é o atalho do efeito itálico
            if not aber1: # se for, verifico se a tag de abertura não existe
                novo_texto += "<i>" #se não existir, insiro a tag de abertura
                aber1 = True #sinalizo que tag de abertura existe agora
            else: 
               novo_texto += "</i>" #caso já exista fecho a tag 
               aber1 = False #sinalizo que a tag de abertura ja foi fechada e não existe mais
        elif letra == "*": #Replico a lógica do itálico pro negrito.
            if not aber2:
                novo_texto += "<b>"
                aber2 = True
            else:
               novo_texto += "</b>"
               aber2 = False    
        else: #Caso seja algo diferente dos atalhos so armazeno na variável
           novo_texto += letra
       print(novo_texto)         
    except EOFError:
       break 