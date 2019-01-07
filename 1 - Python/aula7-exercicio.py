"""
EXERCICIO: Escreva uma funcao que recebe um objeto de coleção e retorna o valor do maior numero dentro dessa coleção, 
e outra função que retorne o menor valor dessa coleção
"""

def maior_valor(object):
    object = sorted(object, reverse=True)
    return object[0]

def menor_valor(object):
    object = sorted(object)
    return object[0]

lista = [2,3,1,4,5]

print("Printando o maior valor!")
print(maior_valor(lista))

print("Printando o menor valor!")
print(menor_valor(lista))