def insert_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Пример использования:
arr = [5, 7, 4, 3, 8, 2]
print(insert_sort(arr))  # Ожидается [2, 3, 4, 5, 7, 8]
