# quick_sort.py
# Запуск: python quick_sort.py

# Быстрая сортировка (Lomuto partition): среднее O(n log n), худшее O(n^2).
def partition(a, lo, hi):
    pivot = a[hi]
    i = lo
    for j in range(lo, hi):
        if a[j] <= pivot:
            a[i], a[j] = a[j], a[i]
            i += 1
    a[i], a[hi] = a[hi], a[i]
    return i

def quick_sort(a, lo=0, hi=None):
    if hi is None:
        hi = len(a) - 1
    if lo < hi:
        p = partition(a, lo, hi)
        quick_sort(a, lo, p - 1)
        quick_sort(a, p + 1, hi)
    return a

def main():
    arr = [10, 7, 8, 9, 1, 5]
    print("Исходный массив:")
    print(*arr)
    quick_sort(arr)
    print("Отсортированный массив:")
    print(*arr)

if __name__ == "__main__":
    main()


