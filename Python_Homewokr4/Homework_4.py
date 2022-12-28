# 30. Вычислить число с заданной точностю

# from math import*
#
# number = int(input('Введите число: '))
# print(round(pi, number))
#_______________________________________________________________________________________________________

# 31. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

# num = int(input())
# count = 0
# list_num = []
# while num != 1:
#     if num % 2 == 0:
#         list_num.append(2)
#         num = num / 2
#     elif num % 3 == 0:
#         list_num.append(3)
#         num = num / 3
#     elif num % 5 == 0:
#         list_num.append(5)
#         num = num / 5
#     else:
#         list_num.append(int(num))
#         break
#
# print(list_num)
#_____________________________________________________________________________________________________

# 32. Задайте последователтность чисел. Наптшите программу,
# которая выведет список неповторяющихся элементов исходной последовательности

# from random import *
# numbers_list = [randint(0, 20) for i in range(randint(5, 10))]
# print(numbers_list)
# numbers_list2 = []
# for value in numbers_list:
#     if numbers_list.count(value) == 1:
#         numbers_list2.append(value)
# print(numbers_list2)
#______________________________________________________________________________________________________
# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# from random import *
# k = int(input('Введите максимальную степень: '))
# equation = {}
#
# for i in range(k, -1, -1):
#     equation[i] = randint(0, 100)
# print(equation)
#
# eq_str = ''
# for key, coeff in equation.items():
#     if key == 1:
#         if coeff != 0:
#             eq_str += f'{coeff}*x + '
#     elif key == 0:
#         if coeff != 0:
#             eq_str += f'{coeff}'
#     else:
#         if coeff != 0:
#             eq_str += f'{coeff}*x**{key} + '
# data = open('equations2.txt', 'a')
# data.write(f'{eq_str} = 0')
# data.close()
#______________________________________________________________________________________________________
# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.
path1 = 'equations.txt'
path2 = 'equations2.txt'

def eq_str(path):
    eq = ''
    data = open(path, 'r')
    for line in data:
        eq += line
    return eq

eq_str_1 = eq_str(path1)
eq_str_2 = eq_str(path2)
print(eq_str_1)
print(eq_str_2)

eq_str_1 = eq_str_1[1:-6].split(' + ')
eq_str_2 = eq_str_2[0:-5].split(' + ')
print(eq_str_1)
print(eq_str_2)

k1 = int(eq_str_1[0][-1])
k2 = int(eq_str_2[0][-1])


def dict_eq(eq, k):
    result = {}
    for key in range(k, -1, -1):
        if key > 1:
            if key == int(eq[-key - 1][-1]):
                result[key] = int(eq[-key - 1][:-5])
            else:
                result[key] = 0
        elif key == 1:
            if 'x' == str(eq[-key-1][-1]):
                result[key] = int(eq[-key - 1][:-2])
            else:
                result[key] = 0
        elif key == 0:
            if eq_str_1[key].isdigit:
                result[key] = int(eq[k])
            else:
                result[key] = 0
    return result

equation1 = dict_eq(eq_str_1, k1)
equation2 = dict_eq(eq_str_2, k2)
print(equation1)
print(equation2)


def dicts_sum(d1, d2):
    k = set(list(d1.keys()) + list(d2.keys()))
    sorted(k, reverse=True)
    dict_result = {}
    for i in range(len(k) - 1, -1, -1):
        v1 = d1.get(i)
        v2 = d2.get(i)
        if v1 == None:
            v = v2
        elif v2 == None:
            v = v1
        else:
            v = v1 + v2
        dict_result[i] = v
    return dict_result

equation3 = dicts_sum(equation1, equation2)

print(equation3)

eq3_str = ''
for key, coeff in equation3.items():
    if key == 1:
        if coeff != 0:
            eq3_str += f'{coeff}*x + '
    elif key == 0:
        if coeff != 0:
            eq3_str += f'{coeff}'
    else:
        if coeff != 0:
            eq3_str += f'{coeff}*x**{key} + '
data = open('equations3.txt', 'a')
data.write(f'{eq3_str} = 0')
data.close()