# shell_sort.py
# Запуск: python shell_sort.py

# Shell sort с простой последовательностью gap: n//2, n//4, ..., 1.
# Типичная сложность при делении на 2 — около O(n**1.5), память O(1).
def shell_sort(a):
    n = len(a)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = a[i]
            j = i
            # "вставки" в подмассив с шагом gap
            while j >= gap and a[j - gap] > temp:
                a[j] = a[j - gap]
                j -= gap
            a[j] = temp
        gap //= 2
    return a

def main():
    arr = [12, 34, 54, 2, 3]
    print("Исходный массив:", *arr)
    shell_sort(arr)
    print("Отсортированный массив:", *arr)

if __name__ == "__main__":
    main()


