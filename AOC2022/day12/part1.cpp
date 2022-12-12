#include <stdio.h>

#include <deque>
#include <fstream>
#include <iostream>
#include <string>
#include <utility>
#include <vector>
using namespace std;

typedef pair<int, int> pii;

vector<vector<char>> grid;
vector<pii> d4 = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
int main() {
    ifstream f("day12/input.txt");

    string line;
    while (getline(f, line)) {
        vector<char> row = {125};
        for (char c : line) {
            row.push_back(c);
        }
        row.push_back(125);
        grid.push_back(row);
    }
    vector<char> pad(grid[0].size(), 125);
    grid.insert(grid.begin(), pad);
    grid.push_back(pad);

    int n = grid.size(), m = grid[0].size();
    int sx, sy, ex, ey;
    for (int i = 1; i < n; i++) {
        for (int j = 1; j < m; j++) {
            if (grid[i][j] == 'a') {
                sx = i;
                sy = j;
                grid[i][j] = 'a';
            } else if (grid[i][j] == 'E') {
                ex = i;
                ey = j;
                grid[i][j] = 'z';
            }
        }
    }

    deque<pii> q = {{sx, sy}};
    vector<vector<int>> dis(n, vector<int>(m, 1e9));
    dis[sx][sy] = 0;
    while (!q.empty()) {
        auto [cx, cy] = q.front();
        for (auto [dx, dy] : d4) {
            int nx = cx + dx, ny = cy + dy;
            if (grid[nx][ny] <= grid[cx][cy] + 1) {
                if (dis[nx][ny] != 1e9) continue;
                dis[nx][ny] = dis[cx][cy] + 1;
                q.push_back({nx, ny});
            }
        }
        q.pop_front();
    }

    cout << dis[ex][ey] << '\n';

    f.close();
}