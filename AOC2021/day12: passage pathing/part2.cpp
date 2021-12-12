#include <bits/stdc++.h>
using namespace std;

unordered_map<string, vector<string>> adj;
unordered_map<string, int> vis;
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
void dfs(string cur, bool vis_twice) {
    if (cur == "end") {
        ans++;
        return;
    }
    bool all_lower = string_lower(cur);
    if (all_lower) vis[cur]++;
    for (string &nxt : adj[cur]) {
        if (vis[nxt] == 0) {
            dfs(nxt, vis_twice);
        } else if (vis[nxt] == 1 && !vis_twice && nxt != "start") {
            dfs(nxt, true);
        }
    }
    if (all_lower) vis[cur]--;
}
int main() {
    freopen("input.txt", "r", stdin);
    freopen("part2.txt", "w", stdout);
    string t;
    while (cin >> t) {
        auto [a, b] = split(t, '-');
        adj[a].push_back(b);
        adj[b].push_back(a);
        vis[a] = vis[b] = 0;
    }
    dfs("start", false);
    cout << ans << endl;

    return 0;
}
