# 3.1. Дан список my_list = ['a', 'b', [1, 2, 3], 'd']. Распечатайте значения 1, 2, 3
# my_list = ['a', 'b', [1, 2, 3], 'd']
# print(*my_list[-2])

# for x in range(len(my_list)):
#     print(*my_list[x], end=' ')

# 3.2 Дан список list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
#    - получите сумму всех чисел,
#    - распечатайте все строки, где есть буква 'a'

# list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
# tuple1 = (*list_1,)
# print(tuple1)
# result = tuple(filter(lambda x: isinstance(x, int), tuple1))
# print(result)
# print(sum(result))

# list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
# print('Original list: ', list_1)
# print('Sum of all numbers: ', sum([x for x in list_1 if type(x) == int]))
# print('All words with a: ', [y for y in list_1 if type(y) == str and "a" in y])

# How many word "Hi"
# list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
# tuple1 = (*list_1,)
# print(tuple1)
# print(tuple1.count(str('Hi')))
#
# list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
# for string in list_1:
#     if type(string) == str:
#         if string.find('a') !=-1:
#              print(string)

# 3.3. Превратите лист ['cat', 'dog', 'horse, 'cow'] в кортеж
# list_1 = ['cat', 'dog', 'horse', 'cow']
# tuple1 = tuple(list_1)
# print(tuple1)

# list_1 = ['cat', 'dog', 'horse', 'cow']
# tuple1 = (*list_1,)
# print(tuple1)
#
# 3.4. Напишите программу, которая определяет, какая семья больше.
#       1) Программа имеет два input() - например, family_1, family_2.
#       2) Членов семьи нужно перечислить через запятую.
#      Ожидаемый результат - программа выводит семью с бОльшим составом. Если состав одинаковый, print("Equal')
#
# family_1 = input("Перечислите через запятую имена членов первой семьи: ").split(',')
# family_2 = input("Перечислите через запятую имена членов второй семьи: ").split(',')
# family_1_members = len(family_1)
# family_2_members = len(family_2)
# print(f"В первой семье {family_1_members} чл.")
# print(f"Во второй семье {family_2_members} чл.")
# if family_1_members > family_2_members:
#     print("Первая семья больше. The first family is the biggest")
# elif family_2_members > family_1_members:
#     print("Вторая семья больше. The second family is the biggest")
# else:
#     print("Семьи равны. Equal")

# print("Equal" if len(family_1) == len(family_2) else family_2 if len(family_2) > len(family_1) else family_1)

# 3.5. Создайте словарь film c ключами title, director, year, budget, main_actor, slogan. В значения можете передать информацию
#     о вашем любимом фильме.
#     - распечатайте только ключи
#     - распечатайте только значения
#     - распечатайте пары ключ - значение
#
# film = {"date" : 1992, "budget" : 1000000, "main_actor" : "Mamonov", "slogan" : "God with us"}
# film = dict([("date" , 1992), ("budget" , 1000000), ("main_actor", "Mamonov"), ("slogan" , "God_with us")])
# print(film)
# print(*list(film.keys()))
# print(*list(film))
# print(*list(film.values()))
# print(*list(film.items()))

# print(*film.keys())
# print(*film.values())
# print(*film.items())
# 3.6. Найдите сумму всех значений в словаре my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
#
# my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
# a = dict.values(my_dictionary)
# print(a)
#
# print sum(my_dictionary.value)

# 3.7. Удалите повторяющиеся значения из списка [1, 2, 3, 4, 5, 3, 2, 1]
# a = [1, 2, 3, 4, 5, 3, 2, 1]
# b = set(a)
# c = list(b)
# print(c)

# 3.8. Даны два множества: set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}, set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
#      - найдите значения, которые встречаются в обоих множествах
#      - найдите значения, которые не встречаются в обоих множествах
#      - проверьте являются ли эти множества подмножествами друг друга
# Common1
# set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}
# set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
# q = set(set1) & set(set2)
# print(q)

# Common2
# set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}
# set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
# x = set(set1).intersection(set(set2))
# print(x)

# Difference(simmetrichnoe raznoe)
# q = set(set1) ^ set(set2)
# print(q)

# Each other
# set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}
# set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
# a = set(set1) - set(set2)
# b = set(set2) - set(set1)
# if set1 <= set2:
#     print('True')
# else:
#     print('False')

# set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}
# set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
# set1.issubset(set2)
# print('True')

# set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}
# set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
# print(set1 & set2) #пересечение множества
# print(set1 - set2) #разные значения в set1
# #
# diff_set = set1.difference(set2)
# print(diff_set) #Разница между множествами
# #
# set_diff = set1.symmetric_difference(set2)
# print(set_diff) #Симметричная разница множеств
# #
# print(set1 <= set2)  #подмножества
# print(set2.issubset(set1)
