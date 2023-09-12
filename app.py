import telebot

TOKEN = '6607465253:AAGgXR64ZdyTvDgvBAN4nzYHizLWYAT9yxg'

bot = telebot.TeleBot(TOKEN)

keys = {
    'Биткоин': 'BTC',
    'Эфириум': 'ETH',
    'Доллар': 'USD',
}


@bot.message_handler(commands = ['start', 'help'])
def help(message: telebot.types.Message):
    text = 'Чтобы начать работу введите команду боту в следеующем формате: \n<имя валюты> \
<в какую валюту перевести> \
<количество переводимой валюты>\nУвидеть список всех доступных валют: /values'
    bot.reply_to(message, text)


@bot.message_handler(commands = ['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in keys.keys():
        text = '\n'.join((text, key,))
    bot.reply_to(message, text)


bot.polling()
