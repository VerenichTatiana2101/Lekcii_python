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

#быстрая сортировка
def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
    less = [i for i in array[1:] if i <= pivot]
    greater = [i for i in array[1:] if i > pivot]
    return quicksort(less) + [pivot] + quicksort(greater)
print(quicksort([38, 27, 43, 3, 9, 82, 10]))


#сортировка слиянием
def merge_sort(nums):
    if len(nums) > 1:
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1

nums = [38, 27, 43, 3, 9, 82, 10]
merge_sort(nums)
print(nums)
