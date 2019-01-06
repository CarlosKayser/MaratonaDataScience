"""
Essa aula irá discursar sobre Strings e listas
"""

frase = 'Oi, tudo bem?'

print(frase[0]) # uma string é um vetor de caracteres
print(frase[3:10]) # printar a letra 3 até a letra 10
print(frase[0:10:1]) # printar a letra 0 até a letra 13, pulando de 1 em 1 caracter
print(frase[0:10:2]) # printar a letra 0 até a letra 13, pulando de 2 em 2 caracteres
print(frase[::-1]) # Do primeiro ao último a cada -1 passo 

print(frase.lower()) # Passando a frase para letras minusculas
print(frase.count) # Conta quantos caracteres há na frase
frase_separada = frase.split(',') # Separando a frase pela vírgula
print(frase_separada)
print(frase + " como vai você ?")

lista_frutas = ['Maça', 'Morango', 'Limão', 'Jabuticaba'] # criar uma lista

print(type(lista_frutas))
print(lista_frutas[0])
print(lista_frutas)
print(lista_frutas[0:4:2]) # Printando a lista de frutas, do indice 0 até o 4, pulando de 2 em 2 indices
print(lista_frutas[-1]) # Printar o último valor. Neste caso o Pyhton conta de trás pra frente

lista_frutas.append('Uva') # Adiciona mais um item na lista, no último indice
print(lista_frutas)

lista_frutas.remove('Maça') # Remove o item da lista
print(lista_frutas)

lista_frutas.insert(1, 'Abacaxi') # Inserindo o item na lista no indice 1
print(lista_frutas)

lista_frutas[0] = 'Acerola' # Alterando o valor do primeiro item
print(lista_frutas)

contador_Morango = lista_frutas.count('Morango')
print(contador_Morango) # Conta quantos itens morangos há na lista

print(len(lista_frutas)) # O tamanho do objeto

print(lista_frutas.pop()) # Pega o último e remove da lista
print(lista_frutas)

lista_frutas.clear() # Limpa a lista
print(lista_frutas)