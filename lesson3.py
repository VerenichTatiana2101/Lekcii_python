# # Функции

# def sum_numbers(n) :  #в шарпе писали название с большой буквы
#     summa = 0
#     for i in range(1, n + 1) :  #n + 1, так как range не включает последнийэлемент
#         summa += i
#     print(summa)

# sum_numbers(5)

# def sum_numbers(n) :  
#     summa = 0
#     for i in range(1, n + 1) :
#         summa += i
#     return summa  #программа завершает работу

# print(sum_numbers(5))

# def sum_numbers(n) : 
#     summa = 0
#     for i in range(1, n + 1) :
#         summa += i
#     return summa   
# a = sum_numbers(5)

# print(a)  #сколько аргументов приняли, столько и передали наоборот

# def sum_numbers(n, y = 'Hello') : #указали значение у по умолчанию
#     print(y)   #передача второго вргумента
#     summa = 0
#     for i in range(1, n + 1) :
#         summa += i
#     return summa   
# a = sum_numbers(5)

# print(a)  #при вызове второй аргумент не указываем

# def sum_numbers(n, y = 'Hello') : #указали значение у по умолчанию
#     print(y)   #передача второго вргумента
#     summa = 0
#     for i in range(1, n + 1) :
#         summa += i
#     return summa   
# a = sum_numbers(5, 'qwert')  #в данном случае выведет это а не хэлло

# print(a)  #при вызове второй аргумент не указываем


# # Возможность передачи неограниченного количества аргументов
# def concatenatio(*params):
#     res = ""
#     for item in params:
#         res += item
#     return res
# print(concatenatio('a', 's', 'd', 'w')) # asdw
# print(concatenatio('a', '1')) # a1
# # print(concatenatio(1, 2, 3, 4)) # TypeError: ...


# def sum_str(*args) :
#     res = ''
#     for i in args :
#         res += i
#     return res

# print(sum_str('q', 'e', 'l'))
# print(sum_str('q', 'e', 'l',' ', 'hello'))



"""
Модульность
"""
#импорт
import modul

print(modul.max1(5, 9))

