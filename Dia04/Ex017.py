#Desafio 1049: Animal

'''Neste problema, você deverá ler 3 palavras que definem o tipo de animal possível segundo o esquema abaixo, 
da esquerda para a direita.  Em seguida conclua qual dos animais seguintes foi escolhido, 
através das três palavras fornecidas.

vertebrado
 ├── ave
 │    ├── carnivoro → aguia
 │    └── onivoro   → pomba
 └── mamifero
      ├── onivoro   → homem
      └── herbivoro → vaca

invertebrado
 ├── inseto
 │    ├── hematofago → pulga
 │    └── herbivoro  → lagarta
 └── anelideo
      ├── hematofago → sanguessuga
      └── onivoro    → minhoca

'''



p1 = input().strip().lower() #lower -> deixa todo o texto inserido nesse input em minúsculo, afim de evitar erros de digitação e verificação
p2 = input().strip().lower()
p3 = input().strip().lower()

if p1 == "vertebrado":
    if p2 == "ave":
        if p3 == "carnivoro":
            print("aguia")
        else:
            print("pomba")
    else:
        if p3 == "onivoro":
            print("homem")
        else:
            print("vaca")
else:
    if p2 == "inseto":
        if p3 == "hematofago":
            print("pulga")
        else:
            print("lagarta")
    else:
        if p3 == "hematofago":
            print("sanguessuga")
        else:
            print("minhoca")