def heapify(arr, n, i):
    largest = i  # Індекс найбільшого елемента
    left = 2 * i + 1  # Лівий нащадок
    right = 2 * i + 2  # Правий нащадок

    # Якщо лівий нащадок більший за корінь
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Якщо правий нащадок більший за поточний найбільший
    if right < n and arr[right] > arr[largest]:
        largest = right

    # Якщо найбільший не корінь
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Обмін
        heapify(arr, n, largest)  # Рекурсивно heapify піддерево

def heap_sort(arr):
    n = len(arr)

    # Побудова max-heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Вилучення елементів по одному
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Обмін
        heapify(arr, i, 0)

# Приклад використання
arr = [17, 13, 31, 43, 26, 47, 32, 112, 2, 63]
heap_sort(arr)
print("Відсортований масив:", arr)
