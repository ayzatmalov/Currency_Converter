import requests
import json
from config import major_exchanges

class APIException(Exception): # creat child class (from the built-in which catch common exceptions)
    pass

class Convertor: # creat class for currency conversion (take this functionality from main.py and hide it in this class
    @staticmethod
    def get_price(base, quote, amount): # include in convert method the exception handlers
        try: # for exception KeyError for base currency
            base_key = major_exchanges[base.lower()]
        except KeyError:
            raise APIException(f"Currency {base} not found!")
        try: # for exception KeyError for qoute currency
            quote_key = major_exchanges[quote.lower()]
        except KeyError:
            raise APIException(f"Currency {quote} not found!")
        if base_key == quote_key: # for exception equal currencies
            raise APIException(f'Unable to convert same currencies {base}!')
        try: # for exception ValueError for amount
            amount = float(amount)
        except ValueError:
            raise APIException(f'Unable process input value: {amount}!')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={base_key}&tsyms={quote_key}')
        resp = json.loads(r.content)
        price = resp[quote_key] * float(amount)
        new_price = round(price, 2)
        message = f"Price {amount} {base} in {quote} : {new_price}"
        return message