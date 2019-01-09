"""
- Aula 13 - API, JSON e consultando listas de filmes

- API - http://omdbapi.com/
- JSON

"""
import requests
import json

req = None

def request_film(titulo):
    try:
        req = requests.get('http://omdbapi.com/?t=' + titulo) # Inserir uma API válida
        dicicionario = json.loads(req.text)
        return dicicionario
    except Exception as e:
        print("Erro na conexão")
        print("StackTrace:", e)
        return None

def detalhes(filme):
    print(filme)
    print('Título:', filme['Title'])
    print('Ano:', filme['Year'])
    print('Diretor:', filme['Director'])
    print('Atores:', filme['Actors'])
    print('Nota:', filme['imdbRating'])

sair = False
while not sair:

    op = input("Insira o nome do filme ou SAIR: ")

    if op == 'SAIR':
        sair = True
        print("Saindo...")
    else:
        pesquisa = request_film(op)
        if pesquisa['Response'] == 'False':
            print("Filme não encontrado!")
        else:
            detalhes(pesquisa)