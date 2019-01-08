"""
- Aula 11 - Tratamentos de erros e exceções 

- TRY
- EXCEPT

"""

import time

# TRY EXCEPT
try:

    a = 1000/0

except:
    print("Não é possível fazer divisão por zero")

# TRY EXCEPT - Com lançamento de exceção
try:

    a = 1000/0
    ada()
except ZeroDivisionError:
    print("Não é possível fazer divisão por zero")
except NameError:
    print("Você digitou alguma coisa errada")

# TRY EXCEPT - Com lançamento genérico
try:

    a = 1000/0

except Exception as erro:
    print("Aconteceu algum erro:", erro)

# TRY EXCEPT 
try:

    open("ajdiao.txt")

except Exception as erro:
    print("Aconteceu algum erro:", erro)

def abrir_arquivo():
    try:
        arquivo = open('arquiv.txt')
        return arquivo
    except Exception as erro:
        print("Aconteceu algum erro:", erro)
        time.sleep(5)
        return False

while not abrir_arquivo():
    print("Tentando abrir o arquivo!")
    
print("Consegui abrir o arquivo!")
