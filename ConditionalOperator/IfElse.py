'''answer = input('Какой язык программирования ты изучаешь?')
if answer == 'Python':
    print('True')
else:
    print('False')'''

'''num1 = int(input())
num2 = int(input())

if num1 > num2:
    print(f'{num1} больше чем {num2}')
if num1 < num2:
    print(f'{num1} меньше чем {num2}')

if num1 == num2:
    print(f'{num1} равен {num2}')
if num1 != num2:
    print(f'{num1} не равен {num2}')

print('Операция завершена')'''

'''age = int(input())

if 1 <= age <= 9:
    print('ребенок')
if 10 <= age <=14:
    print('юноша')
if 15 <= age <= 25:
    print('подросток')
if age >= 26:
    print('взрослый')'''

'''a = int(input())
b = int(input())
c = int(input())

if a == b == c:
    print('числа равны')
else:
    print('числа неравны')'''

#Ex1
'''word = input()
if word == 'Python':
    print('ДА')
else:
    print('НЕТ')'''

#Ex2
'''num = int(input())
first_digit = num // 10
second_digit = num % 10

if first_digit == second_digit:
    print('ДА. Число состоит из одинаковых цифр')
else:
    print('НЕТ. Число не состоит из одинаковых цифр')'''

#Ex3
'''num1, num2, num3 = int(input()), int(input()), int(input())

counter = 0  
if num1 % 2 == 0:
    counter = counter + 1 
if num2 % 2 == 0:
    counter = counter + 1 
if num3 % 2 == 0:
    counter = counter + 1  

print(counter)'''

'''password1 = input()
password2 = input()

if password1 == password2:
    print('Пароль принят')
else:
    print('Пароль не принят')'''

'''a = int(input())
if a % 2 == 0:
    print('Четное')
else:
    print('Нечетное')'''

'''x = int(input())
first, second, third, fourth = x // 1000, (x % 1000) // 100, (x % 100) // 10, x % 10
summa, raznost = first + fourth, second - third

if summa == raznost:
    print('ДА')
else:
    print('НЕТ')'''

'''age = int(input())
if age < 18:
    print('Доступ запрещен')
else:
    print('Доступ разрешен')'''

'''a, b, c = int(input()), int(input()), int(input())
if (b - a) + b == c:
    print('YES')
else:
    print('NO')'''

'''num1, num2 = int(input()), int(input())
if num1 < num2:
    print(num1)
if num1 > num2:
    print(num2)'''

'''a, b, c, d = int(input()), int(input()), int(input()), int(input())
min_num = a

if b < min_num:
    min_num = b
if c < min_num:
    min_num = c
if d < min_num:
    min_num = d

print(min_num)'''

'''age = int(input())
if age <= 13:
    print('детство')
if 14 <= age <= 24:
    print('молодость')
if 25 <= age <= 59:
    print('зрелость')
if age >= 60:
    print('старость')'''

a, b, c = int(input()), int(input()), int(input())
sum = 0
if a > 0:
    sum += a
if b > 0:
    sum += b
if c > 0:
    sum += c

print(sum)