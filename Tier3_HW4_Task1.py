import timeit
import random

# Реалізація сортування вставками
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Реалізація сортування злиттям
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr

# Використання вбудованого методу sort для Timsort
def timsort(arr):
    arr.sort()
    return arr

# Функція для генерації масиву випадкових чисел
def generate_random_array(size):
    return [random.randint(1, 10000) for _ in range(size)]

# Розміри масивів для тестування
sizes = [100, 1000, 10000]

# Словник для зберігання результатів тестування
results = {}

# Тестування алгоритмів
data_sizes = [100, 1000, 10000]  # Розміри наборів даних

for size in data_sizes:
    data = [random.randint(0, 1000) for _ in range(size)]

    print() 

    merge_sort_time = timeit.timeit(lambda: merge_sort(data.copy()), number=1)
    print(f"Merge sort for {size} elements: {merge_sort_time} seconds")

    insertion_sort_time = timeit.timeit(lambda: insertion_sort(data.copy()), number=1)
    print(f"Insertion sort for {size} elements: {insertion_sort_time} seconds")

    timsort_time = timeit.timeit(lambda: sorted(data.copy()), number=1)
    print(f"Timsort for {size} elements: {timsort_time} seconds")

    
