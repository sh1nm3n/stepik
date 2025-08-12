'''s = 'Python'
print(s[0], s[1], s[2], s[3], s[4], s[5])
print(s[-1], s[-2], s[-3], s[-4], s[-5], s[-6])

s2 = 'Love'
for i in range(len(s2)):
    print(s2[i])'''

'''s = '01234567891011121314151617'
for i in range(0, len(s), 5):
    print(s[i], end='')'''

'''n = input()
for i in range(0, len(n), 2):
    print(n[i])'''

'''n = input()
for i in range(1, len(n)+1):
    print(n[-i])'''

'''a, b, c = input(), input(), input()
print(b[0], a[0], c[0], sep='')'''

'''n = input()
summa = 0
for i in range(0, len(n)):
    summa += int(n[i])

print(summa)'''

'''n = input()
count = 0
for i in range(10):
    if str(i) in n:
        count += 1

if count == 0:
    print('Цифр нет')
else:
    print('Цифра')'''

'''s = input()
m, n = 0, 0

for i in range(len(s)):
    if s[i] == '+':
        n += 1
    if s[i] == '*':
        m += 1

print(f'Символ + встречается {n} раз')
print(f'Символ * встречается {m} раз')'''

'''s = input()
count = 0

for i in range(len(s)-1):
    if s[i] == s[i+1]:
        count += 1

print(count)'''

'''s = input()
glasnie = 'ауоыиэяюеАУОЫИЭЯЮЕ'
soglasnie = 'бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ'
count_gl, count_sogl = 0, 0

for i in range(len(s)):
    if s[i] in glasnie:
        count_gl += 1
    if s[i] in soglasnie:
        count_sogl += 1

print(f'Количество гласных букв равно {count_gl}')
print(f'Количество согласных букв равно {count_sogl}')'''

'''n = int(input())
b = ''
while n > 0:
    b = str(n%2) + b
    n //= 2

print(b)'''