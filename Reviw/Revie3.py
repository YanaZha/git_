# list_1 = [1, 6, 4, 7, 9, 1, 2, 7]
# print(list_1)
# print(id(list_1))
# list_1.sort()
# print(id(list_1))
# print(list_1)
# Or
# print(sorted(list_1))
# print(id(list_1))

# new = [x*x for x in list_1 if x % 2 == 0]
# print(new)

# !!!!!!!
# new_2 = filter(Lambda x:isinstance(x %2 ==0), list_1)
# print(new_2)
# print(*new_2)

# tuple_0 = ('Mark',)
# print(type(tuple_0))
#
# tuple_1 = ('Mark', 26, ['314 N 11Ln', 'LA', 85954])
# print(tuple_1)
#
# list_3 = list(tuple_1)
# print(list_3)
#
# list_3[1] = 27
# print(list_3)
#
# tuple_1 = tuple(list_3)
# print(tuple_1)
#
# tuple_1[2][-1] = 85955
# print(tuple_1)

# list_1 = [1, 6, 4, 7, 9, 1, 2, 7]
# dict_1 = {}
# for ind in range(len(list_1)):
#     dict_1[ind] = list_1[ind]
# print(dict_1)
#
# print(dict_1.keys())
# print(dict_1.values())
# print(dict_1.items())
#
# for ind, val in enumerate(dict_1.items(), 100):
#     print(f'{ind} ---> {val}')
#
# print(dict_1.get(1))
