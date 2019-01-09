"""
- Aula 12 - Bibliotecas, PIP e Requisições Web

"""

# pip install requests
import requests

# Equivalente ao null
texto = None

# Passando alguma info no header
cabecalho = {
    "User-agent" : "Windows 12",
    "Referer"    : "https://www.google.com"
}

meus_cookies = {
    "Ultima-visita" : "10-10-2020"
}

login = {
    "username" : "carlos",
    "password" : "123"
}

try:
    # Fazendo uma requisição POST alterando e Header e passando Cookie
    request = requests.post('http://g1.com.br', 
                           headers = cabecalho,
                           cookies = meus_cookies,
                           data = login)

    #request = requests.get('http://g1.com.br') # 'http://globo.com.br'
            # requests.post()
            # requests.delete()
            # Abrange os métodos do protocolo HTTP

    print(request)
    print(type(request))

    print("")

    print("Status Code:", request.status_code)

    # Código fonte da página
    print("Text:", request.text)

except Exception as e:
    print("Erro durante requisição:", e)

# WebScraping
# Beautiful Soup 4 BS4 - pip install bs4