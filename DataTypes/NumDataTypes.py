'''n = int('12345')
print(type(n), n)

atom = 10 ** 80
print(atom)'''

'''num1 = 10_000_000
num2 = 10000000
print(f'{num1}, {num2}')'''

'''pi = 3.14
print(f'{type(pi)}, {pi}')'''

'''a = float(input())
print(a)'''

'''n = float('12345')
print(n)'''

'''num1 = 18.99
num2 = 1.99
print(int(num1))
print(int(num2))'''

'''a, b = float(input()), float(input())
S = 1 / 2 * a * b
print(S)'''

'''S, V1, V2 = float(input()), float(input()), float(input())
V = V1 + V2
t = S / V
print(t)'''

'''x = float(input())
if x == 0:
    print('Обратного числа не существует')
else:
    print((x) ** -1)'''

'''tF= float(input())
tC = 5 / 9 * (tF - 32)
print(tC)'''

'''n = float(input())

print(int(n * 10 % 10))'''

'''a = float(input())
b = int(a)
c = a - b
print(c)'''

'''a = max(3.2, 1, 123, -23, 442)
b = min(-2.3, 0.1, 2, -5)
print(a)
print(b)'''

'''print(abs(-2))
print(abs(-17.22))
print(abs(0))'''

'''a, b, c, d, e = int(input()), int(input()), int(input()), int(input()), int(input())
print(f'Наименьшее число = {min(a,b,c,d,e)}')
print(f'Наибольшее число = {max(a,b,c,d,e)}')'''

'''a, b, c = int(input()), int(input()), int(input())
n1, n2 = max(a, b, c), min(a, b, c)
n3 = (a + b + c) - (n1 + n2)
print(n1, n3, n2, sep='\n')'''

'''x = int(input())
fd, sd, td = x // 100, (x % 100) // 10, x % 10
n1, n2 = max(fd, sd, td), min(fd, sd, td)
mid = (fd + sd + td) - (n1 + n2)
if n1 - n2 == mid:
    print('Число интересное')
else:
    print('Число неинтересное')'''

'''a1, a2, a3, a4, a5 = float(input()), float(input()), float(input()), float(input()), float(input())
print(abs(a1) + abs(a2) + abs(a3) + abs(a4) + abs(a5))'''

'''p1, p2, q1, q2 = int(input()), int(input()), int(input()), int(input())
print(abs(p1 - q1) + abs(p2 - q2))'''
