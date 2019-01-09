"""
- Aula 15 - Consultando o clima e cotação do dólar

- API's
    - https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/aplicacao#!/
    - https://api.hgbrasil.com/finance/quotations
"""

import requests
import json

req = requests.get('https://api.hgbrasil.com/finance/quotations?format=json')

cotacao = json.loads(req.text)

print('#### COTAÇÃO ####')
print('Valor Dólar:', cotacao['results']['currencies']['USD']['buy'])
print('Valor Euro:', cotacao['results']['currencies']['EUR']['buy'])
print('Valor Bitcoin:', cotacao['results']['currencies']['BTC']['buy'])