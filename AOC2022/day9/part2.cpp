#include <math.h>

#include <fstream>
#include <iostream>
#include <string>
using namespace std;

int stops[] = {20, 60, 100, 140, 180, 220, 100000};
int *iter = stops;
int X = 1, cycles = 0;
char grid[6 * 40];
int grid_pos = 0;
void add_cycle(int inc) {
    cycles++;
    if (cycles == *iter) {
        iter++;
    }
    if (abs(grid_pos % 40 - X) <= 1) {
        grid[grid_pos] = '#';
    } else {
        grid[grid_pos] = ' ';  // easier to see letters
    }
    grid_pos++;
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

    for (int i = 0; i < 6; i++) {
        for (int j = 0; j < 40; j++) {
            cout << grid[i * 40 + j];
        }
        cout << '\n';
    }

    f.close();
}