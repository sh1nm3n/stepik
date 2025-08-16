'''s = 'PyThoN LaNguAge iS vEry bEautIfUl'
print(s)
print(s.capitalize())
print(s.swapcase())
print(s.title())
print(s.upper())
print(s.lower())'''

'''s = input()
title = s.title()
print('YES' if s == title else 'NO')'''

'''s = input()
lower = 'abcdefghijklmnopqrstuvwxyz'
count = 0

for i in range(len(s)):
    if s[i] in lower:
        count += 1

print(count)'''

'''s = 'Pyy Lyy Kyy'
print(s.count('yy'))
print(s.count('yy', 0, 7))'''

'''s2 = 'loobop'
print(s2.startswith('loo'))
print(s2.startswith('bo'))

print(s2.endswith('op'))
print(s2.endswith('loo'))'''

'''s3 = '  foo bar lol kek lol prop foo '
print(s3.find('bar'))
print(s3.rfind('lol'))'''
#print(s3.strip()) #удаляет пробелы по бокам
#print(s3.lstrip())
#print(s3.rstrip())
#print(s3.replace('foo', 'boo', 1))

'''s = 'I learn Python language. Python - awesome!'
print(s.find('Python'))'''

'''s = input()
count = 1
for symbol in range(len(s)):
    if s[symbol] == ' ':
        count += 1

print(count)
'''

'''s = input()
s_lower = s.lower()
print(f'Аденин: {s_lower.count('а')}\nГуанин: {s_lower.count('г')}\nЦитозин: {s_lower.count('ц')}\nТимин: {s_lower.count('т')}')'''

'''n = int(input())
count = 0
for _ in range(n):
    s = input()
    if s.count('11') >= 3:
        count += 1

print(count)'''

'''s = input()
count = 0
for i in range(len(s)):
    if s[i] in '0123456789':
        count += 1

print(count)'''

'''s = input()
if s.endswith('.com') or s.endswith('.ru'):
    print('YES')
else:
    print('NO')'''

'''s = input()
often_symbol = ''
counter = 0
for i in range(len(s)):
    if s.count(s[i]) >= counter:
        counter = s.count(s[i])
        often_symbol = s[i]
print(often_symbol)'''

'''a = input()
if 'f' not in a:
    print('NO')
elif a.count('f') == 1:
    print(a.find('f'))
else:
    print(a.find('f'), a.rfind('f'))'''

'''a = input()
afind1, afind2 = a.find('h'), a.rfind('h')
s = a[:afind1] + a[afind2+1:]
print(s)'''

'''s = '123asd'
s1 = '-='
s2 = 'qwe'
print(s.isalnum()) #состоит ли исходная строка из буквенно и/или цифровых символов
print(s1.isalnum())
print(s2.isalnum())'''

'''s = 'asd'
s1 = '123'
print(s.isalpha()) #состоит ли только из буквенных символов
print(s1.isalpha())
'''

'''s = '123'
print(s.isdigit())'''

'''s = 'Abc'
s1 = 'asd'
print(s.islower())
print(s1.islower()) #все ли буквы нижнего регистра'''

'''s = 'ABC'
s1 = 'Ab23'
print(s.isupper())
print(s1.isupper())'''

'''s = ' '
s1 = ' asd'
print(s.isspace())
print(s1.isspace())'''

'''n = int(input())
for i in range(1, n+1):
    s = input()
    if s.isspace() == True or len(s) == 0:
        print(f'{i}: COMMENT SHOULD BE DELETED')
    else:
        print(f'{i}: {s}')'''

'''s = input()
alphabet = 'АВЕКМНОРСТУХ'
if s.isupper() == True and (s.count('_') == 1 and s.find('_') == 6) and 9 <= len(s) <= 10:
    if (s[0] in alphabet and s[4] in alphabet and s[5] in alphabet) and (s[1:4].isdigit()==True and s[7:].isdigit()==True):
        print('YES')
    else:
        print('NO')
else:
    print('NO')'''

'''nickname = input()
if (5 <= len(nickname) <= 15 and nickname[0] == '@' and nickname[1:].isalnum() and (nickname[1:].islower() or nickname[1:].isdigit() == True)):
    print('Correct')
else:
    print('Incorrect')'''

'''s = 'In {0}, someone paid {1} {2} for two pizzas.'
date, price, btc = '2010', '10k', 'Bitcoin'
full_s = s.format(date, price, btc)
print(full_s)'''

'''date, euro, yuan = input(), input(), input()
print(f'На {date}: 1€ = {euro}₽, 1¥ = {yuan}₽')'''

'''a, b = int(input()), int(input())
print(f'Для чисел {a} и {b}:')
print(f'  Сумма кубов: {a}**3 + {b}**3 = {(a**3) + (b**3)}')
print(f'  Куб суммы: ({a} + {b})**3 = {(a + b)**3}')'''

'''a = int(input())
b = float(input())
c = 100 - a * 0.2
if b <= c:
    print("Все идет по плану")
    print(f"#{a} ДЕНЬ: ТЕКУЩИЙ ВЕС = {b} кг, ЦЕЛЬ по ВЕСУ = {c} кг")
else:
    print("Что-то пошло не так")
    print(f"#{a} ДЕНЬ: ТЕКУЩИЙ ВЕС = {b} кг, ЦЕЛЬ по ВЕСУ = {c} кг")'''