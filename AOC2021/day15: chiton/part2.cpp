#include <bits/stdc++.h>
using namespace std;
#define INF 0x3f3f3f3f
typedef pair<int, int> pii;

int n, m, dx[] = {0, 0, 1, -1}, dy[] = {1, -1, 0, 0};
vector<vector<int>> mini, arr, dis;
deque<pii> q;
int add(int a, int b) {
    return a + b <= 9 ? a + b : a + b - 9;
}
void print_arr(){
    for (int i=0; i<arr.size(); i++){
        for (int j=0; j<arr[0].size(); j++) cout << arr[i][j];
        cout << '\n';
    }
}
int main() {
    freopen("input.txt", "r", stdin);
    freopen("part2.txt", "w", stdout);
    string t;
    while (cin >> t) {
        vector<int> cur;
        for (char c : t) cur.push_back(c - '0');
        mini.push_back(cur);
    }
    n = mini.size(), m = mini[0].size();
    arr.resize(n * 5, vector<int>(m * 5, 0));
    for (int i = 0; i < 5; i++) {
        for (int j = 0; j < 5; j++) {
            for (int x = 0; x < n; x++) {
                for (int y = 0; y < m; y++) {
                    arr[n * i + x][m * j + y] = add(mini[x][y], i + j);
                }
            }
        }
    }
    n *= 5;
    m *= 5;
    dis.resize(n, vector<int>(m, INF));
    dis[0][0] = 0;
    q.emplace_back(0, 0);
    while (!q.empty()) {
        int curx = q.front().first, cury = q.front().second;
        q.pop_front();
        for (int d = 0; d < 4; d++) {
            int nx = curx + dx[d], ny = cury + dy[d];
            if (nx < 0 || nx >= n || ny < 0 || ny >= m) continue;
            if (dis[nx][ny] > dis[curx][cury] + arr[nx][ny]) {
                dis[nx][ny] = dis[curx][cury] + arr[nx][ny];
                q.emplace_back(nx, ny);
            }
        }
    }
    cout << dis[n - 1][m - 1] << '\n';

    return 0;
}