#Desafio 1175: Troca em Vetor I

'''Faça um programa que leia um vetor N[20]. Troque a seguir, o primeiro elemento com o último, o segundo elemento 
com o penúltimo, etc., até trocar o 10º com o 11º. Mostre o vetor modificado.'''

n = []
for _ in range(20): #Armazena os valores no vetor n
    num = int(input())
    n += [num]

for i in range(10): #Faz a troca, ou seja, inverte o vetor. Em python pode-se usar a função reverse() para fazer o mesmo, mas como o foco é desenvolver a lógica fiz com o for
    n[i], n[20-i-1] = n[20-i-1], n[i] #Declaro que o vetor na posição inicial n[i] e posição final, que é igual ao tamanho menos a posição atual menos 1, vão inverter seus valores.

for i in range(20): #Mostro o vetor modificado
    print(f"N[{i}] = {n[i]}")