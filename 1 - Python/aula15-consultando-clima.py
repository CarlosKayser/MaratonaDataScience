"""
- Aula 15 - Consultando o clima e cotação do dólar

- Clima API
    - https://hgbrasil.com/status/weather/
    - https://api.hgbrasil.com/weather/?format=json&woeid=455903 # Brasil

"""
import requests
import json

req = requests.get('https://api.hgbrasil.com/weather/?format=json&woeid=455903')

clima = json.loads(req.text)
clima = clima['results']

print('#### CLIMA ####')
print('Data:', clima['date'])
print('Hora:', clima['time'])
print('Temperatura:', str(clima['temp'])+'ºC')
print('Tempo:', clima['description'])
print('Cidade:', clima['city'])