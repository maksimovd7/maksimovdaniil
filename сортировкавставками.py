# insertion_sort.py
# Запуск: python insertion_sort.py

# Вставки: O(n^2) время, O(1) память. На почти отсортированных массивах ~O(n).
def insertion_sort(a):
    for i in range(1, len(a)):
        key = a[i]      # элемент для вставки
        j = i - 1
        # сдвигаем вправо все элементы > key
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key  # вставка на место
    return a

def main():
    arr = [12, 11, 13, 5, 6]
    print("Исходный массив:")
    print(*arr)
    insertion_sort(arr)
    print("Отсортированный массив:")
    print(*arr)

if __name__ == "__main__":
    main()


