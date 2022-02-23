import telebot
from config import exchanges, TOKEN
from extentions import APIException, Convertor

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def function_name(message: telebot.types.Message):
    text = "Здравуйте я Curcy! Я помогу вам узнать актуальный курс валют! Чтобы начать работу введите " \
           "комманду боту в следующем формате \n<имя валюты, цену которой вы хотите узнать> " \
           "<в какую валюту перевести> <количество первой валюты>""\nУвидеть список всех доступных валют: /values"
    bot.reply_to(message, text)


@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = "Доступые валюты:"
    for ex in exchanges.keys():
        text = '\n'.join((text, ex))
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text'])
def convert(message: telebot.types.Message):
    try:
        values = message.text.split(' ')

        if len(values) != 3:
            raise APIException('Слишком много параметров!')

        quote, base, amount = values
        total_base = Convertor.convert(quote, base, amount)
    except APIException as e:
        bot.reply_to(message, f'Ошибка пользователя \n{e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду\n{e}')
    else:
        calculation = total_base * int(amount)
        text = f'{amount} {quote} = {calculation} {base}'
        bot.send_message(message.chat.id, text)


bot.polling(none_stop=True)