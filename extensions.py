import requests
import json
from config import major_exchanges

class APIException(Exception): # creat child class (from the built-in which catch common exceptions)
    pass

class Converter: # creat class for currency conversion (take this functionality from main.py and hide it in this class
    @staticmethod
    def get_price(base, quote, amount):
        try: # for exception KeyError for base currency
            base_key = major_exchanges[base.lower()]
        except KeyError:
            raise APIException(f'Валюта {base} не найдена, попробуйте еще раз, все буквы должны быть заглавными!')
        try: # for exception KeyError for qoute currency
            quote_key = major_exchanges[quote.lower()]
        except KeyError:
            raise APIException(f'Валюта {base} не найдена, попробуйте еще раз, все буквы должны быть заглавными!')
        try: # for exception ValueError for amount
            amount = float(amount.replace(',', '.'))
        except ValueError:
            raise APIException(f'Не удалось обработать введенное количество: {amount}, пожалуйста повторите ввод!')
        if base_key == quote_key: # for exception equal currencies
            raise APIException(f'Выберите другую валюту для конвертации {base}!')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={base}&tsyms={quote}')
        resp = json.loads(r.content)
        price = resp[quote] * float(amount)
        return price
