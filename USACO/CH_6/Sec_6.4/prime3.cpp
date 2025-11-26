/*
ID: amolgur1
TASK: prime3
LANG: C++
*/
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cstring>

using namespace std;

struct Prime {
    int val;
    int d[5];
};

int SUM, CORNER;
bool is_prime_lut[100000];
vector<Prime> primes;

// Buckets for rapid access:
// [first_digit][last_digit]
vector<int> p_by_ends[10][10]; 
// [first_digit][last_digit][middle_digit] (Used for Col 4 optimization)
vector<int> p_by_ends_mid[10][10][10]; 

// Pruning Tables:
// pat1[d0][d1][d3]: Is there a prime with digits d0, d1, d3 at pos 0,1,3?
bool pat1[10][10][10];
// pat2[d0][d2]: Is there a prime with digits d0, d2 at pos 0,2?
bool pat2[10][10];
// pat3[d0][d2][d4]: Is there a prime with digits d0, d2, d4 at pos 0,2,4?
bool pat3[10][10][10];

int g[5][5];
vector<string> solutions;

void init() {
    memset(is_prime_lut, 0, sizeof(is_prime_lut));
    memset(pat1, 0, sizeof(pat1));
    memset(pat2, 0, sizeof(pat2));
    memset(pat3, 0, sizeof(pat3));

    for (int i = 10000; i < 100000; i++) {
        // Primality check
        bool p = true;
        for (int k = 2; k * k <= i; k++) {
            if (i % k == 0) { p = false; break; }
        }
        if (!p) continue;

        // Digit sum check
        int s = 0, t = i;
        int d[5];
        for (int k = 4; k >= 0; k--) {
            d[k] = t % 10;
            s += d[k];
            t /= 10;
        }
        
        if (s != SUM) continue;

        // Store valid prime
        is_prime_lut[i] = true;
        Prime P; P.val = i;
        for(int k=0; k<5; k++) P.d[k] = d[k];
        primes.push_back(P);

        int d0 = d[0], d1 = d[1], d2 = d[2], d3 = d[3], d4 = d[4];

        // Populate Buckets
        p_by_ends[d0][d4].push_back(primes.size() - 1);
        p_by_ends_mid[d0][d4][d2].push_back(primes.size() - 1);

        // Populate Pruning Tables
        pat1[d0][d1][d3] = true;
        pat2[d0][d2] = true;
        pat3[d0][d2][d4] = true;
    }
}

void solve() {
    // 1. Main Diagonal (0,0) -> (4,4)
    for (size_t i1 = 0; i1 < primes.size(); i1++) {
        const Prime& D1 = primes[i1];
        if (D1.d[0] != CORNER) continue;
        for(int k=0; k<5; k++) g[k][k] = D1.d[k];

        // 2. Anti Diagonal (4,0) -> (0,4)
        for (size_t i2 = 0; i2 < primes.size(); i2++) {
            const Prime& D2 = primes[i2];
            if (D2.d[2] != g[2][2]) continue; // Center must overlap
            for(int k=0; k<5; k++) g[4-k][k] = D2.d[k]; // Correct filling direction

            // 3. Row 0
            const vector<int>& r0_list = p_by_ends[g[0][0]][g[0][4]];
            for (int idx_r0 : r0_list) {
                const Prime& R0 = primes[idx_r0];
                g[0][1] = R0.d[1]; g[0][2] = R0.d[2]; g[0][3] = R0.d[3];

                // Pruning: Check partial columns
                // Col 1 potential: g[0][1], g[1][1], g[3][1]
                if (!pat1[g[0][1]][g[1][1]][g[3][1]]) continue;
                // Col 2 potential: g[0][2], g[2][2]
                if (!pat2[g[0][2]][g[2][2]]) continue;
                // Col 3 potential: g[0][3], g[1][3], g[3][3]
                if (!pat1[g[0][3]][g[1][3]][g[3][3]]) continue;

                // 4. Row 4
                const vector<int>& r4_list = p_by_ends[g[4][0]][g[4][4]];
                for (int idx_r4 : r4_list) {
                    const Prime& R4 = primes[idx_r4];
                    g[4][1] = R4.d[1]; g[4][2] = R4.d[2]; g[4][3] = R4.d[3];

                    // Optimization: Solve Col 1 mid (2,1) immediately
                    int sum_c1 = g[0][1] + g[1][1] + g[3][1] + g[4][1];
                    int mid_c1 = SUM - sum_c1;
                    if (mid_c1 < 0 || mid_c1 > 9) continue;
                    g[2][1] = mid_c1;
                    int val_c1 = g[0][1]*10000 + g[1][1]*1000 + g[2][1]*100 + g[3][1]*10 + g[4][1];
                    if (!is_prime_lut[val_c1]) continue;

                    // Optimization: Solve Col 3 mid (2,3) immediately
                    int sum_c3 = g[0][3] + g[1][3] + g[3][3] + g[4][3];
                    int mid_c3 = SUM - sum_c3;
                    if (mid_c3 < 0 || mid_c3 > 9) continue;
                    g[2][3] = mid_c3;
                    int val_c3 = g[0][3]*10000 + g[1][3]*1000 + g[2][3]*100 + g[3][3]*10 + g[4][3];
                    if (!is_prime_lut[val_c3]) continue;

                    // Check Col 2 potential with new R4 data: g[0][2], g[2][2], g[4][2]
                    if (!pat3[g[0][2]][g[2][2]][g[4][2]]) continue;

                    // 5. Col 0
                    const vector<int>& c0_list = p_by_ends[g[0][0]][g[4][0]];
                    for (int idx_c0 : c0_list) {
                        const Prime& C0 = primes[idx_c0];
                        g[1][0] = C0.d[1]; g[2][0] = C0.d[2]; g[3][0] = C0.d[3];

                        // Calculate required g[2][4] from Row 2 sum
                        int sum_r2_partial = g[2][0] + g[2][1] + g[2][2] + g[2][3];
                        int req_24 = SUM - sum_r2_partial;
                        if (req_24 < 0 || req_24 > 9) continue;
                        g[2][4] = req_24;

                        // 6. Col 4 (Filtered by middle digit)
                        const vector<int>& c4_list = p_by_ends_mid[g[0][4]][g[4][4]][g[2][4]];
                        for (int idx_c4 : c4_list) {
                            const Prime& C4 = primes[idx_c4];
                            g[1][4] = C4.d[1]; g[3][4] = C4.d[3]; // g[2][4] is already set/checked

                            // Verify Row 2 (Full)
                            int val_r2 = g[2][0]*10000 + g[2][1]*1000 + g[2][2]*100 + g[2][3]*10 + g[2][4];
                            if (!is_prime_lut[val_r2]) continue;

                            // Solve Row 1 mid (1,2)
                            int sum_r1 = g[1][0] + g[1][1] + g[1][3] + g[1][4];
                            int mid_r1 = SUM - sum_r1;
                            if (mid_r1 < 0 || mid_r1 > 9) continue;
                            g[1][2] = mid_r1;
                            int val_r1 = g[1][0]*10000 + g[1][1]*1000 + g[1][2]*100 + g[1][3]*10 + g[1][4];
                            if (!is_prime_lut[val_r1]) continue;

                            // Solve Row 3 mid (3,2)
                            int sum_r3 = g[3][0] + g[3][1] + g[3][3] + g[3][4];
                            int mid_r3 = SUM - sum_r3;
                            if (mid_r3 < 0 || mid_r3 > 9) continue;
                            g[3][2] = mid_r3;
                            int val_r3 = g[3][0]*10000 + g[3][1]*1000 + g[3][2]*100 + g[3][3]*10 + g[3][4];
                            if (!is_prime_lut[val_r3]) continue;

                            // Verify Col 2 (Full)
                            int val_c2 = g[0][2]*10000 + g[1][2]*1000 + g[2][2]*100 + g[3][2]*10 + g[4][2];
                            if (!is_prime_lut[val_c2]) continue;

                            // Solution found
                            string s = "";
                            for(int r=0; r<5; r++) {
                                for(int c=0; c<5; c++) s += to_string(g[r][c]);
                                if(r!=4) s += "\n";
                            }
                            solutions.push_back(s);
                        }
                    }
                }
            }
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    if (fopen("prime3.in", "r")) {
        freopen("prime3.in", "r", stdin);
        freopen("prime3.out", "w", stdout);
    }

    cin >> SUM >> CORNER;

    init();

    if (primes.empty()) {
        cout << "NONE" << endl;
        return 0;
    }

    solve();

    if (solutions.empty()) {
        cout << "NONE" << endl;
    } else {
        sort(solutions.begin(), solutions.end());
        for (size_t i = 0; i < solutions.size(); i++) {
            cout << solutions[i] << endl;
            if (i < solutions.size() - 1) cout << endl;
        }
    }

    return 0;
}