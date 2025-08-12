#список - изменяемые элементы различных типов данных []

'''new_list = [1, 'orange', 3.14]
print(new_list)

empty_list = []'''

'''numbers = [1, 2, 3, 4, 5]        # список чисел
words = ['Python', 'Java']       # список строк
mixed = ['abc', 123, 4.5]        # список разных типов
empty_list1 = []                 # пустой список
empty_list2 = list()'''             # пустой список

'''fruits = ['apple', 'orange', 'banana']
count = 0
for fruit in fruits:
    count += 1
    print(f'{count} элемент списка: {fruit}')'''

'''numbers = [3, 12, 42]
count = 0
for num in numbers:
    count += 1
    print(f'{count} элемент списка: {num}')'''

'''nums = range(10)
numbers_list = list(nums)
even = []
odd = []

for num in numbers_list:
    if num % 2 != 0:
        odd.append(num)
    else:
        even.append(num)

print(numbers_list)
print(f'Список нечетных чисел: {odd}')
print(f'Список четных чисел: {even}')'''

#food_list = ['apple', 'tomato', 'banana', 'cucumber', 'meat']

'''fruits, vegetables = [], []

for food in food_list:
    if food == 'apple' or food == 'banana':
        fruits.append(food)
    if food == 'tomato' or food == 'cucumber':
        vegetables.append(food)
        
print(fruits)
print(vegetables)'''

'''food_list.insert(1, 'strawberry') #вставил элемент в индекс
print(food_list)

food_list.remove('cucumber')
print(food_list)

food_list.sort()
print(food_list)

nums = [231, 31, -22.2, 120]
nums.sort()
print(nums)'''

'''squares = [x**2 for x in range(10) if x % 2 == 0]
print(squares)'''

'''list_nums = [0 , 2, 4, 6, 8]
print(list_nums)

nums = list(range(1, 10, 2))
print(nums)

nums = 1, 2, 3, 4, 5
list_n = list(nums)
print(list_n)

names = ['James']
print(names)

empty = ['']
print(list(range(1)))'''

'''n = int(input())
list1 = list('abcdefghijklmnopqrstuvwxyz')
for i in range(1, n+1):
    res = list1[:i]
print(res)'''

'''numbers = [1, 2, 3, 4, 5]
print(numbers[2:][::-1])'''

'''fruits = ['apple', 'cherry', 'banana', 'melon', 'orange']
fruits[2:4] = ['банан', 'арбуз'] #изменили элементы по индексу
print(fruits)'''

'''print([1, 2, 3] + [3, 4, 5])
print([1, 0, 1] * 3)'''

'''nums = [1, 2, 3, 4, 5, 6, 7, 8]
print(sum(nums)) #сумма всех элементов'''

'''books = ['1984', 'clockwork orange', 'norwegian wood']
print(books[0][3])
print(books[1][10:])
print(books[2][::-1])
print(books[2:]) #возвращает список'''

'''browsers = ['Firefox', 'Chrome', 'Safari', 'Yandex']
print(browsers[-1:])

evens = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
average = sum(evens) / len(evens)

print(average)  '''

'''numbers1 = [1, 2, 3]
numbers2 = [6]
numbers3 = [7, 8, 9, 10, 11, 12, 13]

print((numbers1 * 2) + (numbers2 * 9) + numbers3)'''

'''numbers = [1, 2, 3, 4, 5]
numbers.append(6)
numbers.append(7) #добавление элемента в конец списка
print(numbers)

count = 1
for el in numbers:
    print(f'{count}-й элемент: {el}')
    count += 1'''

'''numbers = [2, 4, 6, 8]
odd = [1, 3, 5 ,7]
numbers.extend(odd)
odd.extend('python') #extend разбивает строку на элементы в отличие от append
print(numbers)
print(odd)'''

'''for el in numbers:
    if el % 2 == 0:
        print(f'{el} - четное число')
    else:
        print(f'{el} - нечетное число')'''

'''numbers = [1, 2, 3, 4, 5 ,6, 7, 8, 9, 10]
del numbers[3] #удалил четверку по индексу
del numbers[2:7]
del numbers[::2]
print(numbers)'''

'''nums = [2, 4, 5, 8]
for num in range(len(nums)):
    nums[num] *= 2

print(nums)'''

'''numbers = [2, 6, 3, 14, 10, 4, 11, 16, 12, 5, 4, 16, 1, 0, 8, 16, 10, 10, 8, 5, 1, 11, 10, 10, 12, 0, 0, 6, 14, 8, 2, 12, 14, 5, 6, 12, 1, 2, 10, 14, 9, 1, 15, 1, 2, 14, 16, 6, 7, 5]
print(len(numbers))
print(numbers[-1])
print(numbers[::-1])
if 5 in numbers and 17 in numbers:
    print('YES')
else:
    print('NO')
del numbers[0]
del numbers[-1]
print(numbers)'''

'''n = int(input())
n_list = []
for i in range(n):
    n_list.append(input())

print(n_list)'''

'''abc = 'abcdefghijklmnopqrstuvwxyz'
alphabet = []
for letter in range(26):
    n = alphabet.append(abc[letter] * letter + abc[letter])

print(alphabet)'''

'''n = int(input())
nums_list = []

for i in range(n):
    n = int(input())
    nums_list.append(n ** 3)

print(nums_list)'''

'''n = int(input())
divisors_list = []

for i in range(1, n+1):
    if n % i == 0:
        divisors_list.append(i)
print(divisors_list)'''

'''n, temp = int(input()), int(input())
l = []
for i in range(n-1):
    a = int(input())
    l.append(temp + a)
    temp = a
print(l)'''

'''n_list = ['hello', ['a', 's', 'd']]
print(n_list[0][2])
print(n_list[1][1])

nums = [4, 1, 1, 3, 3, 2, 2, 5, 6 ,7]

sort_nums = sorted(set(nums)) #отсортированный и без дубликатов
print(sort_nums)

sort_nums.insert(1, 23) #добавляет элемент в индекс
print(sorted(sort_nums))

sort_nums.remove(23) #удаляем определенный элемент
print(sort_nums)

print(sort_nums.index(4)) #индекс элемента
print(nums.count(3)) #количество вхождений

sort_nums.reverse()
print(sort_nums) #тоже самое что и [::-1]'''

'''people = ['Alice', 'Ivan', 'Artem', 'Anna', 'Lelouch']
if 'Artem' not in people:
    people.append('Artem')
elif 'Artem' in people:
    people.remove('Artem')

print(people)

del people[0]
del people[1:2]
print(people)'''


'''n = int(input())
odd_list = []
for i in range(n):
    n = int(input())
    odd_list.append(n)

print(odd_list[::2])'''

'''n = int(input())
lst = []
s = ''
for i in range(n):
    n = input()
    lst.append(n)

k = int(input())
for i in range(len(lst)):
    m = lst[i]
    if k <= len(m):
        x = m[k-1]
        s += x

print(s)'''

'''n = int(input())
lst = []
for i in range(n):
    n = input()
    lst.extend(n)

print(lst)'''

'''nums = [1, 2, 3, 4, 5, 6]
print(*nums) #выводит элементы в строку

numbers = [1, 3, 0, 2, 4]

for i in numbers:
    print(numbers[i], end=' ')'''

'''numbers = [1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111]
res = 0

for num in numbers:
    res += num ** 2

print(res)'''

'''n = int(input())
nums = []
res = []
for i in range(n):
    n = int(input())
    nums.append(n)
    res.append(n ** 2 + 2 * n + 1)

print(*nums, sep='\n')
print()
print(*res, sep='\n')'''

'''n = int(input())
nums = []
for i in range(n):
    n = int(input())
    nums.append(n)

nums.remove(max(nums))
nums.remove(min(nums))
print(*nums, sep='\n')'''

'''n = int(input())
s_list = []

for i in range(n):
    n = input()
    if n not in s_list:
        s_list.append(n)

print(*s_list, sep='\n')'''

'''n = int(input())
neg_nums = []
zero_nums = []
pos_nums = []
res = []
for i in range(n):
    n = int(input())
    if n < 0:
        neg_nums.append(n)
    if n == 0:
        zero_nums.append(n)
    if n > 0:
        pos_nums.append(n)

res.extend(neg_nums)
res.extend(zero_nums)
res.extend(pos_nums)
print(*res, sep='\n')'''

'''s = 'Python is the most lamest language'
print(s.split()) #возвращает список из слов строки'''

'''nums = input().split()
print(nums)'''

'''ip = '192.0.28.234'
print(ip.split('.')) #разделитель ввиде точки'''

'''s = 'Python is the most lamest language'
res = s.split()
print(' '.join(res)) #совмещаем каждый элемент списка с помощью пробела и .join
print('-'.join(res))
print('*'.join(res))'''

'''s = 'a    b c'
print(s.split())'''

'''s = input().split()
print(*s, sep='\n')'''

'''s = input().split()
F,I,O = s[0][0], s[1][0], s[2][0]
fio = []
fio.extend(F)
fio.extend(I)
fio.extend(O)
print('.'.join(fio), end='.')'''

'''s = input()
print(*s.split('\\'), sep='\n')'''

'''numbers = input().split()
for i in range(len(numbers)):
    print('+' * int(numbers[i]))'''
