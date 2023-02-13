import random
import emoji
from aiogram import types
from loader import dp



max_count = 150
total = 0
new_game = False
duel = []
first = 0
current = 0


@dp.message_handler(commands=['start', 'старт'])
async def mes_start(message: types.Message):
    name = message.from_user.first_name
    await message.answer(f'{name}, привет! Сегодня сыграем с тобой в конфеты! Для начала игры введи команду /new_game. '
                         f'Для настройки конфет введи команду /set и укажи количество конфет\n'
                         f'Или /duel и id оппонента, для игры вдвоем')
    print(message.from_user.id)


@dp.message_handler(commands=['new_game'])
async def mes_new_game(message: types.Message):
    global new_game
    global total
    global max_count
    global first
    new_game = True
    total = max_count
    first = random.randint(0,1)
    if first:
        await message.answer(f'Игра началась. По жребию первым ходит {message.from_user.first_name}! Бери конфеты...')
    else:
        await message.answer(f'Игра началась. По жребию первым ходит Ботяо')
        await bot_turn(message)


@dp.message_handler(commands=['duel'])
async def mes_duel(message: types.Message):
    global new_game
    global total
    global max_count
    global duel
    global first
    global current
    duel.append(int(message.from_user.id))
    duel.append(int(message.text.split()[1]))
    total = max_count
    first = random.randint(0,1)
    if first:
        await dp.bot.send_message(duel[0], 'Первый ход за тобой, бери конфеты')
        await dp.bot.send_message(duel[1], 'Первый ход за твоим противником! Жди своего хода')
    else:
        await dp.bot.send_message(duel[1], 'Первый ход за тобой, бери конфеты')
        await dp.bot.send_message(duel[0], 'Первый ход за твоим противником! Жди своего хода')
    current = duel[0] if first else duel[1]
    new_game = True


@dp.message_handler(commands=['set'])
async def mes_set(message: types.Message):
    global max_count
    global new_game
    name = message.from_user.first_name
    count = message.text.split()[1]
    if not new_game:
        if count.isdigit():
            max_count = int(count)
            await message.answer(f'Конфет теперь будет {max_count}, {emoji.emojize(":thumbs_up:")}')
        else:
            await message.answer(f'{name}, напишите цифрами')
    else:
        await message.answer(f'{name}, нельзя менять правила во время игры')


@dp.message_handler()
async def mes_take_candy(message: types.Message):
    global new_game
    global total
    global max_count
    global duel
    global first
    name = message.from_user.first_name
    count = message.text
    y = ''
    if len(duel) == 0:
        if new_game:
            if message.text.isdigit() and 0 < int(message.text) < 29:
                total -= int(message.text)
                if total <= 0:
                    await message.answer(f'Ура! {name} ты победил!{emoji.emojize(":candies:")}')
                    new_game = False
                else:
                    if int(message.text) in [1, 21]: y = 'у'
                    elif int(message.text) in [2, 3, 4, 22, 23, 24]: y = 'ы'

                    await message.answer(f'{name} взял {message.text} конфет{y}. '
                                         f'На столе осталось {total}')
                    await bot_turn(message)
            else:
                await message.answer(f'{name}, надо указать ЧИСЛО от 1 до 28!')
    else:
        if current == int(message.from_user.id):
            name = message.from_user.first_name
            count = message.text
            if new_game:
                if message.text.isdigit() and 0 < int(message.text) < 29:
                    total -= int(message.text)
                    if total <= 0:
                        await message.answer(f'Ура! {name} ты победил!{emoji.emojize(":candies:")}')
                        await dp.bot.send_message(enemy_id(), f'К сожалению ты проиграл! Твой оппонент оказался умнее! '
                                                              f'{emoji.emojize(":worried:")}')
                        new_game = False
                    else:
                        if int(message.text) in [1, 21]: y = 'у'
                        elif int(message.text) in [2, 3, 4, 22, 23, 24]: y = 'ы'

                        await message.answer(f'{name} взял {message.text} конфет{y}. '
                                             f'На столе осталось {total}')
                        await dp.bot.send_message(enemy_id(), f'Теперь твой ход, бери конфеты! На столе осталось ровно {total}')
                        switch_players()
                else:
                    await message.answer(f'{name}, надо указать ЧИСЛО от 1 до 28!')


async def bot_turn(message: types.Message):
    global total
    global new_game
    bot_take = 0
    y = ''
    if 0 < total < 29:
        bot_take = total
        total -= bot_take

        if bot_take in [1, 21]: y = 'у'
        elif bot_take in [2, 3, 4, 22, 23, 24]:  y = 'ы'

        await message.answer(f'Бот взял {bot_take} конфет{y}. '
                             f'На столе осталось {total} и бот одержал победу {emoji.emojize(":stuck_out_tongue_closed_eyes:")}')
        new_game = False

    else:
        remainder = total%29
        bot_take = remainder if remainder != 0 else 28
        total -= bot_take

        if bot_take in [1, 21]: y = 'у'
        elif bot_take in [2, 3, 4, 22, 23, 24]: y = 'ы'

        await message.answer(f'Бот взял {bot_take} конфет{y}. '
                             f'На столе осталось {total}')

def switch_players():
    global duel
    global current
    if current == duel[0]:
        current = duel[1]
    else:
        current = duel[0]


def enemy_id():
    global duel
    global current
    if current == duel[0]:
        return duel[1]
    else:
        return duel[0]




