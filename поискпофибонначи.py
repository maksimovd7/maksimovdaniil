# fibonacci_search.py
# Запуск: python fibonacci_search.py

# Поиск Фибоначчи: O(log n) время. Требует отсортированный массив.
def fibonacci_search(a, x):
    n = len(a)
    # F(m) >= n
    fib_m2, fib_m1 = 0, 1
    fib_m = fib_m1 + fib_m2
    while fib_m < n:
        fib_m2, fib_m1 = fib_m1, fib_m
        fib_m = fib_m1 + fib_m2

    offset = -1
    while fib_m > 1:
        i = min(offset + fib_m2, n - 1)
        if a[i] < x:
            fib_m, fib_m1, fib_m2 = fib_m1, fib_m2, fib_m - fib_m1
            offset = i
        elif a[i] > x:
            fib_m, fib_m1, fib_m2 = fib_m2, fib_m1 - fib_m2, fib_m - (fib_m1 - fib_m2)
        else:
            return i
    if fib_m1 == 1 and offset + 1 < n and a[offset + 1] == x:
        return offset + 1
    return -1

def main():
    arr = [10, 22, 35, 40, 45, 50, 80, 82, 85, 90, 100]
    target = 85
    idx = fibonacci_search(arr, target)
    if idx != -1:
        print("Элемент найден на позиции:", idx)
    else:
        print("Элемент не найден")

if __name__ == "__main__":
    main()
