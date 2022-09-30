# task 1
# 1.1
# x = int(input('Character_health: '))
# if x <= 0:
#     print('False')
# else:
#     print('True')

# x = int(input('Character_health: '))
# if x <= 0:
#     print('Dead!')
# else:
#     print('Good!')

# x = int(input('Character_health: '))
# if x <= 0:
#     print(bool(0))
# else:
#     print(bool(1))

# Task2
# Even-Odd
# i = int(input('Enter_number: '))
# if i % 2 == 0:
#     print('Even')
# else:
#     print('Odd')


# # Task3
# # Year
# i = int(input('year: '))
# if i % 4 == 0 \
#         and i%100:
#     print('leap_year: ')
# elif i % 400 == 0:
#     print('leap_year: ')
# else:
#     print('non_leap_year')

# year = int(input('year: '))
# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#     print('leap_year: ')
# else:
#     print('non_leap_year')
# doesnt work for 100, 500, 600
# year = int(input('year: '))
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print('leap_year')
#         else:
#             print('non_leap_year')
#     else:
#         print('leap_year')
# else:
#     print('non_leap_year')
# mine 100, 500, 600
# year = int(input('year: '))
# if year % 4 == 0:
#     if year % 100 != 0:
#         if year % 400 == 0:
#             print('leap_year')
#         else:
#             print('non_leap_year')
#     else:
#         print('leap_year')
# else:
#     print('non_leap_year')

#   if i % 100 != 0:
#     print('non_leap_year')
# else i % 400 == 0:
#     print('non_leap_year')

# i = int(input('Is this leap_year: '))
# print(i % 4 == 0 and i % 400 == 0)



# i = int(input('year: '))
# if i % 4 == 0 and i % 100 == 0 and i % 400 == 0:
#     print('leap_year')
# else:
#     print('non_leap_year')

# Task4
# 1.1
# i = input('Text: ')
# n = int(input('How many times?' ))
# for i in range(n):
#     print('i')

# 1.2
# for i in range(5):
#     print('Knowledge is light!')

# # 1.3
# n = input('How many times? ')
# i = input('Text: ')
#  while n > 1:
#     print('i')
#     i = i+1

# 1.4
# n = input('How many times?')
# i = input('Text')
# print(i*int(n))

# i = input('Text: ')
# n = int(input('How many times?' ))
# for index in range(1, n+1):
#     print(index, 'i')
