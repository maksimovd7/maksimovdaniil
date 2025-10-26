# linear_search.py
# Запуск: python linear_search.py

# Линейный поиск: O(n) время, O(1) память. Работает на неотсортированных массивах.
def linear_search(a, target):
    for i, v in enumerate(a):
        if v == target:
            return i
    return -1

def main():
    arr = [3, 5, 2, 7, 9, 1, 4]
    target = 7
    idx = linear_search(arr, target)
    if idx != -1:
        print("Элемент найден на позиции:", idx)
    else:
        print("Элемент не найден")

if __name__ == "__main__":
    main()


