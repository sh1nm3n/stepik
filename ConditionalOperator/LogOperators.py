#operator AND
'''age = int(input('Сколько вам лет?'))
grade = int(input('В каком классе вы обучаетесь?'))
city = str(input('В каком городе вы живете?'))

if age >= 14 and 7 <= grade <= 11 and city == 'Ростов':
    print('Доступ разрешен')
else:
    print('Доступ запрещен')'''

#operator OR
'''city = str(input('В каком городе вы живете?'))
if city == 'Москва' or city == 'Ростов' or city == 'Батайск':
    print('Отлично')
else:
    print('False')'''

#operator NOT
'''age = int(input())
if not (age < 12):
    print('OKAY')
else:
    print('False')
'''

'''num = int(input())
if 100 <= num <= 999:
    print('число трехзначное')
else:
    print('число не трехзначное')'''

'''num = int(input())
fd, sd, td = num // 100, (num % 100) // 10, num % 10
if fd != sd and sd != td and td != fd:
    print(f'все цифры числа {num} различны')
else:
    print('цифры числа не отличаются друг от друга')'''

'''num1 = 34
num2 = 81
if num1 // 9 == 0 or num2 % 9 == 0:
    print('число', num1, 'выиграло')
else:
    print('число', num2, 'выиграло')'''

'''x = int(input())
if -1 < x < 17:
    print('Принадлежит')
else:
    print('Не принадлежит')'''

'''x = int(input())
if x <= -3 or x >= 7:
    print('Принадлежит')
else:
    print('Не принадлежит')'''

'''x = int(input())
if -30 < x <= -2 or 7 < x <= 25:
    print('Принадлежит')
else:
    print('Не принадлежит')'''

'''x = int(input())
if 1000 <= x <= 9999 and ((x // 7) * 7 == x or (x // 17) * 17 == x):
    print('YES')
else:
    print('NO')'''

'''a, b, c = int(input()), int(input()), int(input())
x1, x2, x3 = a + b, a + c, b + c
if x1 > c and x2 > b and x3 > a:
    print('YES')
else:
    print('NO')'''

'''year = int(input())
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print('YES')
else:
    print('NO')'''

'''x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
if -1 <= (x1 - x2) <= 1 and -1 <= (y1 - y2) <= 1:
    print("YES")
else:
    print("NO")'''

'''point = int(input('Введите свой балл от 0 до 100: '))

if 75 <= point <= 100:
    print('Оценка: 5')
elif 50 <= point < 75:
    print('Оценка: 4')
elif 25 < point <= 50:
    print('Оценка: 3')
elif 0 <= point < 25:
    print('Оценка: 2')
else:
    print('Ошибка')'''

'''a, b, c = int(input()), int(input()), int(input())
if a == b == c:
    print('3')
elif a == b:
    print('2')
elif a == c:
    print('2')
elif b == c:
    print('2')
else:
    print('0')'''

'''n, k = int(input()), int(input())
if n > k:
    print('NO')
elif n < k:
    print('YES')
elif n == k:
    print("Don't know")'''

'''a, b, c = int(input()), int(input()), int(input())
if a == b == c:
    print('Равносторонний')
elif a == b > c or a == c > b or b == c > a:
    print('Равнобедренный')
elif a != b and b != c and a != c:
    print('Разносторонний')'''

'''a, b, c = int(input()), int(input()), int(input())
if (a > b > c) or (c > b > a):
    print(b)
elif (c > a > b) or (b > a > c):
    print(a)
else:
    print(c)
'''

'''month = int(input())
if month == 2:
    print('28')
elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    print('31')
else:
    print('30')'''

'''a = int(input())
if a < 60:
    print('Легкий вес')
elif 60 <= a < 64:
    print('Первый полусредний вес')
else:
    print('Полусредний вес')'''

'''a, b, c = int(input()), int(input()), input()
if c == '+':
    print(a + b)
elif c == '-':
    print(a - b)
elif c == '*':
    print(a * b)
elif c == '/':
    if b == 0:
        print('На ноль делить нельзя!')
    else:
        print(a / b)
else:
    print('Неверная операция')'''

'''a, b = str(input()), str(input())
if (a == 'красный' and b == 'синий') or (a == 'синий' and b == 'красный'):
    print('фиолетовый')
elif (a == 'красный' and b == 'желтый') or (a == 'желтый' and b == 'красный'):
    print('оранжевый')
elif (a == 'синий' and b == 'желтый') or (a == 'желтый' and b == 'синий'):
    print('зеленый')
elif (a != 'красный' and a != 'желтый' and a != 'синий') or (b != 'красный' and b != 'желтый' and b != 'синий'):
    print('ошибка цвета')
else:
    print(b)'''

'''pocket = int(input())
if pocket == 0:
    print('зеленый')
elif (1 <= pocket <= 10) or (19 <= pocket <= 28):
    if pocket % 2 == 0:
        print('черный')
    else:
        print('красный')
elif (11 <= pocket <= 18) or (29 <= pocket <= 36):
    if pocket % 2 == 0:
        print('красный')
    else:
        print('черный')
else:
    print('ошибка ввода')'''

'''year = int(input())
fd, td = year % 100, year % 10
if fd == 0 and td == 0:
    print('YES')
else:
    print('NO')'''

x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
if ((x1 + y1) % 2 == 0 and (x2 + y2) % 2 == 0) or ((x1 + y1) % 2 != 0 and (x2 + y2) % 2 != 0):
    print('YES')
else:
    print('NO')