# bubble Sort

def bubble_sort(arr):
    n = len(arr)
    comparisons = 0
    swaps = 0

    for i in range(n):
        for j in range(0, n - i - 1):
            comparisons += 1

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1

    print("Sorted Array:", arr)
    print("Comparisons:", comparisons)
    print("Swaps:", swaps)

arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)


# Selection Sort

def selection_sort(arr):
    comparisons = 0
    swaps = 0

    for i in range(len(arr)):
        min_index = i

        for j in range(i + 1, len(arr)):
            comparisons += 1

            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]
        swaps += 1

    print(arr)
    print("Comparisons:", comparisons)
    print("Swaps:", swaps)

arr = [29, 10, 14, 37, 13]
selection_sort(arr)