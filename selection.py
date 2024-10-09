def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

# Пример использования:
arr = [5, 7, 4, 3, 8, 2]
print(selection_sort(arr))  # Ожидается [2, 3, 4, 5, 7, 8]
