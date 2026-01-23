
maior = pos = 0
for i in range(1, 101):
    num = int(input())
    if i == 1 or num > maior:  # O primeiro valor é definido como o maior; depois, comparamos os próximos para atualizar o maior e sua posição.
        maior = num
        pos = i 

print(maior)
print(pos)