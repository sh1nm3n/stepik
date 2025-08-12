#словарь - каждый элемент имеет уникальный ключ
#dictionary = { ключ1:значение1, ключ2:значение2, ....}

'''user_dict = {'admin': 'Ivan', 'user': 'Artem'}
print(user_dict)

empty_dict = {}
objects = dict()'''

'''users_list = [
    ['ivan@gm.com', 'Ivan'],
    ['anna@gm.com', 'Anna'],
    ['artem@gm.com', 'Artem']
]

users_dict = dict(users_list) #преобразовал список в словарь
for key in users_dict:
    print(key, end=' ')'''

'''print(users_dict)
print(users_list)'''

'''shop_tuple = (
    ('1', 'apple'),
    ('2', 'orange'),
    ('3', 'melon')
)

shop_dict = dict(shop_tuple)
for key in shop_dict:
    print(key)
print(shop_dict)'''

users_list = [
    ['ivan@gm.com', 'Ivan'],
    ['anna@gm.com', 'Anna'],
    ['artem@gm.com', 'Artem']
]

users_dict = dict(users_list) #преобразовал список в словарь
'''for key in users_dict:
    print(key, end=' ')'''
#key = 'leila@gm.com'

#print(users_dict['ivan@gm.com']) #выводит значение по ключу
users_dict['leila@gm.com'] = 'Leila' #добавил элемент
'''print(users_dict['leila@gm.com'])

if key in users_dict:
    print(users_dict[key]) #если ключ в словаре то выведи его значение
else:
    print('Не найден')'''

#print(users_dict.get('ivan@gm.com')) #выводит значение по ключу
#del users_dict['artem@gm.com'] #удаление
#print(users_dict)

'''key = 'artem@gm.com'
if key in users_dict:
    del users_dict[key]
    print(users_dict)
else:
    print('ключ не найден')'''

#print(users_dict.pop('ivan@gm.com')) #удаляет элемент по ключу и возвращает его значение
#print(users_dict)
#users_dict.clear() #очистка всех элементов
#print(users_dict)

country_dict = {
    'Britannia': 'Lelouch vi Britannia',
    'Japan': 'Suzaku Kururugi'
}
city_dict = {
    'Tokyo': 'Nannali',
    'Kyoto': 'Shirley'
}
students = country_dict.copy()
#print(students)

students.update(city_dict) #объединяем два словаря
#print(students)

'''for key in students:
    print(f'Место рождения: {key} | Имя: {students[key]}')'''

'''for key, value in students.items():
    print(f'Место рождения: {key} | Имя: {value}')''' #результат один и тот же но методом .items()

'''for keys in students.keys():
    print(f'Место рождения: {keys}')''' #вывод только ключей методом .keys()

'''for values in students.values():
    print(f'Имя: {values}')''' #вывод только значений методом .values()

'''users_info = {
    'Ivan' : {
        'phone_number': '+7918546',
        'email': 'dan@1gm.com'
    },
    'Lelouch' : {
        'phone_number': '+3333333',
        'email': 'lulu@gm.com'
    }
}
print(users_info)
print(users_info['Ivan']['phone_number']) #вывел номер телефона используя два индекса

print(users_info['Lelouch']['email'])

users_info['Lelouch']['email'] = 'luluvibrit@gm.com'
print(users_info['Lelouch']['email'])'''

'''user1 = {'Name' : 'Tom', 'Age' : '39','Company' : 'SuperCorp', 'Prog_Languages' : ['Python', 'JavaScript']}
print(f'Имя : {user1['Name']}')
print(f'Возраст: {user1['Age']}')
print(f'Компания: {user1['Company']}')
print(f'Языки программирования: {user1['Prog_Languages']}')'''

'''people = [
    {"name": "Tom", "age": 39, "company": "SuperCorp", "languages": ["Python", "JavaScript"]},
    {"name": "Bob", "age": 43, "company": "BigCorp", "languages": ["Python", "C++", "C#"]},
    {"name": "Sam", "age": 28, "company": "LittleCorp", "languages": ["Python", "Java"]}
]

for person in people:
    print(f'Name: {person['name']}')
    print(f'Last language: {person['languages'][-1]}')'''


