#ord - позволяет определить код некоторого символа в таблице символов Unicode
'''print(ord('A'))
print(ord('3'))
print(ord('&'))

print(chr(14)) #обратная функция
print(chr(88))

for i in range(10): #вывод алфавита от А
    print(chr(ord('A') + i))'''

'''print(ord('a'))
print(ord('A'))
print(ord('z'))
print(ord('Z'))
print(ord('7'))
print(ord('6'))'''

'''letter = input()
if letter == 'Я':
    print('Дальше букв нет')
else:
    print(chr(ord(letter) + 1))'''

'''a, b = int(input()), int(input())
for i in range(a, b + 1):
    print(chr(i), end=' ')'''

'''s = input()
for i in s:
    print(ord(i), end=' ')'''

'''a, b, c, d = input(), input(), input(), input()
sum_a, sum_b, sum_c, sum_d = 0, 0, 0, 0

for i in a:
    sum_a += ord(i)
for i in b:
    sum_b += ord(i)
for i in c:
    sum_c += ord(i)
for i in d:
    sum_d += ord(i)

if sum_a >= sum_b and sum_a >= sum_c and sum_a >= sum_d:
    print(a)
elif sum_b >= sum_c and sum_b >= sum_d:
    print(b)
elif sum_c >= sum_d:
    print(c)
else:
    print(d)'''

'''message = input()
sum = 0
for el in message:
    sum += ord(el) * 3

print(f"Текст сообщения: '{message}'")
print(f'Стоимость сообщения: {sum}🐝')'''

# шифр цезаря
'''n = int(input())  # Считываем сдвиг
encoded = input().strip()  # Считываем закодированную строку
decoded = []

for char in encoded:
    if char.islower():  # Работаем только со строчными латинскими буквами
        # Декодируем символ: (ord(char) - ord('a') - n) % 26 + ord('a')
        decoded_char = chr((ord(char) - ord('a') - n) % 26 + ord('a'))
        decoded.append(decoded_char)
    else:
        decoded.append(char)  # Оставляем другие символы без изменений

print(''.join(decoded))'''
'''
print('a' > 'b')
print('z' > 'a')
print(max('low', 'qwe', 'zxc'))
print(min('low', 'qwe', 'zxc'))'''

'''a, b, c, d = input(), input(), input(), input()
mx_s, mn_s = max(a, b, c, d), min(a, b, c, d)
magic_word = (ord(mn_s[-1]) * ord(mx_s[-1])) ** 2
print(magic_word)'''

'''n = int(input())
alphabet = 'АБВГДЕЖЗИЙКЛМНОП'
nums = '0123456789'
for i in range(n):
    n = input()
    if len(n) == 2 and n[0] in nums and n[1] in alphabet:
        print('YES')
    else:
        print('NO')'''

'''s1, s2 = input(), input()
n1, n2 = '', ''
for i in range(len(s1)):
    if s1[i].isalpha():
        n1 += s1[i]

for i in range(len(s2)):
    if s2[i].isalpha():
        n2 += s2[i]

new_n1, new_n2 = n1.lower(), n2.lower()
if new_n1 == new_n2:
    print('YES')
else:
    print('NO')'''

'''s1, s2, s3 = input(), input(), input()
mid = min(max(s1, s2), max(s1, s3), max(s2, s3))
mx, mn = max(s1, mid, s2, s3), min(s1, mid, s2, s3)
print(f'{mn} {mid} {mx}')'''

'''s = input()
full = ''
for el in range(len(s)):
    if el % 3 != 0:
        full += s[el]
print(full)'''

'''s = input()
if s.count('f') == 1:
    print('-1')
elif s.count('f') > 1:
    print(s.find('f', s.find('f')+1))
else:
    print('-2')'''

s = input()
h1, h2 = s.find('h'), s.rfind('h')
print(s[:h1] + s[h2:h1:-1] + s[h2:])