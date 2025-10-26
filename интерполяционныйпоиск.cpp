// interpolation_search.cpp
// Компиляция/запуск: g++ -O2 interpolation_search.cpp -o isearch && ./isearch
#include <bits/stdc++.h>
using namespace std;

// Интерполяционный поиск: лучшее ~ O(log log n) при равномерных данных, худшее O(n).
int interpolation_search(const vector<int>& a, int x) {
    int lo = 0, hi = (int)a.size() - 1;
    while (lo <= hi && x >= a[lo] && x <= a[hi]) {
        if (a[hi] == a[lo]) return (a[lo] == x) ? lo : -1;
        // оценка позиции по интерполяции
        long long pos = lo + (long long)(hi - lo) * (x - a[lo]) / (a[hi] - a[lo]);
        if (a[pos] == x) return (int)pos;
        if (a[pos] < x) lo = (int)pos + 1;
        else hi = (int)pos - 1;
    }
    return -1;
}

int main() {
    vector<int> arr{1,3,5,7,9,11,13,15,17,19};
    int x = 15;
    int idx = interpolation_search(arr, x);
    if (idx != -1) cout << "Элемент найден на позиции: " << idx << "\n";
    else cout << "Элемент не найден\n";
    return 0;
}
