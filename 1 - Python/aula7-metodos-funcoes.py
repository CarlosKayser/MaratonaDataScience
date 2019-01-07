"""
Aula 7 - Funções e Métodos

- Funções
- Métodos

- https://docs.python.org/2/library/stdtypes.html#functions
"""

def soma(num1, num2):
    return num1 + num2

soma = soma(10, 5)

print(soma)

def imprime_hw():
    print('Hello World!')

imprime_hw()
imprime_hw()

def tem_sete_itens(object):
    if len(object) == 7:
        return True
    else: 
        return False

if tem_sete_itens('Carlos'):
    print('Tem sete letras!')
else:
    print('Não tem sete letras!')
