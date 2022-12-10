#include <fstream>
#include <iostream>
#include <string>
using namespace std;

int stops[] = {20, 60, 100, 140, 180, 220, 100000};
int *iter = stops;
int X = 1, cycles = 0, ans = 0;
void add_cycle(int inc) {
    cycles++;
    if (cycles == *iter) {
        iter++;
        ans += X * cycles;
    }
    X += inc;
}
int main() {
    ifstream f("day9/input.txt");

    string line;
    while (getline(f, line)) {
        if (line[0] == 'a') {
            int inc = stoi(line.substr(5, line.size() - 1));
            add_cycle(0);
            add_cycle(inc);
        } else {
            add_cycle(0);
        }
    }
    cout << ans << endl;

    f.close();
}