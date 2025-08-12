#кортежи - неизменяемые последовательности элементов, данные нельзя изменять как в списках ()

'''empty_tuple = ()
print(type(empty_tuple))

numbers_tuple = (1, 2, 3, 4, 5)
print(numbers_tuple)

fruits_tuple = ('banana', 'apple', 'orange')
print(fruits_tuple)

days_of_week = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

workdays = days_of_week[:5]
weekends = days_of_week[5:]

print(workdays)
print(weekends)'''

'''single_item = (42,) #обязательно с запятой, без запятой это не будет кортеж
print(single_item)

coordinates = 12.0, 2.0 #можно без скобок
print(type(coordinates))'''

#mixed = (True, 'a', 3, 23.9)

'''nested = ((2, 32), ('a', 'bc'), (True, False))
tpl = []
for tpls in nested:
    tpl.append(tpls)
for el in tpl:
    print(el)

print(tpl)'''

'''coord = 23.0, 1.3, 10.2

x, y, z = coord
print(x, y, z)'''

'''empty_tuple = tuple()

list_to_tuple = tuple([1, 2, 3]) #преобразование
print(list_to_tuple)

str_to_tuple = tuple('Python')
print(str_to_tuple) #каждый символ становится элементом кортежа

set_to_tuple = tuple({1, 2, 3})
print(set_to_tuple)'''

'''nums = (1, 2, 3, 4, 5, 6, 7)
print(nums,'=', len(nums))
print(nums[:2])
print(nums[2:])
print(nums[::-2])

print(nums.index(3))
print(nums.count(4))

print(9 in nums)'''

squares = tuple(x**2 for x in range(10) if x > 3)
print(squares)