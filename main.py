

import telebot
from config import TOKEN, major_exchanges
from extensions import Convertor, APIException
import traceback

# initialization of bot object:
bot = telebot.TeleBot(TOKEN)

# main commands for bot:
# base commands:
@bot.message_handler(commands=['start']) # use method message_handler with argument 'start' or type of message and return decorator
def start(message: telebot.types.Message): # in decarator our function - start, which process the messages
    text = 'Hello! \nChoice the commands: \n/start (show you menu of commands) ' \
           '\n/values (show you available currencies) \n/help (show you the conversion rules)'
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

# the command for currency conversion with Exception handler
@bot.message_handler(content_types=['text'])
def converter(message: telebot.types.Message):
    values = message.text.split(' ')
    try:
        if len(values) != 3:
            raise APIException('Wrong numbers of parameters!')

        answer = Convertor.get_price(*values) # take parametres from class Converter
    except APIException as e:
        bot.reply_to(message, f"Command error:\n{e}")
    except Exception as e:
        traceback.print_tb(e.__traceback__)
        bot.reply_to(message, f"Unknown error:\n{e}")
    else:
        bot.reply_to(message, answer)


# launch communication with Telegram (use the method - polling, for start bot mode)
bot.polling()