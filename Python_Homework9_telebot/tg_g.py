# https://t.me/GB_canbies_bot

import telebot
import random
from telebot import types

bot = telebot.TeleBot("5690682682:AAFxafGwTByfycauhmq6jRf9DH8giiqRkHE")

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id,"Сыграем в игру 'Конфеты'?")
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = types.KeyboardButton("Очень легко")
    but2 = types.KeyboardButton("Кошмар")
    markup.add(but1)
    markup.add(but2)
    bot.send_message(message.chat.id, "Если да, то выберете уровень сложности'", reply_markup=markup)
    bot.register_next_step_handler(message, game)


sweets = 221
max_sweets = 28
flag = ''
@bot.message_handler(commands=["Играть"])
def game(message):
    global flag
    bot.send_message(message.chat.id, '_', reply_markup=types.ReplyKeyboardRemove())
    bot.send_message(message.chat.id, "Отлично. Начинаем!")
    bot.send_message(message.chat.id, f"Условие игры: "
                                      f"\n\t - На столе лежит {sweets} конфета. Играют два игрока, делая ход друг после друга. Первый ход определяется жеребьёвкой."
                                      f"\n\t - За один ход можно забрать не более чем {max_sweets} конфет. Все конфеты оппонента достаются сделавшему последний ход.")
    flag = random.choice(['user', 'bot'])

    if flag == 'user':
        bot.send_message(message.chat.id, f"Превым ходите Вы")
        controller(message)
    else:
        bot.send_message(message.chat.id, f"Ходит бот")
        controller(message)


def controller(message):
    global sweets, flag, max_sweets
    if sweets > 0:
        if flag == 'user':
            bot.send_message(message.chat.id, f"Сколько конфет вы возьмёте?")
            bot.register_next_step_handler(message, user_input)
        else:
            bot_input(message)

    else:
        flag = 'user' if flag == 'bot' else 'bot'
        if flag == 'user':
            bot.send_message(message.chat.id, f"Поздравляю, вы победили!!")
            start(message)
        else:
            bot.send_message(message.chat.id, f"Победил bot, в следующий раз вам повезёт(нет).")
            start(message)
        sweets = 221
        max_sweets = 28

def bot_input(message):
    global sweets, flag
    if message == "Очень легко":
        if sweets <= max_sweets:
            bot_turn = sweets
        else:
            bot_turn = random.randint(1, 29)
    else:
        if sweets <= max_sweets:
            bot_turn = sweets
        elif sweets % max_sweets == 0:
            bot_turn = max_sweets - 1
        else:
            bot_turn = sweets % max_sweets - 1
            if bot_turn == 0:
                bot_turn = 1

    sweets -= bot_turn
    bot.send_message(message.chat.id, f"Бот взял {bot_turn} конфет")
    bot.send_message(message.chat.id, f"Осталось {sweets}")
    flag = 'user' if flag == 'bot' else 'bot'
    controller(message)

def user_input(message):
    global flag, sweets
    try:
        user_turn = int(message.text)
        if 0 < int(user_turn) < 29:
            sweets -= user_turn
            bot.send_message(message.chat.id, f"Осталось {sweets}")
            flag = 'user' if flag == 'bot' else 'bot'
            controller(message)
        else:
            bot.send_message(message.chat.id, f"Колличество не должно быть от 1 до {max_sweets}")
            bot.register_next_step_handler(message, user_input)
    except ValueError:
        bot.send_message(message.chat.id, "Введите число.")
        bot.register_next_step_handler(message, user_input)


bot.infinity_polling()
