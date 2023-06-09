# def calc1(a, b):
#     return a + b

# calc1 = lambda a, b: a + b


# def calc2(a, b):
#     return a * b

# def math(op, x, y):
#     print(op (x, y))

# math(lambda a, b: a + b, 5, 45)


# 1. В списке хранятся числа. Нужно выбрать только чётные числа и составить
# список пар (число; квадрат числа).
# Пример: 1 2 3 5 8 15 23 38
# Получить: [(2, 4), (8, 64), (38, 1444)]

"""
array = [1, 2, 3, 5, 8, 15, 23, 38]
rez = []

for i in array:
    if i %2 == 0:
        rez.append((i, i ** 2))
print(rez)
"""

# def select(f, col):
#     return [f(x) for x in col]

# def where(f, col):
#     return [x for x in col if f(x)]

# data = [1, 2, 3, 5, 8, 15, 23, 38]
# res = select(int, data)
# print(res) 
# res = where(lambda x: x % 2 == 0, res)
# print(res)

# res = list(select(lambda x: (x, x**2), res))
# print(res)

"""
list_1 = [x for x in range (1,20)]
list_1 = list(map(lambda x: x + 10, list_1 ))
print(list_1)
"""

# Задача: C клавиатуры вводится некий набор чисел, в качестве разделителя используется
# пробел. Этот набор чисел будет считан в качестве строки. Как превратить list строк в list чисел?
"""
data = '1 2 3 5 8 15 23 38'
print(data)
data = list(map(int,data.split()))
print(data)
"""

# # filter
# data = [15, 65, 9, 36, 175]
# res = list(filter(lambda x: x % 10 == 5, data))
# print(data)
# print(res)

# ИТОГ:
# map = # def select(f, col):
#       #    return [f(x) for x in col]
  
# filter = # def where(f, col):
#          #     return [x for x in col if f(x)]
# Наш изначальный ког получится таким:
"""
data = [1, 2, 3, 5, 8, 15, 23, 38]
res = map(int, data)
res = filter(lambda x: x % 2 == 0, res)
res = list(map(lambda x: (x, x**2), res))
print(res)
"""

# #zip
# #пример1
# users = ['user1', 'user2', 'user3', 'user4']
# ids = [4, 5, 6, 7]
# data = list(zip(users, ids))
# print(data)

# #пример2
# users = ['us1', 'us2', 'us3', 'us4', 'us5']
# ids = [4, 5, 9, 14, 7]
# salary = [111, 222, 333]
# data = list(zip(users, ids, salary))
# print(data)

# # enumerate
# users = ['user1', 'user2', 'user3']
# data = list(enumerate(users))
# print(data)

# работа с файлами
"""
1. Режим a
"""
# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'a') # здесь указываем режим, в котором будем работать
# data.writelines(colors) # разделителей не будет
# data.close()
###############
# with open('file.txt', 'w') as data:
#     data.write('line 1\n')
#     data.write('line 2\n')
"""
2. Режим r
"""
# # ● Чтение данных из файла:
# path = 'file.txt'
# data = open('file.txt', 'r')
# for line in data:
#     print(line)
# data.close()
"""
3. Режим w
"""
# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'w')
# data.writelines(colors) # разделителей не будет
# data.close()

