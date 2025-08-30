from random import *

'''num1 = randint(0, 20)
num2 = randint(-20, 0)

print(f'{num1} + {num2} = {num1 + num2}')'''

'''total = 1
for i in range(5):
    total *= randint(1, 10)
    print(total)'''

'''random_num = randint(0, 5)
user_num = int(input('Угадайка. Введите число от 0 до 5: '))

if user_num == random_num:
    print('Победа. Вы угадали!')
else:
    print('Проигрыш. Вы не угадали.')'''

'''num = randrange(0, 100, 10) #randrange - то же что и range
print(num)'''

'''num = random() #возвращает вещественное число от 0.0 до 1.0 не включительно
print(num)'''

'''num = uniform(0.4, 2) #то же что и рандом но с диапазоном
print(num)'''

'''seed(13) #seed это один и тот же набор случайных чисел
for _ in range(5):
    print(randint(0, 20))'''

'''again = 'д'
while again == 'д':
    print('Бросаю кубик...')
    print(randint(1, 6))
    again = input('Бросить кубик еще раз? - (д - да / н - нет): ')'''

'''nums = [1, 2, 3, 4, 5, 6, 7]
shuffle(nums) #перемешивает список
print(nums)'''

'''nums = [i for i in range(0, 10)]
shuffle(nums)
print(nums)'''

#выводит одно рандомное значение
'''print(choice('SNUSIK'))
print(choice([1, 2, 3]))
print(choice(['a', 'b', 'c']))'''

#выводит указанное колво случайных значений
'''print(sample('SNUSIK', 2))
print(sample([1, 2, 3, 4, 5], 3))
print(sample(['a', 'b', 'c'], 1))'''

random_num = randint(1, 10)
user_num = int(input('Угадайка. Введите число от 1 до 10: '))

while random_num != user_num:
    if user_num > random_num:
        print('Твое число больше рандомного.')
        user_num = int(input('Пробуй дальше!'))
    elif user_num < random_num:
        print('Твое число меньше рандомного.')
    elif user_num == random_num:
        print('Молодец! Ты угадал.')