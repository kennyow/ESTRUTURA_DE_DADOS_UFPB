
vetor = []
cont = 0
stop = 's'

if not vetor:
    print("O vetor está vazio.")
    while True:
        loc = int(input(f"Insira um número na lista:"))
        vetor.append(loc)
        stop = str(input("Deseja acrescentar outro número? [s/n]"))
        if stop in 'Nn':
            break
else:
    print("O vetor está ocupado.")

print(f"Vetor digitado pelo usuário: {vetor}")
print(f"Tamanho do Vetor: {len(vetor)}")



while True:
    mod = int(input("Qual número digitado deseja modificar? "))
    out = int(input("Por qual número deseja modificá-lo? "))
    for num in range(0, len(vetor)):
        if vetor[num] == mod:
            vetor[num] = out
    stop = str(input("Deseja substituir outro número? [s/n]"))
    if stop in 'Nn':
        break



print(f"Novo vetor modificado: {vetor}")

while True:
    add = str(input("Deseja adicionar algum outro número ao vetor?[s/n] "))
    if add in 'Nn':
        break
    add2 = int(input("Qual número deseja acrescentar?"))
    loc2 = int(input(f"Em qual das {len(vetor)} posições deseja colocá-lo?"))

    vetor[loc2 - 1] = add2


print(f"Novo vetor modificado: {vetor}")

while True:
    rem = str(input("Deseja remover algum dos vetores?[s/n]"))
    if rem in 'Nn':
        break
    add3 = int(input(f"Qual dos seguintes vetores {vetor} deseja remover?"))
    for item in vetor:
        if item == add3:
            vetor.remove(item)  


print(f"O novo vetor modificado {vetor} agora possui {len(vetor)} itens.")
