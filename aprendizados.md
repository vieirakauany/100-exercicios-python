# 😎Aprendizados

## Dia 01
cod1, num1, valor1 = map(float, input().split())

1 - O **input** lê uma linha digitada pelo usuário.  
>Por exemplo: 12 1 5.10

2 - O split() divide a string em partes, separando onde há espaços.
> Com o exemplo acima:   
['12' ,  '1' , '5.10']

3- O map() aplica a função float() em cada item da lista.
Ou seja, transforma '12', '1' e '5.10' em números reais:
>   [12 ,  1  , 5.10]

4 -  x1, y1 = ... Aqui ocorre a atribuição.O Python pega os valores retornados e coloca em cada variável respectivamente (primeiro valor é armazenado na primeira variável):
> cod1 = 12 <br> num1 = 1 <br> valor1 = 5.10