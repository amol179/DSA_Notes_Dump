/*
ID: amolgur1
LANG: C++11
TASK: clocks
*/

#include <bits/stdc++.h>
using namespace std;

// Moves and their affected indices (0..8)
static const int moves[9][9] = {
    {0,1,3,4,-1,-1,-1,-1,-1},    // 1: ABDE
    {0,1,2,-1,-1,-1,-1,-1,-1},   // 2: ABC
    {1,2,4,5,-1,-1,-1,-1,-1},    // 3: BCEF
    {0,3,6,-1,-1,-1,-1,-1,-1},   // 4: ADG
    {1,3,4,5,7,-1,-1,-1,-1},     // 5: BDEFH
    {2,5,8,-1,-1,-1,-1,-1,-1},   // 6: CFI
    {3,4,6,7,-1,-1,-1,-1,-1},    // 7: DEGH
    {6,7,8,-1,-1,-1,-1,-1,-1},   // 8: GHI
    {4,5,7,8,-1,-1,-1,-1,-1}     // 9: EFHI
};

// Apply move m (0-based) k times (k in 0..3) to state
static inline array<int,9> apply_move(const array<int,9> &state, int m, int k) {
    array<int,9> res = state;
    for (int t = 0; t < k; ++t) {
        for (int i = 0; i < 9; ++i) {
            int idx = moves[m][i];
            if (idx == -1) break;
            res[idx] = (res[idx] + 1) % 4; // 0,1,2,3 represent 12,3,6,9; +1 is +3 hours
        }
    }
    return res;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    freopen("clocks.in", "r", stdin);
    freopen("clocks.out", "w", stdout);

    array<int,9> start{};
    for (int i = 0; i < 9; ++i) {
        int v; if (!(cin >> v)) return 0; // handle empty input
        // Map 12->0, 3->1, 6->2, 9->3
        int rem = (v % 12) / 3; // 12%12=0 =>0; 3->1;6->2;9->3
        start[i] = rem;
    }

    const array<int,9> goal{}; // all zeros

    // brute-force over 4^9 combinations; order by lexicographic move list (lowest concat)
    array<int,9> best_counts{};
    bool found = false;

    for (int m1 = 0; m1 < 4; ++m1)
    for (int m2 = 0; m2 < 4; ++m2)
    for (int m3 = 0; m3 < 4; ++m3)
    for (int m4 = 0; m4 < 4; ++m4)
    for (int m5 = 0; m5 < 4; ++m5)
    for (int m6 = 0; m6 < 4; ++m6)
    for (int m7 = 0; m7 < 4; ++m7)
    for (int m8 = 0; m8 < 4; ++m8)
    for (int m9 = 0; m9 < 4; ++m9) {
        array<int,9> st = start;
        int counts[9] = {m1,m2,m3,m4,m5,m6,m7,m8,m9};
        for (int m = 0; m < 9; ++m) {
            st = apply_move(st, m, counts[m]);
        }
        if (st == goal) {
            best_counts = {m1,m2,m3,m4,m5,m6,m7,m8,m9};
            found = true;
            // Because loops are lexicographic increasing, first found is lexicographically smallest
            goto OUTPUT;
        }
    }

OUTPUT:
    if (!found) return 0; // should not happen per problem constraints

    bool first = true;
    for (int m = 0; m < 9; ++m) {
        for (int k = 0; k < best_counts[m]; ++k) {
            if (!first) cout << ' ';
            first = false;
            cout << (m + 1);
        }
    }
    cout << '\n';
    return 0;
}
