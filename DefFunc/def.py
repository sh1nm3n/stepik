'''def say_hello():
    print('hello')
def say_bye():
    print('goodbye')
def nothing():
    pass

say_hello()
say_bye()
nothing()'''

'''def draw_box():
    print('*' * 10)
    for _ in range(12):
        print('*', '*', sep=' ' * 8)
    print('*' * 10)

draw_box()'''

'''def draw_triangle():
    for i in range(1, 11):
        print('*' * i)

draw_triangle()'''

'''def draw_box(height, width):
    for i in range(height):
        print('*' * width)

draw_box(7, 5)'''

'''def print_hello(txt, n):
    print(txt * n)


print_hello('abc', 5)'''

'''def print_number(a, b, c):
    d = (a + c) // b
    print(d)

print_number(2, 3, 11)'''

'''def draw_triangle(fill, base):
    for i in range(1, base // 2 + 2):
        print(fill * i)

    for j in range(base // 2, 0, -1):
        print(fill * j)

draw_triangle('*', 9)'''

'''def print_fio(name, surname, patronymic):
    n, s, p = name[0], surname[0], patronymic[0]
    res = s + n + p
    print(res.upper())

name, surname, patronymic = input(), input(), input()
print_fio(name, surname, patronymic)'''

'''def print_digit_sum(num):
    res = 0
    while num != 0:
        res += num % 10
        num //= 10
    print(res)

n = int(input())

# вызываем функцию
print_digit_sum(n)'''

'''def print_birds():
    global birds #глобальная переменная внутри функции
    birds = 5000
    print(f'{birds} птиц')

def print_texas():
    print(f'{birds} птиц')

print_birds()
print_texas()'''

'''def convert_to_celcius(temp):
    return (5 / 9) * (temp - 32)

fahrenheit = float(input())
res = convert_to_celcius(fahrenheit))
print(res)'''

'''def convert_to_miles(km):
    return km * 0.6214

num = int(input())

# вызываем функцию
print(convert_to_miles(num))'''

'''def get_days(month):
    days = [0,31,28,31,30,31,30,31,31,30,31,30,31]
    return days[month]

num = int(input())
print(get_days(num))'''

'''def get_factors(num):
    factors = []
    for i in range(1, num+1):
        if num % i == 0:
            factors.append(i)
    return factors

n = int(input())

# вызываем функцию
print(get_factors(n))'''

'''def number_of_factors(num):
    count = 0
    for i in range(1, num+1):
        if num % i == 0:
            count += 1
    return count

n = int(input())

# вызываем функцию
print(number_of_factors(n))'''

'''def find_all(target, symbol):
    lst = []
    for i in range(len(target)):
        if target[i] == symbol:
            lst.append(i)
    return lst

s = input()
char = input()

# вызываем функцию
print(find_all(s, char))'''

'''def merge(list1, list2):
    return sorted(list1 + list2)

numbers1 = [int(c) for c in input().split()]
numbers2 = [int(c) for c in input().split()]

# вызываем функцию
print(merge(numbers1, numbers2))'''

'''def is_valid_triangle(side1, side2, side3):
    if side1 < side2 + side3 and side2 < side1 + side3 and side3 < side1 + side2:
        return True
    else:
        return False

res = is_valid_triangle(2, 3, 10)
print(res)'''

'''def is_prime(number):
    if number < 2:  # Числа меньше 2 не являются простыми
        return False
    for i in range(2, int(number ** 0.5) + 1):  # Проверяем делители до корня из числа
        if number % i == 0:  # Если найден делитель
            return False
    return True

def get_next_prime(num):
    next_num = num + 1
    while True:
        if is_prime(next_num):
            return next_num
        next_num += 1


print(get_next_prime(6))  # 7
print(get_next_prime(7))  # 11
print(get_next_prime(14))'''

'''def is_password_good(password):
    count, lower, l_count, upper, r_count, d_count = 0, 'abcdefghijklmnopqrstuvwxyz', 0, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 0, 0
    if (len(password) >= 8):
        count += 1
    for el in range(len(password)):
        if password[el] in lower:
            l_count += 1
            if l_count == 1:
                count += 1
    for el in range(len(password)):
        if password[el] in upper:
            r_count += 1
            if r_count == 1:
                count += 1
    for el in range(len(password)):
        if password[el].isdigit():
            d_count += 1
            if d_count == 1:
                count += 1
    if count == 4:
        return True
    else:
        return False'''

def is_one_away(word1, word2):
    if len(word1) == len(word2):
        count = 0
        for i in range(len(word1)):
            if word1[i] == word2[i]:
                count += 1
        if len(word1) - count == 1:
            return True
    return False

