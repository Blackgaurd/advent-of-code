#include <bits/stdc++.h>
using namespace std;
#define INF 0x3f3f3f3f
typedef pair<int, int> pii;

int n, m, dx[] = {0, 0, 1, -1}, dy[] = {1, -1, 0, 0};
vector<vector<int>> arr, dis;
deque<pii> q;
int main(){
    freopen("input.txt", "r", stdin);
    freopen("part1.txt", "w", stdout);
    string t;
    while (cin >> t){
        vector<int> cur;
        for (char c : t) cur.push_back(c - '0');
        arr.push_back(cur);
    }
    n = arr.size(), m = arr[0].size();
    dis.resize(n, vector<int>(m, INF));
    dis[0][0] = 0;
    q.emplace_back(0, 0);
    while (!q.empty()){
        int curx = q.front().first, cury = q.front().second;
        q.pop_front();
        for (int d=0; d<4; d++){
            int nx = curx + dx[d], ny = cury + dy[d];
            if (nx < 0 || nx >= n || ny < 0 || ny >= m) continue;
            if (dis[nx][ny] > dis[curx][cury] + arr[nx][ny]){
                dis[nx][ny] = dis[curx][cury] + arr[nx][ny];
                q.emplace_back(nx, ny);
            }
        }
    }
    cout << dis[n-1][m-1] << '\n';

    return 0;
}