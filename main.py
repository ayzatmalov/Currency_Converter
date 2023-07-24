import telebot
import requests
import json

# creation of dictionary for major currencies:
major_exchanges = {
    'Dollar': 'USD',
    'Euro': 'ЕUR',
    'Ruble': 'RUB',
}

# main contstant for HTTP API:
TOKEN = '6416434012:AAEcWPvx66qzOsuBjJJTKvoQd3IyRwl5Mhk'

# initialization of bot object:
bot = telebot.TeleBot(TOKEN)

# main commands for bot:
# base commands:
@bot.message_handler(commands=['start', 'help']) # use method message_handler with two arguments 'start' and 'help' or types of messages and return decorator
def start(message: telebot.types.Message): # in decarator our function - start, which process the messages
    text = 'Hello! \nChoice the commands: \n/values (show you available currencies) ' \
           '\n/start (show you menu of commands)'
    bot.send_message(message.chat.id, text)

# the command for handler which show availbale currencies for conversion:
@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Available currencies:'
    for i in major_exchanges.keys(): # go through the keys of major_currencies
        text = '\n'.join((text, i)) # display each currency on new line
    bot.reply_to(message, text) # attaching the message like a reply for user's message

# the command for currency conversion
@bot.message_handler(content_types=['text'])
def converter(message: telebot.types.Message):
    base, quote, amount = message.text.split()
    r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={base}&tsyms={quote}')
    resp = json.loads(r.content)
    price = resp[quote] * float(amount)
    bot.reply_to(message, f'Price for {amount} {base} in {quote} : {price}')
    return message

# launch communication with Telegram (use the method - polling, for start bot mode)
bot.polling()