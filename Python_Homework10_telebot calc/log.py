from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import telebot
from telebot import types
def log_comand(update: Update):
    file = open('log.csv', 'a')
    file.write(f'{update.message.text}')
    file.close()