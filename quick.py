def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr if x < pivot]
    center = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + center + quick_sort(right)

# Пример использования:
arr = [5, 7, 4, 3, 8, 2]
print(quick_sort(arr))  # Ожидается [2, 3, 4, 5, 7, 8]
