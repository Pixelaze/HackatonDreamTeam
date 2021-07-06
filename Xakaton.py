import telebot
bot = telebot.TeleBot('1834921230:AAFZNRZfuIzBjKES5ITcTwUkGyTqkoWIUWk')
@bot.message_handler(commands=['Начать'])
def send_welcome(message):
    bot.reply_to(message, f'Я - бот. Я слежу за состоянием окружающей среды в классах. Приятно познакомиться, {message.from_user.first_name}. Что вы хотите узнать?')
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text.lower() == 'Список помещений.':
        bot.send_message(message.from_user.id, '')
    elif message.text.lower() == 'Карта этажа [номер этажа]':
        bot.send_message(message.from_user.id, '')
    elif message.text.lower() == 'Состояние класса [номер класса]':
        bot.send_message(message.from_user.id, '')
    else:
        bot.send_message(message.from_user.id, 'Не понимаю, что это значит.')
bot.polling(none_stop=True)
