#include <bits/stdc++.h>
using namespace std;

vector<int> split(string s, char delim) {
    vector<int> res;
    stringstream ss(s);
    string item;
    while (getline(ss, item, delim)) {
        res.push_back(stoi(item));
    }
    return res;
}
int check(const vector<int> &arr, int pos) {
    int ret = 0;
    for (int i: arr){
        int n = abs(i - pos);
        ret += n * (n + 1) / 2;
    }
    return ret;
}
int main() {
    freopen("input.txt", "r", stdin);
    freopen("part2.txt", "w", stdout);
    string s;
    cin >> s;
    vector<int> arr = split(s, ',');
    int lo = INT_MAX, hi = INT_MIN, ans = INT_MAX, ans_pos = -1;
    for (int i : arr) {
        lo = min(lo, i);
        hi = max(hi, i);
    }
    while (lo <= hi) {
        int mid = (lo + hi) / 2;
        int left = check(arr, mid), right = check(arr, mid + 1);
        ans = min({ans, left, right});
        if (left < right) {
            hi = mid - 1;
        } else if (left > right) {
            lo = mid + 2;
        } else
            break;
    }
    cout << ans << '\n';
    return 0;
}