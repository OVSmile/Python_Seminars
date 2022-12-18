# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11
number = input('Введите число: ')
print(f'{number} ->', end=' ')
number = number.split('.')
sum = 0

for i in number:
    i = int(i)
    while i > 0:
        sum += i % 10
        i = i // 10
print(sum)
#____________________________________________________________________________________________________________

# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
n = int(input("Введите число N: "))
my_list = []
factorial = 1
for i in range(1, n + 1):
    factorial *= i
    i -= 1
    my_list.append(factorial)
print(f'N = {n}, тогда набор произведений чисел от 1 до N {my_list}')
#___________________________________________________________________________________________________________

# Задайте список из n чисел последовательности $(1+1/n)**n$ и выведите на экран их сумму.
# Пример:
#- Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44}

n = int(input('Введите число n: '))
my_list = {}
for i in range(1, n + 1):
    my_list[i] = round((1 + 1 / i) ** i, 2)
print(f'Для n = {n} {my_list}')
print(f'Сумма {sum(my_list.values())}')
#__________________________________________________________________________________________________________

# Реализуйте алгоритм перемешивания списка.
import random
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(my_list)
index = random.randint(0, 9)
temp = None
index_list = []
for i in range(len(my_list)):
    if my_list[i] in index_list:
        break
    index_list.append(i)
    while index in index_list:
        index = random.randint(0, 9)
    index_list.append(index)
    temp = my_list[index]
    my_list[index] = my_list[i]
    my_list[i] = temp

print(my_list)
#_________________________________________________________________________________________________________

# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

import os
os.system(r'nul>listN.txt')

N = int(input('Enter number: '))
my_list = []
for i in range(-N, N + 1):
    my_list.append(i)
print(F'list [-N:N]: {my_list}')

pos1, pos2 = int(input('Enter the index of the first element: ')), int(input('Enter the index of the second element: '))
list_positions = [pos1, pos2]
data = open('listN.txt', 'a')
for i in range(len(list_positions)):
    data.write(f'{list_positions[i]}\n')
data.close()

count = 1
path = 'listN.txt'
data = open(path, 'r')
for line in data:
    count *= my_list[int(line)]
print(f'Product of list items -> {count}')




