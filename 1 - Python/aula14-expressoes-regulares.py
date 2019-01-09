"""
- Aula 14 - Expressões regulares, procurando por e-mails

- Documentação: https://docs.python.org/2/library/re.html
- Simular Regex: https://regex101.com/
"""
# Libs para expressões regulares
import re
import requests

teste = 'O gato é bravo'

# O primeiro argumento de search é a expressão que será usada para procurar os padrões dentro da String teste
padrao = re.search(r'ga', teste) # RAW String # search busca somente a primeira ocorrencia
#padrao = re.search(r'ga\w', teste) # /w aceita qualquer String após a palavra 'ga'

if padrao:
    print(padrao.group())
else:
    print("Padrão não encontrado!")

teste = 'O gato, a gata, os gatinhos, os gatoes'

padrao = re.findall(r'gat\w+', teste) # findall busca todas as ocorrencias
# + repete uma ou mais vezes o padrão anterior
# * repete por 0 ou infinitas vezes
# r'[gat]' irá procurar por qualquer das letras g a t dentro da string teste

if padrao:
    print(padrao)
else:
    print("Padrão não encontrado!")

print("")
print("Procurando e-mails em sites . . .")

requisicao = requests.get('http://www.acessoainformacao.gov.br/contato-1')

padrao = re.findall(r'[\w\.-]+@[\w-]+\.[\w\.-]+', requisicao.text) # RAW String

if padrao:
    print(padrao)
else:
    print("Nenhum e-mail foi encontrado!")