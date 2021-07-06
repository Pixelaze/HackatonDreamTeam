import telebot
import Enum
import DataAnalyze
import Room
import Status

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
        reply = reply.replace("%STATUS%", Status.statusAnalyzer.analyzeRoom(room)[0])
        reply = reply.replace("%NAME%", room['room'])
    bot.reply_to(message, reply)

@bot.message_handler(commands=['status', 'статус', 'Статус', 'Status'])
def send_room_data(message):
    message_splitted = message.text.split()
    if(len(message_splitted) == 1):
        bot.reply_to(message, "ЕРЖАН ВСТАВАЙ!!!!!!!")
    else:
        try:
            room_id = int(message_splitted[1])
            if(room_id <= 0 or room_id > Enum.ROOM_COUNT):
                bot.reply_to(message, Enum.LOCALE['room_not_exists_error'])
                return
            reply = Room.getStringRoom(room_id - 1)
            bot.reply_to(message, reply)
        except Exception as e:
            print(e)
            print(e.args)
            bot.reply_to(message, Enum.LOCALE['not_a_number_error'])

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