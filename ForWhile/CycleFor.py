from math import *

'''for num in range(5):
    print(num, '- Hello')'''

'''for i in range(5):
    num = int(input())
    print('квадрат вашего числа =', num * num)

print('END')'''

'''for i in range(5):
    print(i, ' - L')

for i in range(5):
    print(i, ' - O')

print('KEK')'''

'''for i in range(10):
    print('Python is awesome!')'''

'''for _ in range(6):
    print('AAA')

for _ in range(5):
    print('BBBB')

print('E')

for _ in range(9):
    print('TTTTT')

print('G')'''

'''s, n = str(input()), int(input())

for _ in range(n):
    print(s)'''

'''n = int(input())
for _ in range(n):
    print('*' * 19)'''

'''s = str(input())
for i in range(10):
    print(i, s)'''

'''n = int(input())
for i in range(n + 1):
    print('Квадрат числа', i, 'равен', i * i)'''

'''n = int(input())
for i in range(n):
    print((n - i) * '*')'''

'''number = int(input())
summa = 0
for i in range(number+1):
    # summa = summa + i
    summa += i
print(summa)'''

'''for i in range(56, 170, 2):
    print(i)
    '''
'''for i in range(10, 0, -1):
    print(i, end=' ')'''

'''m, n = int(input()), int(input())
for i in range(m, n + 1):
    print(i)'''

'''m, n = int(input()), int(input())
if m < n:
    for i in range(m, n + 1):
        print(i)

elif m > n:
    for i in range(m, n - 1, -1):
        print(i)

elif m == n:
    print(m)'''

'''m, n = int(input()), int(input())
if m % 2 == 0:
    for i in range(m-1, n-1, -2):
        print(i)

elif m % 2 != 0:
    for i in range(m, n-1, -2):
        print(i)'''

'''m, n = int(input()), int(input())
for i in range(m, n+1):
    if (i % 17 == 0) or (i % 10 == 9) or (i % 15 == 0):
        print(i)'''

'''n = int(input())
for i in range(1, 10+1):
    print(f'{n} x {i} = {n*i}')'''

'''count = 0
count2 = 0
for _ in range(10):
    n = int(input())
    if n > 10:
        count += 1
    if n == 0:
        count2 += 1

print(f'было введено {count} чисел больших 10')
print(f'было введено {count2} нулей')'''

'''total = 0
for _ in range(10):
    n = int(input())
    if n > 10:
        total += n

print(f'сумма всех чисел что больше 10: {total}')'''

'''largest = int(input())
for _ in range(5):
    n = int(input())
    if n < largest:
        largest = n

print(f'наименьшее число {largest}')'''

'''total = 0
for i in range(1, 6):
    total += i
print(total)'''

'''a, b, count = int(input()), int(input()), 0
for i in range(a, b + 1):
    if (i ** 3) % 10 == 4 or (i ** 3) % 10 == 9:
        count += 1

print(count)'''

'''summa = 0
n1 = int(input())
for i in range(n1):
    n2 = int(input())
    summa += n2

print(summa)'''

'''total = 0
n = int(input())
for i in range(1, n + 1):
    x = 1 / i
    total += x

print(total - log(n))'''

'''summa = 0
n = int(input())
for i in range(1, n+1):
    if (i ** 2) % 10 == 2 or (i ** 2) % 10 == 5 or (i ** 2) % 10 == 8:
        summa += i

print(summa)'''

'''num = 1
n = int(input())
for i in range(1, n+1):
    num *= i

print(num)'''

'''summa = 1
for i in range(10):
    n = int(input())
    if n != 0:
        summa *= n

print(summa)'''

'''summa = 0
n = int(input())
for i in range(1, n+1):
    if n % i == 0:
        summa += i

print(summa)'''

'''total = 0
n = int(input())
for i in range(1, n+1):
    num = (-1)**(i+1)* i
    total += num

print(total)'''


'''max1 = 0
max2 = 1
n = int(input())
for i in range(1, n+1):
    num = int(input())
    if num > max1:
        max2 = max1
        max1 = num

    elif num > max2:
        max2 = num

print(max1)
print(max2)'''

'''count = 0
for i in range(10):
    num = int(input())
    if num % 2 == 0:
        count += 1

if count == 10:
    print('YES')
else:
    print('NO')'''

'''n = int(input())  # Читаем количество чисел

a, b = 1, 1  # Первые два числа Фибоначчи

for i in range(n):
    if i == 0 or i == 1:  # Для первых двух чисел
        print(1, end=' ')
    else:
        c = a + b         # Следующее число
        print(c, end=' ')
        a, b = b, c       # Обновляем значения'''

print('hello world')

