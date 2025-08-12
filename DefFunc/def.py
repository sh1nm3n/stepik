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

def print_hello(txt, n):
    print(txt * n)


print_hello('abc', 5)