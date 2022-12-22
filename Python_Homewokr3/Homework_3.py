# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
#
from random import *
my_list = []
for i in range(randint(3, 10)):
    my_list.append(randint(0, 20))
print(my_list)
sum = 0
for i in range(1, len(my_list) - 1, 2):
    sum += my_list[i]
print(sum)
#_________________________________________________________________________________________________________________________________

# 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

from random import *
my_list = [randint(0, 20) for i in range(randint(2, 10))]
print(my_list)
productNumbers = []
for i in range(len(my_list) // 2 + len(my_list) % 2):
    productNumbers.append(my_list[i] * my_list[-i - 1])
print(productNumbers)
#________________________________________________________________________________________________________________________________

# 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

from random import *
my_list = [round(uniform(0, 20), 2) for i in range(randint(2, 10))]
print(my_list)
fractionalPart = []
for i in range(len(my_list)):
    fract = my_list[i] % 1
    if fract != 0:
        fractionalPart.append(round(fract, 2))
print(fractionalPart)
print(max(fractionalPart) - min(fractionalPart))
#_______________________________________________________________________________________________________________________________

# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

n = int(input("Введите десятичное число: "))
print(f'Число {n} в двоичном представлении {bin(n)[2:]}')
#_______________________________________________________________________________________________________________________________
#
# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def positive_fib(n):
    positive_list = [0, 1]
    for i in range(n - 1):
        positive_list.append(positive_list[-2] + positive_list[-1])
    return positive_list

def negative_fiv(n):
    negative_list = [1, 0]
    for i in range(n - 1):
        negative_list.insert(0, negative_list[1] - negative_list[0])
    return negative_list

print(negative_fiv(8) + positive_fib(8)[1:])



