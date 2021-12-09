#include <bits/stdc++.h>
using namespace std;

vector<string> arr;
int dx[] = {0, 0, 1, -1}, dy[] = {1, -1, 0, 0};
int main() {
    freopen("input.txt", "r", stdin);
    freopen("part1.txt", "w", stdout);
    string t;
    while (cin >> t) {
        arr.push_back(t);
    }
    int n = arr.size(), m = arr[0].size(), ans = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            bool flag = true;
            for (int d = 0; d < 4; d++) {
                if (i + dx[d] < 0 || i + dx[d] >= n || j + dy[d] < 0 || j + dy[d] >= m) continue;
                if (arr[i][j] >= arr[i + dx[d]][j + dy[d]]) {
                    flag = false;
                    break;
                }
            }
            if (flag){
                ans += (arr[i][j] - '0') + 1;
            }
        }
    }
    cout << ans << endl;

    return 0;
}