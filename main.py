import telebot

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
    text = 'Hello Marat Malov!'
    bot.send_message(message.chat.id, text)

# the command for handler which show availbale currencies for conversion:
@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'available currencies:'
    for i in major_exchanges.keys(): # go through the keys of major_currencies
        text = '\n'.join((text, i)) # display each currency on new line
    bot.reply_to(message, text) # attaching the message like a reply for user's message

# launch communication with Telegram (use the method - polling, for start bot mode)
bot.polling()