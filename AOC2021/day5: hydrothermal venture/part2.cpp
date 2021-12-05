// python screwed me up, so I'm using cpp

#include <bits/stdc++.h>
using namespace std;
#define endl '\n'

string strip(string s) {
    while (s.back() == ' ') {
        s.pop_back();
    }
    int i = 0;
    while (s[i] == ' ') {
        i++;
    }
    s.erase(0, i);
    return s;
}
vector<string> split(string s, string deliminator) {
    vector<string> result;
    size_t pos = 0;
    string token;
    while ((pos = s.find(deliminator)) != string::npos) {
        token = s.substr(0, pos);
        result.push_back(strip(token));
        s.erase(0, pos + deliminator.length());
    }
    result.push_back(strip(s));
    return result;
}
struct line {
    int x1, y1, x2, y2;
    line(string unparsed) {
        vector<string> coords = split(unparsed, "->");
        vector<string> p1 = split(coords[0], ",");
        vector<string> p2 = split(coords[1], ",");
        x1 = stoi(p1[0]);
        y1 = stoi(p1[1]);
        x2 = stoi(p2[0]);
        y2 = stoi(p2[1]);
        if (x1 > x2) {
            swap(x1, x2);
            swap(y1, y2);
        } else if (x1 == x2 && y1 > y2) {
            swap(y1, y2);
        }
    }
};
const int MM = 1000;
int arr[MM][MM];
void print(bool flag) {
    int ans = 0;
    for (int i = 0; i < MM; i++) {
        for (int j = 0; j < MM; j++) {
            if (arr[j][i] >= 2) ans++;
            if (flag) {
                if (arr[j][i] == 0)
                    cout << ".";
                else
                    cout << arr[j][i];
            }
        }
        if (flag) cout << endl;
    }
    cout << ans << endl;
}
int main() {
    freopen("input.txt", "r", stdin);
    freopen("c++out.txt", "w", stdout);

    string t;
    while (getline(cin, t)) {
        line cur = line(t);
        if (cur.x1 == cur.x2) {
            for (int i = cur.y1; i <= cur.y2; i++) {
                arr[cur.x1][i]++;
            }
        } else if (cur.y1 == cur.y2) {
            for (int i = cur.x1; i <= cur.x2; i++) {
                arr[i][cur.y1]++;
            }
        } else if (cur.y1 < cur.y2) {
            for (int x = cur.x1, y = cur.y1; x <= cur.x2; x++, y++) {
                arr[x][y]++;
            }
        } else {
            for (int x = cur.x1, y = cur.y1; x <= cur.x2; x++, y--) {
                arr[x][y]++;
            }
        }
    }
    print(true);
}