'''s1 = 'qwe_rty'
leng1 = len(s1) #7
leng2 = len('xzssdscvnbm') #11
print(leng1)
print(leng2)'''

#преобразование в строку
'''num1 = 144
num2 = 1.234
print(type(str(num1)), num1)
print(type(str(num2)), num2)'''

'''s1 = 'pyt'
s2 = 'hon'
s12 = s1 + s2
s21 = s2 + s1
full_str = s12 + '!!!'
print(s1)
print(s2)
print(s21)
print(type(full_str), full_str)'''

print('a' + '*' + 'b' + '*' + 'c' + '!')
print('Py' * 4)
print(' ', '*')
print('', '*' * 3)
print('*' * 5)


'''mystr = '123' * 3 + '456' * 2 + '789' * 1
print(mystr)'''

'''name = input()
last_name = input()
print('Hello' + ' ' + name + ' ' + last_name + '!' ' You have just delved into Python')'''

'''FC = input()
leng = str(len(FC))
print('Футбольная команда ' + FC + ' имеет длину ' + leng + ' символов')'''

'''city1, city2, city3 = input(), input(), input()
shortest = city1
if len(city2) < len(shortest):
    shortest = city2
if len(city3) < len(shortest):
    shortest = city3
longest = city1
if len(city2) > len(longest):
    longest = city2
if len(city3) > len(longest):
    longest = city3
print(shortest)
print(longest)'''

'''a, b, c = len(input()), len(input()), len(input())
if (2*b-c-a)*(2*c-b-a)*(2*a-b-c) == 0:
    print('YES')
else:
    print('NO')'''

'''s = 'stepikZaebal'
if 'z' not in s:
    print('yes')
else:
    print('no')'''

'''s = 'Sigma'
print('a' in s)
print('z' in s)'''

'''print('ab' in 'abc')
print('ac' in 'abc')'''

'''s = input()
if 'синий' in s:
    print('YES')
else:
    print('NO')'''

'''s = input()
if 'суббота' in s or 'воскресенье' in s:
    print('YES')
else:
    print('NO')'''

email = input()
if '@' in email and '.' in email:
    print('YES')
else:
    print('NO')