#include <bits/stdc++.h>
using namespace std;

vector<string> arr;
vector<vector<bool>> vis;
int n, m, dx[] = {0, 0, 1, -1}, dy[] = {1, -1, 0, 0};
int dfs(int x, int y) {
    vis[x][y] = true;
    int ret = 1;
    for (int d = 0; d < 4; d++) {
        if (x + dx[d] < 0 || x + dx[d] >= n || y + dy[d] < 0 || y + dy[d] >= m) continue;
        if (!vis[x + dx[d]][y + dy[d]] && arr[x + dx[d]][y + dy[d]] != '9') {
            ret += dfs(x + dx[d], y + dy[d]);
        }
    }
    return ret;
}
int main() {
    freopen("input.txt", "r", stdin);
    freopen("part2.txt", "w", stdout);
    string t;
    while (getline(cin, t)) {
        arr.push_back(t);
    }
    n = arr.size();
    m = arr[0].size();
    int ans = 0;
    vis.assign(n, vector<bool>(m, false));
    vector<int> basins;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (!vis[i][j] && arr[i][j] != '9') {
                basins.push_back(dfs(i, j));
            }
        }
    }
    sort(basins.begin(), basins.end(), greater<int>());
    cout << basins[0] * basins[1] * basins[2] << endl;

    return 0;
}