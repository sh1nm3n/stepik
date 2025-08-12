from math import *

'''i = int(input())
while i <= 10:
    print('HELLO')
    i += 1

print('END')'''

'''num = int(input())
while num != -1:
    print(num * num)
    num = int(input())'''

'''i = 0
while i < 101:
    print(i)
    i += 3'''

'''stop = input()
num = 0
while stop != 'stop':
    num += int(stop)
    stop = input()

print(num)'''

'''i = 7
a = 5
while i < 11:
    a += i
    i += 2

print(a)'''

'''count = 0
word = input()
while word != 'стоп' and word != 'хватит' and word != 'достаточно':
    word = input()
    count += 1

print(count)'''


'''num = int(input())
while num % 7 == 0:
    print(num)
    num = int(input())'''

'''summa = 0
num = int(input())
while num >= 0:
    summa += num
    num = int(input())

print(summa)'''

'''count = 0
num = int(input())
while num > 0 and num <= 5:
    if num == 5:
        count += 1
    num = int(input())

print(count)'''

'''count = 0
num = int(input())
while num != 0:
    if num >= 25:
        num -= 25
        count += 1
    elif num >= 10:
        num -= 10
        count += 1
    elif num >= 5:
        num -= 5
        count += 1
    else:
        num -= 1
        count += 1

print(count)'''

'''summa = 0
nums_of_digits = 0
multi_of_digits = 1
arithm_mid = 0
first_digit = 0
summa2 = 0
n = int(input())
last_digit = n % 10
while n > 0:
    digit = n % 10
    summa += digit
    nums_of_digits += 1
    multi_of_digits *= digit
    arithm_mid = summa / nums_of_digits
    n //= 10
    if n == 0:
        first_digit = digit

summa2 = first_digit + last_digit

print(summa)
print(nums_of_digits)
print(multi_of_digits)
print(arithm_mid)
print(first_digit)
print(summa2)'''

'''n = int(input())
second_digit = n % 10
while n > 9:
    last_digit = n % 10
    n //= 10
    second_digit = last_digit

print(second_digit)'''

'''n = int(input()) #121
count = 0
digit = n % 10 #1

while n != 0:
    last_digit = n % 10 #1
    n //= 10 #12
    if last_digit > digit:
        count += 1

if count > 0:
    print('NO')
else:
    print('YES')'''

'''result = 0
for i in range(10):
    n = int(input())
    if n < 0:
        break
    result += n
print(result)'''

'''n = int(input())
flag = False
while n != 0:
    last_digit = n % 10
    if last_digit == 6:
        flag = True
        break
    n //= 10
print('YES' if flag else 'NO')'''

'''for i in range(1, 101):
    if i == 8 or i == 88 or i == 14:
        continue
    print(i, end='|')'''

'''n = 10
while n > 0:
    n -= 1
    if n == 2:
        continue
    print(n, end='*')'''

'''mult = 1
for i in range(1, 11):
    if i % 2 == 0:
        continue
    if i % 9 == 0:
        break
    mult *= i

print(mult)'''

'''n = int(input())
for i in range(2, n+1):
    if n % i == 0:
        print(i)
        break'''

'''n = int(input())
for i in range(1, n+1):
    if 5 <= i <= 9 or 17 <= i <= 37 or 78 <= i <= 87:
        continue
    print(i)'''

'''count = 0
p = 1  # Ошибка 1: произведение должно начинаться с 1, а не с 0
for i in range(10):  # Ошибка 2: нужно обработать 10 чисел (range(10)), а не 9 (range(1,10))
    x = int(input())
    if x >= 0:  # Ошибка 3: нужно считать неотрицательные числа (>= 0), а не только положительные (> 0)
        p = p * x
        count = count + 1
if count > 0:
    print(count)  # Ошибка 4: нужно вывести количество (count), а не последнее число (x)
    print(p)
else:
    print('NO')'''


'''mx = -10 ** 6
s = 0
for i in range(1, 11):
    x = int(input())
    if x < 0:
        s += x
        if x > mx:
            mx = x
if s >= 0:
    print('NO')
else:
    print(s)
    print(mx)'''

'''s = 0
for i in range(1, 8):
    n = int(input())
    if n % 2 == 0:
        s += n
if s % 2 != 0:
    print('NO')
else:
    print(s)'''

'''n = int(input())
max_digit = -1
while n != 0:
    digit = n % 10
    if digit % 3 == 0:
        if digit >= max_digit:
            max_digit = digit
    n //= 10
if max_digit == -1:
    print('NO')
else:
    print(max_digit)'''

'''n = int(input())
while n != 0:
    first_digit = n % 10
    n //= 10
    digit = first_digit
    
print(digit)'''

'''n = int(input())
product = 1
while n != 0:
    digit = n % 10
    product = product * digit
    n //= 10

print(product)'''

#for hours in range(12):
'''for minutes in range(60):
    for seconds in range(60):
        print(minutes, ':', seconds)'''

'''for i in range(3):
    for j in range(3):
        if i == j:
            break
        print(i, j)'''

'''for i in range(8):
    for j in range(6):
        print('*', end='')
    print()'''

'''counter = 0
for i in range(99, 102):
    temp = i
    while temp > 0:
        counter += 1
        temp //= 10

print(counter)'''

'''n = int(input())
for i in range(n):
    for j in range(3):
        print(n, end=' ')
    print()'''

'''n = int(input())
for i in range(1, n+1):
    for j in range(5):
        print(i, end=' ')
    print()'''

'''n = int(input())
for i in range(1, n+1):
    for j in range(1, 10):
        print(f'{i} + {j} = {i + j}', end='\n')
    print()'''

'''n = int(input())
for i in range(1, n+1):
    for j in range(1, 10):
        print(f'{i} + {j} = {i + j}', end='\n')
    print()'''

'''n = int(input())
for i in range(1, n // 2 + 2):
    print('*' * i)

for j in range(n // 2, 0, -1):
    print('*' * j)

print()'''

'''n = int(input())
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(i, end='')
    print()'''

'''n = int(input())
for i in range(1, n + 1):
    for j in range(i):
        print(j + 1, end='')
    for k in range(i - 1, 0, -1):
        print(k, end='')
    print()'''

'''a, b = int(input()), int(input())
max_sum = 0
best_num = a  # Начинаем с первого числа отрезка

for num in range(a, b + 1):
    current_sum = 0
    for divisor in range(1, num + 1):
        if num % divisor == 0:
            current_sum += divisor

    # Обновляем максимальную сумму и число
    if current_sum > max_sum or (current_sum == max_sum and num > best_num):
        max_sum = current_sum
        best_num = num

print(best_num, max_sum)'''

'''n = int(input())
while n > 9:
    summa1 = 0
    while n > 0:
        last_digit = n % 10
        summa1 += last_digit
        n //= 10
    n = summa1
print(n)'''

'''n = int(input())
summa = 0
for i in range(1, n+1):
    summa += factorial(i)

print(summa)'''

'''a, b = int(input()), int(input())
for i in range(a, b+1):
    counter = 0
    for j in range(1, i+1):
        if i % j == 0:
            counter += 1
    if counter == 2:
        print(i)'''

'''n = int(input())
s = 0
while n > 0:
    if n % 2 == 0:
        s += n % 10
    n //= 10
print(s)'''

'''n = 4
count = 0
maximum = -10 ** 8
for i in range(1, n + 1):
    x = int(input())
    if x % 2 != 0:
        count += 1
    if x > maximum:
        maximum = x
if count > 0:
    print(count)
    print(maximum)
else:
    print('NO')'''

'''n = int(input())
print('*' * 19)
for i in range(n-2):
    print('*', '*', sep=' ' * 17)
print('*' * 19)'''

'''n = int(input())
digit = 0
while n > 99:
    last_digit = n % 10
    digit = last_digit
    n //= 10

print(digit)'''

n = int(input())
troyki = 0
kolvo_last_digit = 0
kolvo_chetnih_num = 0
summa_5 = 0
multi_bolshe_7 = 1
count_0_5 = 0
last_digit1 = n % 10

while n != 0:
    last_digit2 = n % 10
    if last_digit2 == 3:
        troyki += 1
    if last_digit1 == last_digit2:
        kolvo_last_digit += 1
    if last_digit2 % 2 == 0:
        kolvo_chetnih_num += 1
    if last_digit2 > 5:
        summa_5 += last_digit2
    if last_digit2 > 7:
        multi_bolshe_7 *= last_digit2
    if last_digit2 == 0 or last_digit2 == 5:
        count_0_5 += 1
    n //= 10

print(troyki)
print(kolvo_last_digit)
print(kolvo_chetnih_num)
print(summa_5)
print(multi_bolshe_7)
print(count_0_5)