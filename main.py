# n = 5 целое число
# n = 1.89 дробные числа
# n = None пустое значение переменной
# print(n)

# n1 = 'это' строка
# print(n1)
# n2 = "интересно"
# print(n2)

# n = 5
# print(type(n)) вывод типа данных

# n = 'hello\'world' #если нужно вывести строку с ковычкой, перед ней ставим \, или оборачиваем в ""
# print(n)
"""
print(5)
print(5, 8)
print(5)
print(5)
print(5, 9)
"""
# a = 5
# b = 1.89
# c = 'hello'
# print(a, b , c)
# print(a, '-', b, '-', c)
# print(f"{a} - {b} - {c}")
# print("{} - {} - {}".format(a, b ,c))

""""
print('Введите первое число: ')
a = input()
print(a)
b = input('Введите второе число: ')
print(a, '+', b, '=', a + b) в данном случае выведет два числа в строку 3+3 =33
"""

# c = 5.89
# print(c)
# n = int(c)
# print(n) выведет 5
"""
c = 5.89
print(c)
print(type(c))
c = int(c)
print(c)
print(type(c))
"""

# v = 'hello'
# v = int(v)
# print(v)
"""
print('Введите первое число: ')
a = int(input())   #int сразу переводит строку в число и программа уже считает числа
print(a)
b = int(input('Введите второе число: '))
print(a, '+', b, '=', a + b) 
"""

# a = 5.89956    #не указываем int, потому что нет input
# b = 6.556551
# print(round(a*b, 3))

"""
iter = 2
iter += 3 # iter = iter + 3
iter -= 4 # iter = iter - 4
iter *= 5 # iter = iter * 5
iter /= 5 # iter = iter / 5
iter //= 5 # iter = iter // 5
iter %= 5 # iter = iter % 5
iter **= 5 # iter = iter ** 5
"""

# a = 1 > 4
# print(a) # False

# a = 1 < 4 and 5 > 2 #оператор and объединяет условия
# print(a) # True

# a = 1 == 2  #в данном случае результат тоже будет правда или ложь, даже если правда значение в переменную для вывода принт не перекладывает
# print(a) # False

# a = 1 != 2
# print(a) # True

# a = 'qwe'
# b = 'qwe'
# print(a == b) # True

# a = 1 < 3 < 5 < 10
# print (a) # True
#################
# username = input('Введите имя: ')
# if username == 'Маша':
#     print('Ура, это же МАША!')
# elif username == 'Марина':
#     print('Я так ждала Вас, Марина!')
# elif username == 'Ильнар':
#     print('Ильнар - топ)')
# else:
#     print('Привет, ', username)
"""
n = 423
summa = 0
while n > 0:
    x = n % 10
    summa = summa + x
    n = n // 10
print(summa) # 9
"""

# i = 0
# while i < 5:
#     if i == 3:
#         break  тут прекращается работа не самостоятельно и блок else не работает
#     i = i + 1
# else:
#     print('Пожалуй')
#     print('хватит )')
# print(i)

"""
n = int(input('Введите число: '))
flag = True
i = 2
while flag:
    if n % i == 0: # если остаток при делении числа n на i равен 0
        flag = False
        print(i)
    elif i > n // 2: # делить числа не может превышать введенное число, деленноена 2
        print(n)
        flag = False 
    i += 1
"""

# n = 423
# summa = 0
# while summa > 0:
#     x = n % 10
#     summa = summa + x
#     n = n // 10
# else:
#     print('Пожалуй')
#     print('хватит )')
# print(summa)
# Пожалуй
# хватит )
# 9

"""
r = range(5) # 0 1 2 3 4
r = range(2, 5) # 2 3 4
r = range(-5, 0) # ----
r = range(1, 10, 2) # 1 3 5 7
r = range(100, 0, -20) # 100 80 60 40 20

r = range(100, 0, -20) # range(100, 0, -20)
for i in r:
    print(i)
100 80 60 40 20
"""

# for i in 'qwerty':
#     print(i)

#строки
# text = 'СъЕШЬ ещё этих МяГкИх французских булок'
# print(len(text)) # 39 символов в строке
# print('ещё' in text) # True в строке есть слово ещё
# print(text.lower()) # съешь ещё этих мягких французских булок, всё с маленькой буквы
# print(text.upper()) # СЪЕШЬ ЕЩЁ ЭТИХ МЯГКИХ ФРАНЦУЗСКИХ БУЛОК всё с большой
# print(text.replace('ещё','ЕЩЁ')) # СъЕШЬ ЕЩЁ этих МяГкИх французских булок замена

text = 'съешь ещё этих мягких французских булок'
# print(text[0]) # c
# print(text[1]) # ъ
# print(text[len(text)-1]) # к
# print(text[-5]) # б индексация с конца строки
# print(text[:]) # съешь ещё этих мягких французских булок, все символы
# print(text[:2]) # съ с 0 по 2 индекс, второй не включая
# print(text[len(text)-2:]) # ок два последних
# print(text[2:9]) # ешь ещё начинаем со второго элемента по 9, не включая
# print(text[6:-18]) # ещё этих мягких с 6 по -18 элементы
# print(text[0:len(text):6]) # сеикакл, от 0 до конца строки с шагом 6, каждый 6 элемент
# print(text[::6]) # сеикакл, от 0 до конца строки с шагом 6, каждый 6 элемент
# text = text[2:9] + text[-5] + text[:2] # ...
