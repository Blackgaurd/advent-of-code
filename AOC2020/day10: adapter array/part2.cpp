#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

vector<int> arr;
vector<ll> dp;
void solve(int cur){
    for (int nxt = cur + 1; nxt <= cur + 3; nxt++){
        if (arr[nxt] - arr[cur] <= 3 && nxt < arr.size()){
            if (dp[nxt] == 0){
                solve(nxt);
            }
            dp[cur] += dp[nxt];
        }
    }
}
int main() {
    freopen("input.txt", "r", stdin);
    freopen("part2.txt", "w", stdout);
    int x;
    while (cin >> x) {
        arr.push_back(x);
    }
    sort(arr.begin(), arr.end());
    dp.assign(arr.size(), 0);
    dp.back() = 1;

    solve(0);
    cout << dp[0] + dp[1] + dp[2] << '\n';
}