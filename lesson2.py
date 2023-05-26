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
dictionary = {}
dictionary ={'up': '↑', 'left': '←', 'down': '↓', 'right': '→'}
print(dictionary) # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
print(dictionary['left']) # ←
# типы ключей могут отличаться
print(dictionary['up']) # ↑
# типы ключей могут отличаться
dictionary['left'] = '⇐'
print(dictionary['left']) # ⇐
print(dictionary['type']) # KeyError: 'type'
del dictionary['left'] # удаление элемента
for item in dictionary: # for (k,v) in dictionary.items():
    print('{}: {}'.format(item, dictionary[item]))
# up: ↑
# down: ↓
# right: →
