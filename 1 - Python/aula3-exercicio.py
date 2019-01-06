"""
Faça um programa que pergunte a idade, o peso e a altura de uma pessoa e decide se ela está apta a ser do Exercito.
Para entrar no exército, é preciso ter mais de 18 anos, pesar mais ou igual 60kg e medir mais ou igual de 1,70 metros
"""

idade = input("Informe sua idade: ")
peso = input("Informe seu peso: ")
altura = input("Informe sua altura: ")

if int(idade) > 18 and int(peso) >= 60 and float(altura) >= 1.70:
    print("Você está apto para servir o exército!")
else:
    print("Você não está apto para servir o exército!")