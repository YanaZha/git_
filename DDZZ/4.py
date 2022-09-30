#4.1. Напишите функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения (с помощью кортежа):
#      периметр квадрата, площадь квадрата и диагональ квадрата.
# 'Perimetr'
# from my_file import perimetr
# per = perimetr(5)
#
# 'Area'
# from my_file import area
# ar = area(5)
#
# 'Hipotenuza'
# from my_file import hipotenusa
# hip = hipotenusa(5)
# hip1 = round(hip)
# print([per, ar, hip1])


# 4.2. Напишите фукнцию, которая принимает произвольное количество именнованных аргументов и выводит их построчно
#      в формате аргумент: значение. Например:

# name: John
# last_name: Smith
# age: 35
# position: web_developer

# def person(name, last_name, age, position):
#     return f'name: {name} \n last_name: {last_name} \n age:{age} \n position: {position}'
#
# print(person('john', 'Smith', 35, 'web developer'))


# def person(name, last_name, age, position):
#     return f'Personal data: {name} {last_name} {age},{position}'
# print(person('john', 'Smith', 35, 'web developer'))

# def print args(**kwargs):
#    for key, value in kwargs.items():
#        print(f'{key}:{str(value)}')

name_args = dict(name = 'John', last_name = Smith, age = 35 , position = 'web_developer')
print(name_args)

# def name_args(**kwargs):
#    for key, value in kwargs.items():
#        print("{}:{}".format(key. value))

# 4.3. Используя лямбда-выражение, из списка my_list = [20, -3, 15, 2, -1, -21] создайте новый список, содержащий только
#      положительные числа

# my_list = [20, -3, 15, 2, -1, -21]
# pos_nums = filter(lambda x: x >= 0, my_list)
# print(list(pos_nums))

# 4.4. Используя лямбда выражение, получите результат перемножения значений в предыдущем списке
# -37800
# my_list = [20, -3, 15, 2, -1, -21]
# from functools import reduce
# mult_nuns = reduce(lambda x , y: x*y,  my_list)
# print(mult_nuns)

# -37800
# import math
# my_list = [20, -3, 15, 2, -1, -21]
# mult_nuns = math.prod(my_list)
# print(mult_nuns)

# -37800
# import math as m
# my_list = [20, -3, 15, 2, -1, -21]
# mult_nuns = m.prod(my_list)
# print(mult_nuns)

# -37800
# mult = lambda  x,y,n,u,j,k: x*y*n*u*j*k
# print(mult(20, -3, 15, 2, -1, -21))

# my_list = [20, -3, 15, 2, -1, -21]
# def mult_it(num):
# result = 0
#  for x in my_list:
#      return x +=1
#      print(mult_it)


# 4.5. Создайте файл my_calc.py и пропишите в нем минимум 4 функции, выполняющие базовые арифметические вычисления.
#      Примените эти функции в качестве методов в другом файле.

# from my_calc import *
# sum1 = sum_it(15, 5)
# dif = difference_it(15, 5)
# mult = mult_it(15, 5)
# div = div_it(15, 5)
#
# print(f'Summa:{sum1}')
# print(f'Difference:{dif}')
# print(f'Multiplication:{mult}')
# print(f'Division:{div}')

# import _datetime
# birth_year = 1969
# current_date = _datetime.date.today()
# age = current_date.year-birth_year
#
# print(current_date)
# print(age)