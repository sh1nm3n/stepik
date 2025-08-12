from math import *

'''print(sqrt(121)) #квадратный корень
print(ceil(3.6)) #округление числа вверх
print(floor(3.6)) #округление числа вниз
print(round(1.55)) #округление
print(round(sqrt(13), 2)) #округление до n чисел после точки
print(fabs(-4.65)) #модуль
print(pow(3, 4)) #возведение в степень
print(log(4, 3)) #логарифм/логарифм числа по основанию
print(log10(5)) #десятичный логарифм
print(factorial(3)) #факториал

print()

print(degrees(1.4)) #радианы в градусы
print(radians(90)) #градусы в радианы
print(cos(190)) #косинус угла в радианах
print(sin(190))
print(tan(190))

print()

print(pi) #константа пи
print(e) #константа эйлера'''

'''x1, y1, x2, y2 = float(input()), float(input()), float(input()), float(input())
euclide = sqrt(pow((x1 - x2), 2) + pow((y1 - y2), 2))
print(euclide)'''

'''R = float(input())
S, C = pi * pow(R, 2), 2 * pi * R
print(S)
print(C)'''

'''a, b = float(input()), float(input())
x1 = (a + b) / 2
x2 = sqrt(a * b)
x3 = (2 * a * b) / (a + b)
x4 = sqrt((pow(a, 2) + pow(b, 2)) / 2)
print(x1)
print(x2)
print(x3)
print(x4)'''

'''x = float(input())
rad = (x * pi) / 180
trigan = sin(rad) + cos(rad) + (tan(rad) * tan(rad))
print(trigan)'''

'''x = float(input())
_ceil = ceil(x)
_floor = floor(x)
print(_ceil + _floor)'''

'''a, b, c = float(input()), float(input()), float(input())
D = (b ** 2) - 4 * (a * c)
if D < 0:
    print('Нет корней')
elif D == 0:
    x = - (b / (2 * a))
    print(x)
elif D > 0:
    x1 = (-b - D ** 0.5) / (2 * a)
    x2 = (-b + D ** 0.5) / (2 * a)
    print(min(x1, x2))
    print(max(x1, x2))'''

n, a = int(input()), float(input())
S = n * (a ** 2) / (4 * tan(pi / n))
print(S)