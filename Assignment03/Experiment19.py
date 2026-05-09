import time
import random


def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(n - i - 1):

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def insertion_sort(arr):

    for i in range(1, len(arr)):

        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:

            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key


def benchmark(sort_function, arr):

    start = time.time()

    sort_function(arr.copy())

    end = time.time()

    return end - start


data = [random.randint(1, 1000) for _ in range(1000)]

print("Bubble Sort Time:", benchmark(bubble_sort, data))
print("Insertion Sort Time:", benchmark(insertion_sort, data))