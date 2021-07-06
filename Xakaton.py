import telebot
import Enum

bot = telebot.TeleBot(Enum.TOKEN)

@bot.message_handler(commands=['help', 'Помощь', 'помощь'])
def send_help(message):
    bot.reply_to(message, Enum.LOCALE['help_list'])

bot.polling(none_stop = True)

"""
@bot.message_handler(commands=['Начать'])
def send_welcome(message):
    bot.reply_to(message, f'Я - бот. Я слежу за состоянием окружающей среды в классах. Приятно познакомиться, {message.from_user.first_name}. Что вы хотите узнать?')
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text.lower() == 'список помещений.':
        bot.send_message(message.from_user.id, '')
    elif message.text.lower() == 'карта этажа [номер этажа]':
        bot.send_message(message.from_user.id, '')
    elif message.text.lower() == 'состояние класса [номер класса]':
        bot.send_message(message.from_user.id, '')
    else:
        bot.send_message(message.from_user.id, 'Не понимаю, что это значит.')
bot.polling(none_stop=True)
"""