#множества - элементы не индексируются и не повторяются {}

'''empty_set = set
print(empty_set)

duplicates = {1, 1, 2, 2, 3, 3, 3, 4, 5, 5}
print(duplicates)

numbers_set = set([1, 2, 2, 3, 4, 5])
print(numbers_set)

s = set('hello')
print(s)'''

'''squares = {x**2 for x in range(10) if x % 2 != 0}
print(squares)'''

fruits = {'apple', 'orange', 'banana'}
'''print('apple' in fruits)

fruits.add('strawberry')
print(fruits)

fruits.update(['blueberry', 'melon']) #в квадратных скобках чтобы не разделило на символы
print(fruits)

fruits.remove('apple')
print(fruits)

random_fruit = fruits.pop()
print(random_fruit)
print(fruits)'''

'''fruits.clear()
print(fruits)'''

'''a, b = {1, 2, 3}, {'a', 'b', 'c'}
print(a | b)
print(b.union(a))
'''

'''numbers = [1, 2, 2, 2, 3, 4, 5]
list_set = list(set(numbers)) #удаляем дубликаты и возвращаем список

print(list_set)'''

users_1 = ['Ivan', 'Elena', 'Anna', 'Eva']
users_2 = ['Natalia', 'Artyom', 'Danil', 'Ivan']

unique_group1 = set(users_1) & set(users_2)
print(f'Пользователи обеих групп: {unique_group1}') #общие элементы

