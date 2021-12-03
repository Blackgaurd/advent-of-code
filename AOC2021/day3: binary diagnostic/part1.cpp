#include <bits/stdc++.h>
using namespace std;

const int LEN = 12;
int cnt[LEN], gma, eps;
string t;
int main() {
    freopen("input.txt", "r", stdin);
    freopen("part1.txt", "w", stdout);
    while (cin >> t) {
        for (int i = 0; i < t.size(); i++) {
            cnt[i] += (t[i] == '1' ? 1 : -1);
        }
    }
    for (int i = 0; i < LEN; i++) {
        gma |= ((cnt[i] > 0) << (LEN - i - 1));
        eps |= ((cnt[i] < 0) << (LEN - i - 1));
    }
    cout << gma * eps << endl;

    return 0;
}