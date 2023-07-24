import requests
import json

class Converter:
    @staticmethod
    def get_price(base, quote, amount):
        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={base}&tsyms={quote}')
        resp = json.loads(r.content)
        price = resp[quote] * float(amount)
        return price
