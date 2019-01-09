"""
- Aula 16 - Publicando e pesquisando no Twitter

- https://developer.twitter.com/en/docs/api-reference-index.html
- pip install oauth2

"""
import oauth2
import json
import pprint # Pretty Print
import urllib.parse

consumer_key = 'Your consumer key here'
consumer_secret = 'Your consumer secret here'
token_key = 'Your token key here'
token_secret = 'Your token secret here'

consumer = oauth2.Consumer(consumer_key, consumer_secret)
token = oauth2.Token(token_key, token_secret)

client = oauth2.Client(consumer, token)

query = input("Pesquisa: ")
query_codificada = urllib.parse.quote(query, safe='')

req = client.request('https://api.twitter.com/1.1/search/tweets.json?q=' + query_codificada + '&lang=pt')

print(type(req[0]))
print(type(req[1]))

req = req[1].decode()
obj = json.loads(req)

# TODO: Verificar se houve algum erro na req
if obj['errors']:
    print('Houve um erro na requisição')
    exit()

tweets = obj['statuses']

for tweet in tweets:

    print(tweet['user']['screen_name'])
    print(tweet['text'])
    print('')