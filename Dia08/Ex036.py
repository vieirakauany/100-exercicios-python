# Desafia 1098: Sequencia IJ 4

'''Você deve fazer um programa que apresente a sequencia conforme o exemplo abaixo.
I=0 J=1
I=0 J=2
I=0 J=3
I=0.2 J=1.2
I=0.2 J=2.2
I=0.2 J=3.2
.....
I=2 J=?
I=2 J=?
I=2 J=?'''


i = 0.0
while i <= 2:
    for j in range(1, 4):
        i_formatado = int(i) if i.is_integer() else i #Converte 1.0 em 1 
        j_formatado = int(i + j) if (i+j).is_integer() else i+j
        print(f"I={i_formatado} J={j_formatado}")
    
    i += 0.2
    i = round(i, 1) #Arredonda i para uma casa decimal. Isso é importante porque, por causa de imprecisões em números decimais, i poderia virar algo como 0.6000000000001.