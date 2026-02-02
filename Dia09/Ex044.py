#Desafio 1176: Fibonacci em Vetor

'''Faça um programa que leia um valor e apresente o número de Fibonacci correspondente a este valor lido. 
Lembre que os 2 primeiros elementos da série de Fibonacci são 0 e 1 e cada próximo termo é a soma dos 2 anteriores a 
ele. Todos os valores de Fibonacci calculados neste problema devem caber em um inteiro de 64 bits sem sinal.'''

t = int(input())
seq_fib = [0,1]
for _ in range(t):
    num = int(input())
    if num < len(seq_fib):
        print(f"Fib({num}) = {seq_fib[num]}") # Se o número já estiver calculado na lista, apenas exibe o resultado
    else:
        for _ in range(num - 1):
            seq_fib += [seq_fib[-2] + seq_fib[-1]]  # Adiciona à lista a soma dos dois últimos elementos (regra da sequência de Fibonacci)
        print(f"Fib({num}) = {seq_fib[num]}")