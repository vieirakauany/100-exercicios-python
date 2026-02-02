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
---

## Dia 03

### 🧠 Entendendo a Conversão de Tempo em Algoritmos

Quando precisamos calcular quanto tempo passou entre dois horários (por exemplo, o início e o fim de um jogo), encontramos um problema comum:

>As unidades de tempo são diferentes (horas, minutos e segundos).

Por isso, a primeira etapa é converter tudo para a menor unidade possível — normalmente segundos ou minutos — para facilitar o cálculo da diferença.

---

### 1. Converter tudo para a menor unidade de tempo

Sabendo que:<br>
1 hora = 60 minutos <br>
1 minuto = 60 segundos <br>
Logo, 1 hora = 3600 segundos

Podemos representar qualquer horário (h:m:s) como segundos totais:

>tempo_total = ℎ × 3600 + 𝑚 × 60 + 𝑠

Isso transforma tudo em um único número — facilitando a subtração depois.

---

### 2. Calcular a diferença entre o tempo final e o inicial

> duracao = tempo_final_em_segundos −  tempo_inicial_em_segundos

Mas, se o jogo começou em um dia e terminou em outro (por exemplo, começou às 22h e terminou às 2h da manhã), o resultado dessa subtração será zero ou negativo.
Isso acontece porque o relógio “reiniciou” ao passar da meia-noite.

---
### 3. Corrigir casos em que o jogo atravessa a meia-noite

Como o relógio zera a cada 24 horas, se o resultado for menor ou igual a zero, adicionamos o total de segundos de um dia inteiro:

>duracao += 24 × 3600

--- 
### 4. Converter o resultado de volta para horas, minutos e segundos

Depois de obter o tempo total em segundos, precisamos voltar para o formato legível (h:m:s):

Sabendo que 1 hora = 3600 segundos,
podemos descobrir quantas horas inteiras cabem dentro da duração total usando divisão inteira (//):

> horas = duracao // 3600

💡Explicação: A divisão inteira pega apenas a parte completa do resultado e ignora o resto.

>📘 Exemplo:<br>
duracao = 10800  # segundos <br>
horas = 10800 // 3600  # → 3

✅ Resultado: 3 horas completas.

#### Descobrindo os minutos

Depois de retirar as horas, ainda sobram alguns segundos — o resto da divisão por 3600.
Usamos o operador módulo (%) para pegar esse resto, e depois transformamos o que sobrou em minutos:

> minutos = (duracao % 3600) // 60


💡 Por que isso funciona: <br>
duracao % 3600 → dá o que sobrou após tirar todas as horas completas. // 60 → converte esse resto (em segundos) em minutos inteiros.

>📘 Exemplo:<br>
duracao = 10920  # segundos (3 horas, 2 minutos) <br>
minutos = (10920 % 3600) // 60 <br>
10920 % 3600 = 120  (sobraram 120 segundos após as 3 horas)<br>
 120 // 60 = 2

✅ Resultado: 2 minutos.

#### Descobrindo os segundos

Por fim, para saber quantos segundos sobraram depois de tirar horas e minutos inteiros, usamos novamente o operador % (resto):

>segundos = duracao % 60


>📘 Exemplo:<br>
duracao = 10923  # segundos<br>
segundos = 10923 % 60  # → 3

✅ Resultado: 3 segundos.


## Dia 09 e 10

#### 🔍 Busca em vetores<br>
A busca em um vetor (ou lista) significa procurar um valor específico entre os elementos armazenados.

A forma mais comum é com um loop:<br>
>for i in range(len(lista)): <br>
    &nbsp;&nbsp;&nbsp;&nbsp;if lista[i] == valor: <br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    print("Encontrado na posição", i)


Para buscar de trás para frente, você pode usar o índice negativo:

<ul>
<li>-1 representa o último elemento</li>
<li>-2, o penúltimo, e assim por diante.</li>
</ul>
Exemplo:<br><br>

>print(lista[-1])  # Último elemento


Também é possível percorrer a lista de forma invertida:

>for i in range(len(lista)-1, -1, -1):<br>
  &nbsp;&nbsp;&nbsp;&nbsp;  print(lista[i])  # percorre do fim para o início
---
#### ⚙️ Principais métodos de listas em Python

  | Método | Função | Exemplo |
|--------|---------|---------|
| `append(x)` | Adiciona um elemento ao final da lista | `lista.append(10)` |
| `insert(i, x)` | Insere um elemento na posição `i` | `lista.insert(2, 5)` |
| `pop()` | Remove e retorna o último elemento | `lista.pop()` |
| `remove(x)` | Remove o primeiro elemento igual a `x` | `lista.remove(3)` |
| `index(x)` | Retorna o índice do primeiro elemento igual a `x` | `lista.index(7)` |
| `count(x)` | Conta quantas vezes `x` aparece | `lista.count(2)` |
| `reverse()` | Inverte a ordem dos elementos | `lista.reverse()` |
| `sort()` | Ordena os elementos (crescente por padrão) | `lista.sort()` |
| `copy()` | Cria uma cópia da lista | `nova = lista.copy()` |
| `clear()` | Apaga todos os elementos da lista | `lista.clear()` |



