# def calc1(a, b):
#     return a + b

# calc1 = lambda a, b: a + b

"""
def calc2(a, b):
    return a * b

def math(op, x, y):
    print(op (x, y))

math(lambda a, b: a + b, 5, 45)
"""

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

data = '1 2 3 5 8 15 23 38'.split()
print(data)
data = list(map(int,input().split()))
