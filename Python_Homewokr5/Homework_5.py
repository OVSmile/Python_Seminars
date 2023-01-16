
# ____________________8. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".(Задание из семинара)____________

data = 'аф фыв ыва ываабв, ывадлойц. Оывало абвываф, длоываабв.'

data=' '.join(list(filter(lambda slovo: not 'абв' in slovo, data.split())))
print(data)
#
# _________________________________________________39(1). Игра "Конфеты"_____________________________________

from random import*
number_candies = 221

# Алгоритм жеребьёвки
def FirstMove():
      print("Узнаем, кто сделает первый ход, выберете 'орел' или 'решка'!")
      print("Программа управления игрой подбрасывает биткоин.")
      temp = randint(0, 1)
      if temp == 0:
            return 'орел'
      else:
            return 'решка'

# Алгоритм работы бота (рандом)
def easy_bot(candies):
      if candies > 28:
            return randint(1, 29)
      else:
            return candies

# Алгоритм работы бота (ИИ)
def hard_bot(candies, player_num):
      if candies > 28:
            if player_num == 0:
                  return randint(1, 29)
            else:
                  temp = 29 - player_num
                  return temp
      else:
            return candies

# Вриант 1. Игра Player 1 VS Player 2
def player_VS_player(candies):
      player_name_1 = input("\nИгрок 1, введите ваше имя: ")
      player_name_2 = input("Игрок 2, Введите ваше имя: ")

      f1 = FirstMove()

      PlayerChoise = input(f"{player_name_1} выбирайте: ")
      if PlayerChoise == f1:
            print(f'Верно! Вы угадали, делайте первый ход!')
      else:
            print(f'Неверно! Право первого хода переходит к {player_name_2}!')
            player = player_name_2

      while candies > 0:
            temp = int(input(f'{player} ваш ход: '))
            if 0 < temp <= 28:
                  if candies - temp == 0:
                        print(f'{player}, поздравляю! Вы победили! Все конфеты достаются вам!')
                        break
                  elif candies < temp:
                        print(f'Нельзя взять больше {candies} кофет.')
                  else:
                        print(f'Осталось {candies - temp} конфет')
                        if player == player_name_2:
                              player = player_name_1
                        else:
                              player = player_name_2
                        candies -= temp
            else:
                  print('Можно взять не больше 28-ми кофет за ход')

# Вариант 2. Игра Player 1 VS Bot (level: Easy)
def player_VS_bot1(candies):
      player_name_1 = input("\nИгрок 1, введите ваше имя: ")
      player_name_2 = 'Бот "Простак"'

      f1 = FirstMove()

      PlayerChoise = input(f"{player_name_1} выбирайте: ")
      if PlayerChoise == f1:
            print(f'Верно! Вы угадали, делайте первый ход!')
            player = player_name_1
      else:
            print(f'Неверно! Право первого хода переходит к {player_name_2}!')
            player = player_name_2

      while candies > 0:
            if player == player_name_1:
                  temp = int(input(f'{player} ваш ход: '))
            else:
                  temp = easy_bot(candies)
                  print(f'{player} делает ход: {temp}')

            if 0 < temp <= 28:
                  if candies - temp == 0:
                        print(f'{player}, поздравляю! Вы победили! Все конфеты достаются вам!')
                        break
                  elif candies < temp:
                        print(f'Нельзя взять больше {candies} конфет.')
                  else:
                        print(f'Осталось {candies - temp} конфет')
                        if player == player_name_2:
                              player = player_name_1
                        else:
                              player = player_name_2
                        candies -= temp
            else:
                  print('Можно взять не больше 28-ми кофет за ход')

# Вариант 3. Игра Player 1 VS Bot (level: Hard)
def player_VS_bot2(candies):
      player_name_1 = input("\nИгрок 1, введите ваше имя: ")
      player_name_2 = 'Бот "Бывалый"'
      player_num = 0

      f1 = FirstMove()

      PlayerChoise = input(f"{player_name_1} выбирайте: ")
      if PlayerChoise == f1:
            print(f'Верно! Вы угадали, делайте первый ход!')
            player = player_name_1
      else:
            print(f'Неверно! Право первого хода переходит к {player_name_2}!')
            player = player_name_2

      while candies > 0:
            if player == player_name_1:
                  temp = int(input(f'{player} ваш ход: '))
                  player_num = temp
            else:
                  temp = hard_bot(candies, player_num)
                  print(f'{player} делает ход: {temp}')
                  player_num = 0

            if 0 < temp <= 28:
                  if candies - temp == 0:
                        print(f'{player}, поздравляю! Вы победили! Все конфеты достаются вам!')
                        break
                  elif candies < temp:
                        print(f'Нельзя взять больше {candies} конфет.')
                  else:
                        print(f'Осталось {candies - temp} конфет')
                        if player == player_name_2:
                              player = player_name_1
                        else:
                              player = player_name_2
                        candies -= temp
            else:
                  print('Можно взять не больше 28-ми кофет за ход')


print("Добро пожаловать в игру 'Конфетки'!")
print()
print("Условие игры: "
      "\n\t - На столе лежит 221 конфета. Играют два игрока, делая ход друг после друга. Первый ход определяется жеребьёвкой."
      "\n\t - За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.")

#Выбор режима игры
print('Варианты сложности: '
                  '\n\t1. Игрок 1 против Игрок 2'
                  '\n\t2. Игрок против Бота (легкий уровень)'
                  '\n\t3. Игрок против Бота (сложный уровень)')

level = int(input('Введите номер варианта игры: '))
if level == 1:
      player_VS_player(number_candies)
elif level == 2:
      player_VS_bot1(number_candies)
elif level == 3:
      player_VS_bot2(number_candies)

# __________________________________________39(2). Создайте программу для игры в "Крестики-нолики"_______________________________________


from random import*

# Алгоритм жеребьёвки
def FirstMove():
      print("Узнаем, кто сделает первый ход, выберете 'орел' или 'решка'!")
      print("Программа управления игрой подбрасывает биткоин.")
      temp = randint(0, 1)
      if temp == 0:
            return 'орел'
      else:
            return 'решка'

def player_VS_player():
    game_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    player_name_1 = input("\nИгрок 1, введите ваше имя: ")
    player_name_2 = input("Игрок 2, Введите ваше имя: ")

    f1 = FirstMove()

    PlayerChoise = input(f"{player_name_1} выбирайте: ")
    if PlayerChoise == f1:
        print(f'Верно! Вы угадали, делайте первый ход!')
        player = player_name_1
    else:
        print(f'Неверно! Право первого хода переходит к {player_name_2}!')
        player = player_name_2

    print(f"|{'|'.join(game_list[:3])}|\n|{'|'.join(game_list[3:6])}|\n|{'|'.join(game_list[6:9])}|")

    move = 0
    while move < 9:
        num = int(input(f'{player}, введите номер клетки: '))

        if game_list[num - 1].isdigit():
            if move % 2 == 0:
                game_list[num - 1] = 'X'
            else:
                game_list[num - 1] = 'O'
        print(f"|{'|'.join(game_list[:3])}|\n|{'|'.join(game_list[3:6])}|\n|{'|'.join(game_list[6:9])}|")

        if (game_list[0] == game_list[1] == game_list[2] or
            game_list[3] == game_list[4] == game_list[5] or
            game_list[6] == game_list[7] == game_list[8] or
            game_list[0] == game_list[3] == game_list[6] or
            game_list[1] == game_list[4] == game_list[7] or
            game_list[2] == game_list[4] == game_list[8] or
            game_list[0] == game_list[4] == game_list[8] or
            game_list[2] == game_list[4] == game_list[6]):
            print(f'Выйграл {player}!')
            print(f"|{'|'.join(game_list[:3])}|\n|{'|'.join(game_list[3:6])}|\n|{'|'.join(game_list[6:9])}|")
            break

        if player == player_name_2:
            player = player_name_1
        else:
            player = player_name_2
        move += 1
    else:
        print('Ничья!')


player_VS_player()


# ___________________________40. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.______________________________________

def rle_emcode(data):
    encoding = ''
    prev_char = ''
    count = 0

    if not data: return ''

    for char in data:
        if char != prev_char:
            if prev_char:
                encoding += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    else:
        encoding += str(count) + prev_char
        return encoding

#encoded_text = rle_emcode('AAAAAAFFFFFFgggggggKLLtEEE')
encoded_text = rle_emcode('1111112225555888889')
print(encoded_text)

def rle_decode(data):
    decode = ''
    count = ''
    for i in range(len(data)):
        if i % 2 == 0:
            count += data[i]
        else:
            decode += (data[i]) * int(count)
            count = ''
    return decode

encoded_text = rle_decode(encoded_text)
print(encoded_text)