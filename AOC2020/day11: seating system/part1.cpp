#include <bits/stdc++.h>
using namespace std;

vector<string> arr;
int n, m, dx[8] = {-1, -1, -1, 0, 0, 1, 1, 1}, dy[8] = {-1, 0, 1, -1, 1, -1, 0, 1};
pair<vector<string>, int> flip() {
    vector<string> flipped = arr;
    int changed = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (arr[i][j] == '.') continue;
            int cnt = 0;
            for (int d = 0; d < 8; d++) {
                int x = i + dx[d], y = j + dy[d];
                if (x < 0 || x >= n || y < 0 || y >= m) continue;
                if (arr[x][y] == '#') cnt++;
            }
            if (arr[i][j] == 'L' && cnt == 0) {
                flipped[i][j] = '#';
                changed++;
            } else if (arr[i][j] == '#' && cnt >= 4) {
                flipped[i][j] = 'L';
                changed++;
            }
        }
    }
    return {flipped, changed};
}
int main() {
    freopen("input.txt", "r", stdin);
    freopen("part1.txt", "w", stdout);

    string t;
    while (cin >> t) {
        arr.push_back(t);
    }
    n = arr.size();
    m = arr[0].size();
    while (true){
        auto [flipped, changed] = flip();
        if (changed == 0) break;
        arr = flipped;
    }
    int ans = 0;
    for (int i=0; i<n; i++)
        for (int j=0; j<m; j++)
            ans += (arr[i][j] == '#');

    cout << ans << endl;

    return 0;
}
