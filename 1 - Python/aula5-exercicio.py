"""
Faça um programa que leia a quantidade de pessoas que serão convidadas para uma festa. 
Após isso, o programa deverá perguntar o nome de todas as pessoas, colocar em uma lista de convidados 
e depois imprimir todos os nomes da lista
"""

qtd_convidados = input("Informe a quantidade de convidados para a festa: ")
lista_convidados = []

for i in range(int(qtd_convidados)):
    print('Insira o nome do convidade de número:', i)
    nome = input()
    lista_convidados.append(nome) 

#print(lista_convidados)

for nome in lista_convidados:
    print('Nome convidado: ', nome)