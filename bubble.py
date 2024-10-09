def bubble_sort(arr):
    n = len(arr)
    for run in range(n-1):
        for i in range(n-1-run):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return arr

# Пример использования:
arr = [5, 7, 4, 3, 8, 2]
print(bubble_sort(arr))  # Ожидается [2, 3, 4, 5, 7, 8]
