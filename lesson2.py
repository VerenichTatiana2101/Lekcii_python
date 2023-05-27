"""
list_1 = [] # Создание пустого списка
list_2 = list() # Создание пустого списка
list_1 = [7, 9, 11, 13, 15, 17] #нумерация начинается с 0
print(*list_1)  #поставив * печатает без скобок и запятых
for i in list_1:
    print(i)  #поочерёдно выводим элементы списка
print(len(list_1))  #размер списка
print(list_1[1])  #выводим элемента списка с индексом 1(индексация начинается с 0)
print(list_1[-1]) #индексация с конца результат 17
list_1.append(8)  #добавили в список элемент 8
print(list_1)
list1 = []
for i in range(5):
    list1.append(i)  #поочерёдно добавляем значения от 0 до 4 в наш список
    print(list1)
"""

# #Метод pop удаляет последний элемент из списка:
# list_1 = [12, 7, -1, 21, 0]
# # print(list_1.pop()) # 0
# # print(list_1) # [12, 7, -1, 21]
# # print(list_1.pop()) # 21
# # print(list_1) # [12, 7, -1]
# # print(list_1.pop()) # -1
# print(list_1) # [12, 7]

# #Удаление конкретного элемента из списка.
# #Надо указать значение индекса в качестве аргумента функции pop:
# print(list_1.pop(0))
# print(list_1)

# Добавление элемента на нужную позицию.
# Функция insert — указание индекса (позиции) и значения.
# list_2 = [12, 7, -1, 21, 0]
# print(list_2)
# print(list_2.insert(2, 11))  #2 это позиция(индекс), 11 это элемент который нужно вставить
# print(list_2) # [12, 7, 11, -1, 21, 0]

# # Срез списка
# # Отрицательное число в индексе — счёт с конца списка
# list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list_1)
# print(list_1[0]) # 1 печать нулевого элемента
# print(list_1[1]) # 2
# print(list_1[len(list_1)-1]) # 10 печать последнего
# print(list_1[-5]) # 6 пятого с конца
# print(list_1[:]) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] от начвала до конца списка
# print(list_1[:2]) # [1, 2] сначала до второго его не включая
# print(list_1[len(list_1)-2:]) #[9, 10] двух последних
# print(list_1[2:9]) # [3, 4, 5, 6, 7, 8, 9] от второго элемента до 9 не включая его
# print(list_1[6:-18]) # [] 
# print(list_1[0:len(list_1):6]) # [1, 7] сначала до конца с шагом 6 [::6]
# print(list_1[::6]) # [1, 7]

# # Кортеж — это неизменяемый список. занимает мало памяти и в сравнении со списком работает быстрее
# t = () # создание пустого кортежа
# print(type(t)) # class <'tuple'>
# t = (1,)  #для определения картежа необходимо всегда оставлять запятую
# print(type(t))
# t = (1)
# print(type(t))
# t = (28, 9, 1990)
# print(type(t))
# colors = ['red', 'green', 'blue']
# print(colors) # ['red', 'green', 'blue']
# t = tuple(colors)  #выводим картеж цветов
# print(t) # ('red', 'green', 'blue')
# t = tuple(['red', 'green', 'blue'])
# print(t[0]) # red
# print(t[2]) # blue
# for e in t:
#     print(e) # red green blue
# t[0] = 'black' # TypeError: 'tuple' object does not support(нельзя изменять кортеж)

# a, b = 1, 2 #возможно такое присваивание

# Словари — неупорядоченные коллекции произвольных объектов с
# доступом по ключу.
# dictionary = {}
# dictionary ={'up': '↑', 'left': '←', 'down': '↓', 'right': '→'}
# print(dictionary) # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
# print(dictionary['left']) # ←
# # типы ключей могут отличаться
# print(dictionary['up']) # ↑
# # типы ключей могут отличаться
# dictionary['left'] = '⇐'
# print(dictionary['left']) # ⇐
# # print(dictionary['type']) # KeyError: 'type'
# del dictionary['left'] # удаление элемента
# for item in dictionary: # for (k,v) in dictionary.items():
#     print('{}: {}'.format(item, dictionary[item]))
# up: ↑
# down: ↓
# right: →

"""
Множества содержат в себе уникальные элементы, не обязательно
упорядоченные.
Одно множество может содержать значения любых типов. Если у Вас есть два
множества, Вы можете совершать над ними любые стандартные операции,
например, объединение, пересечение и разность.
"""
# colors = {'red', 'green', 'blue'}
# print(colors) # {'red', 'green', 'blue'}
# colors.add('red')
# print(colors) # {'red', 'green', 'blue'}
# colors.add('gray')
# print(colors) # {'red', 'green', 'blue','gray'}
# colors.remove('red')  #удалить первое вхождение элемента с указанным значением из списка
# print(colors) # {'green', 'blue','gray'}
# # colors.remove('red') # KeyError: 'red'
# colors.discard('red') # ok удаляет из множества
# print(colors) # {'green', 'blue','gray'}
# colors.clear() # { } удаляет все элементы из списка
# print(colors) # set()

"""
Операции со множествами в Python
"""
# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# c = a.copy() # c = {1, 2, 3, 5, 8} создаёт список c и копирует туда множества из списка "a"
# u = a.union(b) # u = {1, 2, 3, 5, 8, 13, 21} создаёт список "u" и добавляет недостающие элементы из списка "b"
# i = a.intersection(b) # i = {8, 2, 5} создаёт список "i" с пересекающимися элементами списков "a" "b"
# dl = a.difference(b) # dl = {1, 3} создаёт список "d1" из списка "a" выбирает элементы не пересекающиеся со списком "b"
# dr = b.difference(a) # dr = {13, 21} создаёт список "dr" из списка "b" выбирает элементы не пересекающиеся со списком "a"
# q=a.union(b).difference(a.intersection(b)) # {1, 21, 3, 13} выбирает не пересекающиеся элементы из обоих списков

"""
Неизменяемое или замороженное множество(frozenset) — множество, с которым
не будут работать методы удаления и добавления.
"""
# a = {1, 2, 3, 5, 8}
# b = frozenset(a)
# print(b) # frozenset({1, 2, 3, 5, 8})

"""
List comprehension — это упрощенный подход к созданию списка, который
задействует цикл for, а также инструкции if-else для определения того, что в итоге
окажется в финальном списке.
"""
# # 1. Простая ситуация — список:
# list_1 = [exp for item in iterable]
# # 2. Выборка по заданному условию:
# list_1 = [exp for item in iterable (if conditional)]

"""
Задача: Создать список, состоящий из четных чисел в диапазоне от 1 до 100.
"""
# 1. Создать список чисел от 1 до 100
list_1 = []
# for i in range(1, 101):
#     list_1.append(i)
# print(list_1) # [1, 2, 3,..., 100]
# Эту же функцию можно записать так:
# list_1 = [i for i in range(1, 101)] # [1, 2, 3,..., 100]
# print(list_1)
# # 2. Добавить условие (только чётные числа)
# list_1 = [i for i in range(1, 101) if i % 2 == 0] # [2, 4, 6,..., 100]
# print(list_1)
# Допустим, вы решили создать пары каждому из чисел (кортежи)
# list_1 = [(i, i) for i in range(1, 101) if i % 2 == 0] # [(2, 2), (4, 4),...,(100, 100)]
# print(list_1)
# Также можно умножать, делить, прибавлять, вычитать. Например, умножить
# значение на 2.
list_1 = [i * 2 for i in range(10) if i % 2 == 0]
print(list_1) # [0, 4, 8, 12, 16]

"""
Профилирование и отладка
Самые распространенные ошибки:
1.SyntaxError(Синтаксическая ошибка)
"""
# number_first = 5
# number_second = 7
# if number_first > number_second   #!!!!
#     print(number_first)
# # Отсутствие двоеточия в строчке с if
"""
IndentationError(Ошибка отступов)
"""
# number_first = 5
# number_second = 7
# if number_first > number_second:
# print(number_first) # !!!!!
# # Отсутствие отступов
"""
TypeError(Типовая ошибка)
"""
# text = 'Python'
# number = 5
# print(text + number)
# # Нельзя складывать строки и числа
"""
ZeroDivisionError(Деление на 0)
"""
# number_first = 5
# number_second = 0
# print(number_first // number_second)
# # Делить на 0 нельзя
"""
KeyError(Ошибка ключа)
"""
# dictionary = {1: 'Monday', 2: 'Tuesday'}
# print(dictionary[3])
# # Такого ключа не существует
"""
NameError(Ошибка имени переменной)
"""
# name = 'Ivan'
# print(names)
# # Переменной names не существует
"""
ValueError(Ошибка значения)
"""
# text = 'Python'
# print(int(text))
# # Нельзя символы перевести в целые значения
