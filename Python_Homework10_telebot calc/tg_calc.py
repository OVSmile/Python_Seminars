# https://t.me/GB_canbies_bot
from telegram import Update

import telebot
import random
from telebot import types
from log import log_comand

bot = telebot.TeleBot("6055423102:AAE7VT8Rjm9HX576XIIa7oJQx1qrwEO_RIU")
flag = 0
a = ''
b = ''
sign = ''
@bot.message_handler(commands=["start"])
def start(message):
    log_comand(message)
    bot.send_message(message.chat.id,"Калькулятор запущен")
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = types.KeyboardButton("комплексные")
    but2 = types.KeyboardButton("целые")
    markup.add(but1)
    markup.add(but2)
    bot.send_message(message.chat.id, "C какими числами хотите работать?", reply_markup=markup)
    bot.register_next_step_handler(message, get_flag)

def get_flag(message):
    log_comand(message)
    global flag
    if message.text == "комплексные":
        flag = "комплексные"
    elif message.text == "целые":
        flag = "целые"
    bot.send_message(message.chat.id, "Введите число: ")
    bot.register_next_step_handler(message, get_value_a)

def get_value_a(message):
    log_comand(message)
    global a
    try:
        int(message.text) or complex(message.text)
        a = message.text
        bot.register_next_step_handler(message, choice_sign)
    except Exception:
        bot.send_message(message.chat.id, "Введите число: ")
        bot.register_next_step_handler(message, get_value_a)

def choice_sign(message):
    log_comand(message)
    global flag
    if flag == "комплексные":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        but1 = types.KeyboardButton("+")
        but2 = types.KeyboardButton("-")
        but3 = types.KeyboardButton("/")
        but4 = types.KeyboardButton("*")
        markup.add(but1)
        markup.add(but2)
        markup.add(but3)
        markup.add(but4)
        bot.send_message(message.chat.id, "Выберете знак математической операции: ", reply_markup=markup)
        bot.register_next_step_handler(message, get_sign)

    elif flag == "целые":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        but1 = types.KeyboardButton("+")
        but2 = types.KeyboardButton("-")
        but3 = types.KeyboardButton("/")
        but4 = types.KeyboardButton("*")
        but5 = types.KeyboardButton("%")
        but6 = types.KeyboardButton("//")
        markup.add(but1)
        markup.add(but2)
        markup.add(but3)
        markup.add(but4)
        markup.add(but5)
        markup.add(but6)
        bot.send_message(message.chat.id, "Выберете знак математической операции: ", reply_markup=markup)
        bot.register_next_step_handler(message, get_sign)

def get_sign(message):
    log_comand(message)
    global sign
    sign = message.text
    bot.send_message(message.chat.id, "Введите число: ")
    bot.register_next_step_handler(message, get_value_b)

def get_value_b(message):
    global b
    try:
        int(message.text) or complex(message.text)
        b = message.text
        bot.register_next_step_handler(message, get_result)
    except Exception:
        bot.send_message(message.chat.id, "Введите число: ")
        bot.register_next_step_handler(message, get_value_b)

def get_result(message):
    log_comand(message)
    global a, b, sign
    x = None
    y = None
    res = None
    if flag == "комплексные":
        x = complex(a)
        y = complex(b)
    elif flag == "целые":
        x = int(a)
        y = int(b)
    if sign == '+': res = x + y
    if sign == '-': res = x - y
    if sign == '/': res = x / y
    if sign == '*': res = x * y
    if sign == '%': res = x % y
    if sign == '//': res = x // y
    bot.send_message(message.chat.id, str(res))


bot.infinity_polling()


