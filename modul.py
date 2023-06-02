# def max1(a, b) :
#     if a > b :
#         return a
#     return b

# def fib(n):
#     if n in [1, 2]:
#         return 1
#     return fib(n - 1) + fib(n - 2)
# list_1 = []
# for i in range(1, 10):
#     list_1.append(fib(i - 2))
# print(list_1) # [1, 1, 2, 3, 5, 8, 13, 21, 34]

# def fib(n):
#     if n <= 1:
#         return n
#     else:
#         return fib(n-1) + fib(n-2)

# n = int(input("Введите номер числа Фибоначчи: "))
# print(fib(n + 1))


def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
    less = [i for i in array[1:] if i <= pivot]
    greater = [i for i in array[1:] if i > pivot]
    return quicksort(less) + [pivot] + quicksort(greater)
print(quicksort([10, 5, 2, 3]))

if 