// heap_sort.cpp
// Компиляция/запуск: g++ -O2 heap_sort.cpp -o heap && ./heap
#include <bits/stdc++.h>
using namespace std;

void heapify(vector<int>& a, int n, int i) {
    int largest = i;
    int L = 2*i + 1;
    int R = 2*i + 2;
    if (L < n && a[L] > a[largest]) largest = L;
    if (R < n && a[R] > a[largest]) largest = R;
    if (largest != i) {
        swap(a[i], a[largest]);
        heapify(a, n, largest);
    }
}

// Heap sort: всегда O(n log n) время, O(1) память.
void heap_sort(vector<int>& a) {
    int n = (int)a.size();
    for (int i = n/2 - 1; i >= 0; --i) heapify(a, n, i);
    for (int end = n - 1; end > 0; --end) {
        swap(a[0], a[end]);
        heapify(a, end, 0);
    }
}

int main() {
    vector<int> arr{12, 11, 13, 5, 6, 7};
    cout << "Исходный массив: ";
    for (int x : arr) cout << x << " ";
    cout << "\n";
    heap_sort(arr);
    cout << "Отсортированный массив: ";
    for (int x : arr) cout << x << " ";
    cout << "\n";
    return 0;
}

