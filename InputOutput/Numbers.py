'''a = 3
b = 2
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)'''

'''num1 = 4
num2 = 2
print(num1 + num2 * num1)
print((num1 + num2) * num1)'''

'''s = '1992'
year = int(s)
print(type(s))
print(type(year))'''

'''num1 = input()
num2 = input()
print(num1 + num2)''' #суммируется ка текст

'''num1 = int(input())
num2 = int(input())
print(num1 + num2)'''

'''num = 17
s = str(num)
print(type(num), num)
print(type(s), s)'''

'''a = int(input())
b = a + 1
c = a + 2
print(a)
print(b)
print(c)'''

'''a = int(input())
b = int(input())
c = int(input())
d = int(input())
result = (a + b + c + d) * 3
print(result)'''

'''a = int(input())
b = int(input())
func = 3 * (a + b) ** 3 + 275 * b ** 2 - 127 * a - 41
print(func)'''

'''a = int(input())
b = a + 1
c = a - 1
print('Следующее за числом', a, 'число:', b)
print('Для числа', a, 'предыдущее число:', c)'''

'''a = int(input())
V = a * a * a
S = 6 * (a * a)
print('Объем =', V)
print('Площадь полной поверхности =', S)'''

'''a = int(input())
b = int(input())
print(a, '+', b, '=', a+b)
print(a, '-', b, '=', a-b)
print(a, '*', b, '=', a*b)'''

'''a = int(input())
d = int(input())
n = int(input())
an = a + d * (n - 1)
print(an)'''

'''x = int(input())
a, b, c, d = 2 * x, 3 * x, 4 * x, 5 * x
print(x, a, b, c, d, sep='---')'''

'''print(10 // 3)
print(10 // 4)
print(10 // 5)
print(10 // 6)
print(10 // 12)'''

'''a = 15 // (16 % 7)
b = 34 % a * 5 - 29 % 5 * 2
print(a+b)'''

'''b = int(input())
q = int(input())
n = int(input())
print(b * q ** (n - 1))'''

'''x = int(input())
print(x // 100)'''

'''n = int(input())
k = int(input())
print(k // n)
print(k % n)'''

#print((int(input())+1)//2)

'''xmin = int(input())
hour, min = xmin // 60, xmin % 60
print(xmin, 'мин - это', hour, 'час', min, 'минут.')'''


#print(int(input()) // -4 * -1)

# последняя цифра числа определяется всегда как остаток от деления числа на 10 (% 10).
# Чтобы отщепить последнюю цифру от числа, необходимо разделить его нацело на 10 (// 10).

'''num = 754
a = num % 10
b = (num % 100) // 10
c = num // 100
print(a)
print(b)
print(c)'''

'''x = int(input())
last = x % 10
second = (x % 100) // 10
first = x // 100
print('Сумма цифр =', first + second + last)
print('Произведение цифр =', first * second * last)'''

'''x = int(input())
c, b, a = x % 10, (x % 100) // 10,  x // 100
print(a, b, c, sep='')
print(a, c, b, sep='')
print(b, a, c, sep='')
print(b, c, a, sep='')
print(c, a, b, sep='')
print(c, b, a, sep='')'''

'''x = int(input())
first, second, third, fourth = x // 1000, (x % 1000) // 100, (x % 100) // 10, x % 10
print('Цифра в позиции тысяч равна', first)
print('Цифра в позиции сотен равна', second)
print('Цифра в позиции десятков равна', third)
print('Цифра в позиции единиц равна', fourth)'''



