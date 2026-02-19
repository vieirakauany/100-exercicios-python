#Desafio: 2752 - Saída 6
'''O seu professor de programação gostaria que você fizesse um programa com as seguintes características:

Crie uma variável para armazenar 50 caracteres;
Atribua a variável anterior a frase: "AMO FAZER EXERCICIO NO URI";
Mostre na primeira linha o carácter <, o valor armazenado na variável com o formato "%s" e o carácter >;
Mostre na linha seguinte o carácter < , o valor armazenado na variável com o formato "%30s" e o carácter >;
Mostre na linha seguinte o carácter < , o valor armazenado na variável com o formato "%.20s" e o carácter >;
Mostre na linha seguinte o carácter < , o valor armazenado na variável com o formato "%-20s" e o carácter >;
Mostre na linha seguinte o carácter < , o valor armazenado na variável com o formato "%-30s" e o carácter >;
Mostre na linha seguinte o carácter < , o valor armazenado na variável com o formato "%.30s" e o carácter >;
Mostre na linha seguinte o carácter < , o valor armazenado na variável com o formato "%30.20s" e o carácter >;
Mostre na linha seguinte o carácter < , o valor armazenado na variável com o formato "%-30.20s" e o carácter >;'''


frase = "AMO FAZER EXERCICIO NO URI"
print(f"<{frase}>")
print(f"<{frase:>30}>") #A string ocupa 30 posições, alinhada à direita.Se tiver menos que 30 caracteres e completado com espaços à esquerda.
print(f"<{frase[:20]}>") #Mostra apenas os primeiros 20 caracteres da string. Da posição 0 a 19
print(f"<{frase:<20}>") #Mostra a string com 20 posições, mas alinhada à esquerda.O restante das posições é preenchido com espaços à direita.
print(f"<{frase:<30}>") #Alinhado à esquerda, ocupando 30 posições.
print(f"<{frase[:30]}>") #Exibe apenas 30 caracteres (se houver mais, corta).
print(f"<{frase[:20]:>30}>") #Máximo de 20 caracteres mostrados. Dentro de um campo de 30 espaços. Alinhado à direita
print(f"<{frase[:20]:<30}>") #Mostra até 20 caracteres. Em campo de 30. Alinhado à esquerda.