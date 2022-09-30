# class Employee:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
# #
#
#     def walk(self):
#          return "I can walk"
#
#
# employee1 = Employee('Alex', 'Smith')
# print(employee1. name)
# print(employee1. surname)
# print(employee1.walk())
# #
# employee2 = Employee(name='Vladimir', surname='Popov')
# print(employee2. name)
# print(employee2. surname)
#
#
# class Developer(Employee):
#     def __init__(self, name, surname, language):
#         super().__init__(name, surname)
#         # self.__language = language
#
#     def coding(self):
#         return "I am coding!"
#
# dev1 = Developer('Max', 'Frolov', 'Python')
# print(dev1.walk())
# print(dev1.name)
# print(dev1.coding())
# We change language after we save language __ not change it
# dev1.set_language('Java')
# print(get_language)

# class Tester(Employee):
#     def __init__(self, name, surname, language, test_framework):
#         super().__init__(name, surname)
#         self.language = language
#         self.test_framework = test_framework
#
#
#     def testing(self):
#             return "I can write"
#
#
# tester1 = Tester('Anna', 'Fedorova', 'Java', 'TestNG')
# print(tester1.testing())
# # #Tester can walk becouse he is Emplotee as well
# print(tester1.walk())
#
# ## Check is dev1 potomok Developer? 1 podclass 2 superclass
# print(isinstance(dev1, Developer))
# print(issubclass(Developer, Employee))
# print(type(dev1))
#
# # Hide (we cant change) can change with set
#
# self.__language = language

    # def get_language(self):
    #     return f'My language is:{self.__language}'