#include <bits/stdc++.h>
using namespace std;

unordered_map<string, vector<string>> adj;
unordered_set<string> vis;
int ans = 0;
pair<string, string> split(string s, char c) {
    int i = s.find(c);
    return {s.substr(0, i), s.substr(i + 1)};
}
bool string_lower(string &a) {
    for (char c : a) {
        if (isupper(c)) return false;
    }
    return true;
}
void dfs(string cur) {
    if (cur == "end") {
        ans++;
        return;
    }
    bool all_lower = string_lower(cur);
    if (all_lower) vis.insert(cur);
    for (string &nxt : adj[cur]) {
        if (vis.find(nxt) == vis.end()) {
            dfs(nxt);
        }
    }
    if (all_lower) vis.erase(cur);
}
int main() {
    freopen("input.txt", "r", stdin);
    freopen("part1.txt", "w", stdout);
    string t;
    while (cin >> t) {
        auto [a, b] = split(t, '-');
        adj[a].push_back(b);
        adj[b].push_back(a);
    }
    dfs("start");
    cout << ans << endl;

    return 0;
}
