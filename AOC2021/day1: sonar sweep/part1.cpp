#include <bits/stdc++.h>
using namespace std;

int main(){
    freopen("input.txt", "r", stdin);
    freopen("part1.txt", "w", stdout);
    int cnt, pre, cur;
    cin >> pre;
    while (cin >> cur){
        if (cur > pre){
            cnt++;
        }
        pre = cur;
    }
    cout << cnt << '\n';
}