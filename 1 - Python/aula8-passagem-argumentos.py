"""
Aula 8 - Argumentos de linha de comando

- Passagem de argumentos
- Exemplo: python sqlmap.py --help
- Útil para programas CLI

"""

# Importando biblioteca sys
import sys

argumentos = sys.argv # arg1 metod // arg2 - n1 // agr3 - n2
#print(argumentos)

# Digitar python aula8-passagem-argumentos.py --help
# Saida: ['aula8-passagem-argumentos.py', '--help']

def soma(n1,n2):
    return n1 + n2

def sub(n1,n2):
    return n1 - n2

if argumentos[1] == "soma" or argumentos[1] == "SOMA":
    resp = soma(float(argumentos[2]), float(argumentos[3]))
elif argumentos[1] == "sub" or argumentos[1] == "SUB":
    resp = sub(float(argumentos[2]), float(argumentos[3]))

print(resp)