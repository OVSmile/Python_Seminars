# Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент,
# разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
# Ввод: 7 2 5
# Вывод: 7 9 11 13 15
#
# a1 = int(input(f'Введите первый элемент последовательености: '))
# n = int(input(f'Введите значение разности между элементами последовательности: '))
# d = int(input(f'Введите колличество элементов: '))
# print(a1, n, d)
# for i in range(1, n+1):
#     an = a1 + (i-1) * d
#     print(an, end=' ')
#
# print('\n')
#
# an = [str(a1 + (i-1) * d) for i in range(1, n+1)]
# print(' '.join(an))


# Задача 31: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)
# Ввод:  [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# 5
# 15
# Вывод: [1, 9, 13, 14, 19]
# from random import*
#
# num_list = []
# for i in range(20):
#     num_list.append(randint(-100, 100))
# min_num = int(input(f'Введите минимальное число диапазона: '))
# max_num = int(input(f'Введите максималльное число диапазона: '))
# print(num_list)
# new_list = []
# for i in num_list:
#     if min_num <= i <= max_num:
#         new_list.append(i)
# print(new_list)
#
# print('\n')
#
# num_list = [randint(-100, 100) for i in range(20)]
# print(num_list)
# new_list = list(filter(lambda x: min_num <= x <= max_num, num_list))
# print(new_list)

# Задача 32:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8
A, B = int(input("Введите число А: ")), int(input("Введите число В: "))
# def power(a, b):
#     if b == 1:
#         return a
#     return a * power(a, b - 1)
#
# print(f'A = {A}; B= {B} -> {power(A, B)}')

res = lambda a, b: a ** b
print(res(A, B))

