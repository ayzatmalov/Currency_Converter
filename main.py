import telebot
import requests
import json
from config import *

# initialization of bot object:
bot = telebot.TeleBot(TOKEN)

# main commands for bot:
# base commands:
@bot.message_handler(commands=['start']) # use method message_handler with argument 'start' or type of message and return decorator
def start(message: telebot.types.Message): # in decarator our function - start, which process the messages
    text = 'Hello! \nChoice the commands: \n/values (show you available currencies) ' \
           '\n/start (show you menu of commands \n/help (show you the conversion rules)'
    bot.send_message(message.chat.id, text)

# the command for explanation of user how to convert (entering format):
@bot.message_handler(commands=['help'])
def help(message: telebot.types.Message):
    text = 'example entering format:' \
           '\nUSD RUB 100; where,' \
           '\nUSD - the base currency,'\
           '\nRUB - the conversion currency,' \
           '\n100 - amount'
    bot.reply_to(message, text)

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