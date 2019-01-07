"""
Aula 6 - Tuplas, dicionários e conjuntos

- Dicionários
- Tuplas
- Conjuntos

- https://docs.python.org/2/library/stdtypes.html
"""

minha_lista = ['Machine Learning', 'DataScience', 'Big Data'] # Lista - dinamica
minha_tupla = ('Machine Learning', 'DataScience', 'Big Data') # Tupla - estático - numero definido de itens 
meu_dicionario = {'nome' : 'Carlos', 'sobrenome' : 'Henrique', 'idade' : 20, 'profissao' : 'Desenvolvedor de software'} # Dicionário - dinamico, vulgo HashMap do Java
meu_conjunto = {'Carlos', 'Henrique', 'Carlos'} # Conjunto - dinamico

print(minha_lista)
print(minha_tupla)
print(meu_dicionario)
print(meu_conjunto) # Pode-se oberservar que no conjunto não há repetição de itens

# Manipulando tupla
print(minha_tupla[1])
for nome in minha_tupla:
    print(nome)

minha_tupla = ('Machine Learning', 'Data Science', 'BI')

# Printando todos os itens de minha tupla
for nome in minha_tupla:
    print(nome)

# Verificando se há o item Machine Learning em minha tupla
if 'Machine Learning' in minha_tupla:
    print('Machine Learning esta na coleção')
else:
    print('Machine Learning não está na coleção')

# Manipulando Dicionário

print(meu_dicionario)
print('Nome:', meu_dicionario['nome'])
print('Idade:', meu_dicionario['idade'])

# Verificando se há o item 'Carlos' no dicionário
if 'Carlos' in meu_dicionario.values():
    print('Carlos está no dicionário!')

# Printando valores do meu dicionário
for valores in meu_dicionario.values():
    print(valores)

# Printando todas as chaves (keys) que há em meu dicionário
for keys in meu_dicionario.keys():
    print(keys)

# Mudando o valor da chave item
meu_dicionario['idade'] = 21
print(meu_dicionario)

# Adicionando nova chave para novo item
meu_dicionario['cidade'] = 'Marau'
print(meu_dicionario)

    # Dicionario e conjunto é mais eficiente quando estamos buscando informações nas coleções
 
# Manipulando Conjunto
# Eficiencia busca conjunto > Eficiencia busca lista

#print(meu_conjunto[0]) ERRO! Não há indice em conjunto

meu_conjunto.add('Thais')
meu_conjunto.add('Henrique')
print(meu_conjunto)

if 'Carlos' in meu_conjunto:
    print('Carlos foi encontrado dentro do conjunto!')

meu_conjunto.remove('Carlos')
print(meu_conjunto)

# Criação dos objetos vazios
lista = []
tupla = ()
dicionario = {} # or dict()
conjunto = set()