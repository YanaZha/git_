#Вам дали два подсолнуха
flower1 = ['g','r','r','g','g','g','g','g','r','r','g','g','g','g','r','g','g','e','r','r','e','g','g','g','g','r','r','r','g','e']
flower2 = ['g','g','g','r','g','g','e','r','r','e','g','g','g','g','r','r','r','g','e']

#нужно 'good seeds' положить в мешок, а 'rotten and empty seeds' в ведро использовать цикл for and while.
#и подсчитайте сколько у вас семян в ведре и в мешке использовать метод

# tuple1 = (*list(flower1),)
# tuple2 = (*list(flower2),)
# tuple3 = tuple(tuple1)+tuple(tuple2)
# print(tuple3)

flower3 = list(flower1)+list(flower2)
seeds = (*tuple(flower3),)
print(seeds)

print(seeds.count(str('g')))
print(f'Good seeds: {(seeds.count str('g'))}'

# r = seeds.count(str('r'))
# e = seeds.count(str('e'))
# print(sum((r, e)))

# new_list = [r+e]
# print(*new_list,)
# print(seeds.count(str('r')))
# print(seeds.count(str('e')))
# print(len(sum(int(r, e))))
# for i in seeds:
#     if i = 'g'
#     i+=1
#     print(len())

