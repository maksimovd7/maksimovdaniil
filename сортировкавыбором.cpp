// selection_sort.cpp
// Компиляция/запуск: g++ -O2 selection_sort.cpp -o sel && ./sel
#include <bits/stdc++.h>
using namespace std;

// Сортировка выбором: O(n^2) по времени, O(1) по памяти.
void selection_sort(vector<int>& a) {
    int n = (int)a.size();
    for (int i = 0; i < n; ++i) {
        int min_idx = i; // предполагаем, что текущий — минимум
        for (int j = i + 1; j < n; ++j) {
            if (a[j] < a[min_idx]) min_idx = j; // ищем минимум справа
        }
        swap(a[i], a[min_idx]); // ставим найденный минимум на позицию i
    }
}

int main() {
    vector<int> arr{64, 25, 12, 22, 11};
    cout << "Исходный массив: ";
    for (int x : arr) cout << x << " ";
    cout << "\n";
    selection_sort(arr);
    cout << "Отсортированный массив: ";
    for (int x : arr) cout << x << " ";
    cout << "\n";
    return 0;
}
