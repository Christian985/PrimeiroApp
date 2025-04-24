# 1- Cria uma lista com os nomes de 5 objetos.
nomes = ['Ana', 'Bernardo', 'Christian', 'Daniel', 'Eugêne']

# 2- Adiciona mais um objeto ao final da lista.
nomes.append('Dener')

# 3- Acessa o objeto que está na 2a posição.
print('Segundo nome:', nomes[1])

# 4- Remova um objeto da lista.
nomes.remove('Daniel')

# 5- Exibe o tamanho da lista.
len(nomes)

# 6- Mostra todos os itens com um laço for.
for nome in nomes:
    print(nome)
print()

# 7- Verifica se 'Cadeira' está na lista. Se sim a remove, senão a adiciona.
if 'Cadeira' in nomes:
    nomes.remove('Cadeira')
    print(nomes)
else:
    nomes.append('Cadeira')
    print(nomes)

# 8- Ordena a lista em ordem alfabética (nomes.sort(reverse=True) para inverter.
nomes.sort()

# 9- Exibe o primeiro e o último objeto.
print(nomes[0])
print(nomes[4])
print()

# 10- Limpa toda a lista
nomes.clear()
print(nomes)