# import requests
# import json
#
# base = "USD"
# quote = "RUB"
# amount = 100
#
# r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={base}&tsyms={quote}')
# resp = json.loads(r.content)
# price = resp[quote] * amount
# print(price) # 9081,00 (19:49 2023-07-24)
