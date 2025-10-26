# bubble_sort.py
# Запуск: python bubble_sort.py

# Пузырёк: O(n^2) время, O(1) память. Лучший случай O(n) при раннем выходе.
def bubble_sort(a):
    n = len(a)
    while True:
        swapped = False
        for j in range(1, n):
            if a[j - 1] > a[j]:
                a[j - 1], a[j] = a[j], a[j - 1]
                swapped = True
        n -= 1  # последний элемент уже на месте
        if not swapped or n <= 1:
            break
    return a

def main():
    arr = [64, 34, 25, 12, 22, 11, 90]
    print("Исходный массив:")
    print(*arr)
    bubble_sort(arr)
    print("Отсортированный массив:")
    print(*arr)

if __name__ == "__main__":
    main()

