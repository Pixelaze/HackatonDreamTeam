import telebot
import Enum
import DataAnalyze

bot = telebot.TeleBot(Enum.TOKEN)

@bot.message_handler(commands=['help', 'Помощь', 'помощь', 'Help'])
def send_help(message):
    bot.reply_to(message, Enum.LOCALE['help_list'])

@bot.message_handler(commands=['rooms', 'комнаты', 'Комнаты', 'Rooms'])
def send_room_list(message):
    reply = Enum.LOCALE['room_list_print_schema']
    for i in range(Enum.ROOM_COUNT):
        room = Enum.ROOMS[i][0]

        reply += "\n" + Enum.LOCALE['room_list_print_schema_one']
        reply = reply.replace("%ROOM_NUMBER%", str(i + 1))
        reply = reply.replace("%STATUS%", "ЕРЖАН НА МАКСИМЕ ВСТАВАЙ БЛЯТЬ")
        reply = reply.replace("%NAME%", room['room'])
    bot.reply_to(message, reply)

@bot.message_handler()

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