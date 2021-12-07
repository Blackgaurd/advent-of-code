#include <bits/stdc++.h>
using namespace std;

string strip(string s, char c = ' ') {
    int i = 0;
    while (i < s.size() && s[i] == c) i++;
    int j = s.size() - 1;
    while (j >= 0 && s[j] == c) j--;
    return s.substr(i, j - i + 1);
}
string strip_right(string s, char c = ' ') {
    int j = s.size() - 1;
    while (j >= 0 && s[j] == c) j--;
    return s.substr(0, j + 1);
}
vector<string> split(string s, string delimiter) {
    size_t pos_start = 0, pos_end, delim_len = delimiter.length();
    string token;
    vector<string> res;

    while ((pos_end = s.find(delimiter, pos_start)) != string::npos) {
        token = s.substr(pos_start, pos_end - pos_start);
        pos_start = pos_end + delim_len;
        res.push_back(strip(token));
    }

    res.push_back(strip(s.substr(pos_start)));
    return res;
}
vector<string> split(string s, char delimiter) {
    return split(s, string(1, delimiter));
}
vector<string> split(string s, char delimiter, int n) {
    vector<string> res;
    for (int i = 0; i < n; i++) {
        int pos = s.find(delimiter);
        if (pos == string::npos) {
            res.push_back(s);
            return res;
        }
        res.push_back(s.substr(0, pos));
        s = s.substr(pos + 1);
    }
    res.push_back(s);
    return res;
}
unordered_map<string, vector<string>> adj;
unordered_set<string> vis;
int main() {
    freopen("input.txt", "r", stdin);
    freopen("part1.txt", "w", stdout);

    // input parsing
    string s;
    while (getline(cin, s)) {
        s = strip(s, '.');
        vector<string> tmp = split(s, "contain");
        string start = tmp[0].substr(0, tmp[0].size() - 5);
        if (tmp[1] == "no other bags") continue;
        vector<string> inner = split(tmp[1], ",");
        for (string &bag : inner) {
            tmp = split(bag, ' ', 1);
            string color = strip_right(tmp[1], 's');
            color = color.substr(0, color.size() - 4);
            adj[color].push_back(start);
        }
    }

    // bfs
    deque<string> q = {"shiny gold"};
    vis.insert("shiny gold");
    while (!q.empty()){
        string &cur = q.front();
        for (string nxt: adj[cur]){
            if (vis.find(nxt) == vis.end()){
                vis.insert(nxt);
                q.push_back(nxt);
            }
        }
        q.pop_front();
    }

    cout << vis.size() - 1 << '\n'; // subtract 1 for shiny gold

    return 0;
}