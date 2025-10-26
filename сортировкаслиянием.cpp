// merge_sort.cpp
// Компиляция/запуск: g++ -O2 merge_sort.cpp -o merge && ./merge
#include <bits/stdc++.h>
using namespace std;

// Слияние двух отсортированных массивов
vector<int> merge_two(const vector<int>& L, const vector<int>& R) {
    vector<int> res;
    res.reserve(L.size() + R.size());
    size_t i = 0, j = 0;
    while (i < L.size() && j < R.size()) {
        if (L[i] <= R[j]) res.push_back(L[i++]);
        else res.push_back(R[j++]);
    }
    while (i < L.size()) res.push_back(L[i++]);
    while (j < R.size()) res.push_back(R[j++]);
    return res;
}

// Merge Sort: O(n log n) время, O(n) память.
vector<int> merge_sort(const vector<int>& a) {
    if (a.size() <= 1) return a;
    size_t mid = a.size() / 2;
    vector<int> left(a.begin(), a.begin() + mid);
    vector<int> right(a.begin() + mid, a.end());
    left = merge_sort(left);
    right = merge_sort(right);
    return merge_two(left, right);
}

int main() {
    vector<int> arr{38, 27, 43, 3, 9, 82, 10};
    cout << "Исходный массив: ";
    for (int x : arr) cout << x << " ";
    cout << "\n";
    auto sorted_arr = merge_sort(arr);
    cout << "Отсортированный массив: ";
    for (int x : sorted_arr) cout << x << " ";
    cout << "\n";
    return 0;
}
