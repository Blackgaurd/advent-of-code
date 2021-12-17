#include <algorithm>
#include <climits>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

struct range {
    int l, r;
    bool contains(int x) {
        return min(l, r) <= x && x <= max(l, r);
    }
} x, y;
vector<string> split(string t, string delim) {
    vector<string> res;
    size_t pos = 0;
    string token;
    while ((pos = t.find(delim)) != string::npos) {
        token = t.substr(0, pos);
        res.push_back(token);
        t.erase(0, pos + delim.length());
    }
    res.push_back(t);
    return res;
}
void read(int &x) {
    char c;
    bool sign = false;
    for (; !isdigit(c = getchar());) {
        if (c == '-') sign = true;
    }
    do {
        x = x * 10 + c - '0';
    } while (isdigit(c = getchar()));
    if (sign) x = -x;
}
int fn(int n) {
    return n * (n + 1) / 2;
}
bool check(int vel_x, int vel_y) {
    int pos_x = 0, pos_y = 0;
    while (pos_y > y.l) {
        pos_x += max(vel_x--, 0);
        pos_y += vel_y--;
        if (x.contains(pos_x) && y.contains(pos_y)) return true;
    }
    pos_x += max(vel_x--, 0);
    pos_y += vel_y--;
    return (x.contains(pos_x) && y.contains(pos_y));
}
int main() {
    freopen("input.txt", "r", stdin);
    freopen("part1.txt", "w", stdout);
    read(x.l);
    read(x.r);
    read(y.l);
    read(y.r);
    // find possible x velocity
    int x_min = INT_MAX, x_max = 1;
    for (; fn(x_max) <= x.r; x_max++) {
        if (x.contains(fn(x_max))) {
            x_min = min(x_min, x_max);
        }
    }
    // find max y for each posible x
    int y_max = 0;
    for (int cur = x_min; cur <= x_max; cur++) {
        int y_velocity;
        for (y_velocity = 1; y_velocity < 100; y_velocity++) {
            if (check(cur, y_velocity)) {
                y_max = max(y_max, y_velocity);
            }
        }
    }
    cout << fn(y_max) << endl;
}