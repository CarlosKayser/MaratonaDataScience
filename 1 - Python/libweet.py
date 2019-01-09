import oauth2

class Twitter:

    def __init__(self, consumer_key, consumer_secret, token_key, token_secret):
        connect(consumer_key, consumer_secret, token_key, token_secret))
    
    def connect(self, consumer_key, consumer_secret, token_key, token_secret):
        self.consumer = oauth2.Consumer(consumer_key, consumer_secret)
        self.token = oauth2.Token(token_key, token_secret)
        self.client = oauth2.Client(consumer, token)
        
        return self.client