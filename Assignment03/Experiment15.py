def insertion_sort(arr):
    comparisons = 0

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            comparisons += 1
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    print("Sorted Array:", arr)
    print("Comparisons:", comparisons)

arr = [12, 11, 13, 5, 6]
insertion_sort(arr)