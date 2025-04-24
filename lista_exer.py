# 1-
nomes = ['Ana', 'Bernardo', 'Christian', 'Daniel', 'Eugêne']

# 2-
nomes.append('Dener')

# 3-
print('Segundo nome:', nomes[1])
# 4-
nomes.remove('Daniel')

# 5-
len(nomes)

# 6-
for nome in nomes:
    print(nome)
print('')
# 7-
if 'Cadeira' in nomes:
    nomes.remove('Cadeira')
    print(nomes)
else:
    nomes.append('Cadeira')
    print(nomes)

# 8-
nomes.sort()

# 9-
print(nomes[0])
print(nomes[4])
print()
# 10-
nomes.clear()
print(nomes)