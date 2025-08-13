'''class Solution:
    '''

#забросил
'''def romanToInt(s: str):
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    for i in range(len(s)):
        if s[i] in roman_dict:
            if s[i] == 'V' and s[i - 1] == 'I':
                result += 4
            elif s[i] == 'X' and s[i - 1] == 'I':
                result += 9
            elif s[i] == 'L' and s[i - 1] == 'X':
                result += 40
            elif s[i] == 'C' and s[i - 1] == 'X':
                result += 90
            elif s[i] == 'D' and s[i - 1] == 'C':
                result += 400
            elif s[i] == 'M' and s[i - 1] == 'C':
                result += 900
            else:
                result += roman_dict.get(s[i])
    print(result)

romanToInt('MCM')'''

'''def simple_multiplication(number) :
    if number % 2 == 0:
        return number * 8
    else:
        return number * 9

print(simple_multiplication(3))
'''

'''def narcissistic(value):
    power, summa, digits_list = 0, 0, []
    original_value = value
    while value != 0:
        digit = value % 10
        digits_list.insert(0, digit)
        value //= 10
        power += 1
    for el in digits_list:
        summa += el ** power
    if summa == original_value:
        return True
    else:
        return False

print(narcissistic(1938))'''

'''def remove_char(s):
    return s[1:-1]

a = remove_char('')
print(a)'''
