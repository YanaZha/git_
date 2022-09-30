# ВСТРОЕННЫЕ ФУНКЦИИ (BUILT-IN FUNCTIONS)

# min_arg = min(5, 6, 8, 10)
# print(min_arg)
#
# FUNCTIONS

# def person(age, last_name='Smith', name='Anna'):
#     return f'Hello, my name is: {name} {last_name}. I am {age} years old'
#
# print(person(age=30, name='Alice', last_name='Smith'))

# 19*
# def pattern(length, char1='-', char2='*'):
#     return (char1 + char2) * length + char1
#
# print(pattern(char1='*', length=9))


# ПРОСТРАНСТВО ИМЕН (SCOPE)
# x = 15
# y = 78
# def sum_it(x, y):
#     print(f'Locals: {locals()}')
#     return x + y
#
# print(f'Inside the function: {sum_it(5, 8)}')
# print(f'Outside the function: {x + y}')
# print(f'Globals: {globals()}')

# ВСТРОЕННЫЕ МОДУЛИ (BUILT-IN MODULES)
from math import *
# import math as m
#
# arr = [1, 2, 3, 4, 5, 10, 25]
# new_arr = m.prod(arr)
# print(new_arr)

# import datetime
# birth_year = 1980
# current_date = datetime.date.today()
# current_age = current_date.year - birth_year
# current_month = current_date.month
# print(current_date)
# print(current_age)
# print(current_month)

# lambda functions
# mult = lambda x, y: x*y
# print(mult(5, 8))

# Import from my_file
# var1
# import my_file
# res = my_file.sum_it(5, 4)
# print(res)

# var2 * mean all from my file
# from my_file import sum_it, prod
# res = sum_it(5, 8)
# print(res)
#
# res1 = prod(5, 8)
# print(res1)
