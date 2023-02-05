from loader import dp
from aiogram import types
from random import *

total = 150
new_game = False
max_sweets = 28
flag = ''
@dp.message_handler(commands=['start'])
async def mes_start(message: types.Message):
    print(message)

@dp.message_handler(commands=['help'])
async def mes_help(message: types.Message):
    await dp.bot.send_message(message.from_user.id, f"Условие игры: "
                                                    f"\n\t - На столе лежит {total} конфета. "
                                                    f"Играют два игрока, делая ход друг после друга. "
                                                    f"Первый ход определяется жеребьёвкой."
                                                    f"\n\t - За один ход можно забрать не более чем {max_sweets} конфет. "
                                                    f"Все конфеты оппонента достаются сделавшему последний ход.")

@dp.message_handler(commands=['new_game'])
async def mes_new_game(message: types.Message):
    global new_game
    global flag
    new_game = True
    await message.answer(f"Условие игры: "
                         f"\n\t - На столе лежит {total} конфета. "
                         f"Играют два игрока, делая ход друг после друга. "
                         f"Первый ход определяется жеребьёвкой."
                         f"\n\t - За один ход можно забрать не более чем {max_sweets} конфет. "
                         f"Все конфеты оппонента достаются сделавшему последний ход.")
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = types.KeyboardButton("Играть")
    markup.add(but1)
    temp = randint(0, 1)
    if temp == 0:
        flag = 'user'
    else:
        flag = 'bot'
    await message.answer("Если готовы, нажмите 'Играть'", reply_markup=markup)

@dp.message_handler(commands=['set'])
async def mes_set(message: types.Message):
    global total
    global new_game
    count = message.text.split()[1]
    if not new_game:
        if count.isdigit():
            total = int(count)
            await message.answer(f'Конфет теперь будет {count} ')
    else:
        await message.answer(f'{message.from_user.first_name}, нельзя менять правила во время игры')

@dp.message_handler()
async def mes_all(message: types.Message):
    global total, new_game, flag
    if message.text == 'Играть':
        if new_game:
            await message.answer(f'{message.from_user.first_name}, Введите число.')
    elif message.text == 'Ход бота':
        if new_game:
            if total > 0:
                if flag == 'bot':
                    if total <= max_sweets:
                        bot_turn = total
                    elif total % max_sweets == 0:
                        bot_turn = max_sweets - 1
                    else:
                        bot_turn = total % max_sweets - 1
                        if bot_turn == 0:
                            bot_turn = 1
                    total -= bot_turn
                    flag = 'user' if flag == 'bot' else 'bot'
                    await message.answer(f"Бот взял {bot_turn} конфет")
                    await message.answer(f"Осталось {total}")
                    await message.answer(f'{message.from_user.first_name}, cколько конфет вы возьмёте?')
    else:
        if new_game:
            if total > 0:
                if flag == 'user':
                    try:
                        user_turn = int(message.text)
                        if 0 < int(user_turn) < 29:
                            total -= user_turn
                            await message.answer(f"Осталось {total}")
                            flag = 'user' if flag == 'bot' else 'bot'
                            await dp.bot.send_message(message.chat.id, 'Ход бота')
                        else:
                            await message.answer(f"Колличество не должно быть от 1 до {max_sweets}")
                    except ValueError:
                        await message.answer(f'{message.from_user.first_name}, "Введите число."')
                else:
                    if total <= max_sweets:
                        bot_turn = total
                    elif total % max_sweets == 0:
                        bot_turn = max_sweets - 1
                    else:
                        bot_turn = total % max_sweets - 1
                        if bot_turn == 0:
                            bot_turn = 1

                    total -= bot_turn
                    flag = 'user' if flag == 'bot' else 'bot'
                    await message.answer(f"Бот взял {bot_turn} конфет")
                    await message.answer(f"Осталось {total}")
                    await message.answer(f'{message.from_user.first_name}, cколько конфет вы возьмёте?')
        else:
            flag = 'user' if flag == 'bot' else 'bot'
            if flag == 'user':
                await dp.bot.send_message(message.chat.id, f"Поздравляю, {message.from_user.first_name} победили!!")
            else:
                await dp.bot.send_message(message.chat.id, f"Победил bot, в следующий раз вам повезёт(нет).")
            total = 221




