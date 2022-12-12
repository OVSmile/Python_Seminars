# 6. Напишите программу, которая принимает на вход цифру,
# обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:

day_number = int(input("Enter the number of the day of the week: "))
if day_number > 7 or day_number < 1:
    print("Incorrect input")
else:
    print("{day_number} -> Yes" if day_number == 6 or day_number == 7 else "{day_number} -> No")
#_____________________________________________________________________________________________________________________________

#7. Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

for i in range(2):
    for j in range(2):
        for k in range(2):
            print(not(i or j or k) == (not i) and (not j) and (not k))
#_____________________________________________________________________________________________________________________________

#8. Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0
#   и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

x = int(input("Enter X: "))
y = int(input("Enter Y: "))
if x > 0 and y > 0:
    print(f"X={x}; Y={y} -> 1")
elif x < 0 and y > 0:
    print(f"X={x}; Y={y} -> 2")
elif x < 0 and y < 0:
    print(f"X={x}; Y={y} -> 3")
else:
    print(f"X={x}; Y={y} -> 4")
#_____________________________________________________________________________________________________________________________

#9. Напишите программу, которая по заданному номеру четверти,
#   показывает диапазон возможных координат точек в этой четверти (x и y).

quarter_number = int(input("Enter quarter number: "))
if quarter_number == 1:
    print("x > 0; y > 0")
elif quarter_number == 2:
    print("x < 0; y > 0")
elif quarter_number == 3:
    print("x < 0; y < 0")
else:
    print("x > 0; y < 0")
#_____________________________________________________________________________________________________________________________

#10. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

import math
print("Enter coordinates of point A")
Ax = int(input("Enter X: "))
Ay = int(input("Enter Y: "))

print("Enter coordinates of point B")
Bx = int(input("Enter X: "))
By = int(input("Enter Y: "))

print(f"A ({Ax},{Ay}); B ({Bx},{By}) -> {math.sqrt(pow(Ax - Bx, 2) + pow(Ay - By, 2))}")
