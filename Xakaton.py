import telebot
import Enum
import DataAnalyze
import Room
import Status
from telebot import types

bot = telebot.TeleBot(Enum.TOKEN)

@bot.message_handler(commands=['help', 'Помощь', 'помощь', 'Help'])
def send_help(message):
    keyboard = types.InlineKeyboardMarkup()
    callback_button = types.InlineKeyboardButton(text="Список комнат", callback_data="test")
    keyboard.add(callback_button)
    bot.reply_to(message, Enum.LOCALE['help_list'], reply_markup = keyboard)

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
        status = 0
        for i in range(Enum.ROOM_COUNT):
            room_status = Enum.ROOMS[i][0]
            room_status = Status.statusAnalyzer.analyzeRoom(room_status)[0]
            if(room_status == Enum.Status.BEST):
                status += 0
            elif(room_status == Enum.Status.GOOD):
                status += 1
            elif(room_status == Enum.Status.MEDIUM):
                status += 2
            elif(room_status == Enum.Status.BAD):
                status += 3
            elif(room_status == Enum.Status.WORST):
                status += 4
        status = round(status / Enum.ROOM_COUNT)
        if(status == 0):
            status = Enum.Status.BEST
        elif(status == 1):
            status = Enum.Status.GOOD
        elif(status == 2):
            status = Enum.Status.MEDIUM
        elif(status == 3):
            status = Enum.Status.BAD
        else:
            status = Enum.Status.WORST
        bot.reply_to(message, status)
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

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.message:
        if call.data == "test":
            send_room_list(call.message)

bot.polling(none_stop = True)