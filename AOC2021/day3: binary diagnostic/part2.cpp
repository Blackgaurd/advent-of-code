#include <bits/stdc++.h>
using namespace std;

// all 1000 numbers are different
#ifdef TEST
const int LEN = 5;
#else
const int LEN = 12;
#endif
unordered_set<int> o2_nums, co2_nums;
string t;
int solve(unordered_set<int> &cur, int bit) {
    for (int i = 0; i < LEN; i++) {
        int cnt = 0;
        for (auto it = cur.begin(); it != cur.end(); it++) {
            cnt += ((*it >> (LEN - i - 1)) & 1 ? 1 : -1);
        }
        int uncommon = (cnt >= 0 ? bit : !bit);
        vector<int> to_erase;
        for (auto it = cur.begin(); it != cur.end(); it++) {
            if (((*it >> (LEN - i - 1)) & 1) == uncommon) {
                to_erase.push_back(*it);
            }
        }
        for (int i : to_erase) cur.erase(i);
        if (cur.size() == 1) {
            return *cur.begin();
        }
    }
    return -1;
}
int main() {
#ifdef TEST
    freopen("test.txt", "r", stdin);
#else
    freopen("input.txt", "r", stdin);
#endif
    freopen("part2.txt", "w", stdout);
    while (cin >> t) {
        o2_nums.insert(stoi(t, 0, 2));
        co2_nums.insert(stoi(t, 0, 2));
    }
    // find oxygen
    // remove numbers that are uncommon
    // if equal remove numbers with 0 as bit
    int o2 = solve(o2_nums, 0);

    // find carbon dioxide
    int co2 = solve(co2_nums, 1);

    cout << o2 * co2 << '\n';

    return 0;
}