# binary_search.py
# Запуск: python binary_search.py

# Бинарный поиск: O(log n) время, O(1) память. Требует отсортированный массив.
def binary_search(a, target):
    left, right = 0, len(a) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if a[mid] == target:
            return mid
        if a[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1

def main():
    arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    target = 7
    idx = binary_search(arr, target)
    if idx != -1:
        print("Элемент найден на позиции:", idx)
    else:
        print("Элемент не найден")

if __name__ == "__main__":
    main()

