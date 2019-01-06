"""
Estruturas de laços (WHILE e FOR)
"""

nomes = ['Guilherme', 'Marcelo', 'João', 'Júlia']

for nome in nomes: # Para cada nome dentro da lista de nomes, mostre-me o nome
    print(nome)

lista_numeros = range(5) # Gerando uma lista de numeros de 0 a 4 (5 digitos)

for i in lista_numeros:
    print(i)

lista_numeros = range(5, 10, 2) # de 5 a 10 pulando de 2 em dois

for i in lista_numeros:
    print(i)

for indice in range(4):
    print(nomes[indice])

for indice in range(len(nomes)): # len(nomes) retorna a quantidade de itens
    print(nomes[indice])
    nomes.append("OII")

for nome in nomes:
    print(nome)

print(nomes)

print('\n') # Pulando linha

palavra = "Carlos Henrique"

for letra in palavra:
    print(letra)

# Teste com while

i = 0
while i < 10:
    print('i ainda é menor que 10: ', i )
    i = i + 1 # Somando mais 1 ao i
    # i += 1 # Somando mais 1 ao i

print('Acabou o while: i ==', i )

print('\n') # Pulando linha

# Teste com WHILE
numero = 0

while True:
    print(numero)
    if numero == 20:
        print('Parando execução do while com break')
        break
    numero += 1

