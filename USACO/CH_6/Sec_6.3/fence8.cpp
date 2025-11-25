/*
ID: amolgur1
TASK: fence8
LANG: C++
*/
#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <numeric>

using namespace std;

int N, R;
vector<int> boards;
vector<int> rails;
vector<int> prefix_sum_rails; // Prefix sum of sorted rails
int total_board_capacity = 0;

// DFS to check if we can fit rails[rail_idx...0] into the boards
// rail_idx: index of the rail we are trying to cut (starts from k-1 down to 0)
// start_board_idx: optimization to skip boards for duplicate rails
// current_waste: total space wasted in boards so far
bool dfs(int rail_idx, int start_board_idx, int current_waste) {
    // Base case: all rails placed
    if (rail_idx < 0) return true;

    // Pruning: Waste Check
    // If the total capacity minus waste is strictly less than the sum of rails we still need to fit,
    // we can never succeed.
    // sum of rails[0...rail_idx] is prefix_sum_rails[rail_idx + 1]
    if (total_board_capacity - current_waste < prefix_sum_rails[rail_idx + 1]) {
        return false;
    }

    bool found_path = false;

    // Try to place current rail in each board
    for (int i = start_board_idx; i < N; ++i) {
        // Skip identical board states if the previous one failed
        if (i > start_board_idx && boards[i] == boards[i-1]) continue;

        if (boards[i] >= rails[rail_idx]) {
            boards[i] -= rails[rail_idx];

            // Calculate new waste if this board becomes effectively useless
            // A board is useless if its remaining space is smaller than the smallest rail requested (rails[0])
            int waste_delta = 0;
            if (boards[i] < rails[0]) {
                waste_delta = boards[i];
            }

            // Next rail to process
            // Optimization: if the next rail (rail_idx - 1) is the same size as this one,
            // we can start searching from the current board 'i' to avoid permutations.
            // Otherwise reset start index to 0.
            int next_start = 0;
            if (rail_idx > 0 && rails[rail_idx - 1] == rails[rail_idx]) {
                next_start = i;
            }

            if (dfs(rail_idx - 1, next_start, current_waste + waste_delta)) {
                found_path = true;
            }

            // Backtrack
            boards[i] += rails[rail_idx];

            if (found_path) return true;
            
            // Pruning: If the rail fit perfectly (remainder 0), and we failed,
            // we generally can't do better by putting it elsewhere (heuristic/observation).
            if (boards[i] == rails[rail_idx]) return false;
        }
    }

    return false;
}

int main() {
    // Fast I/O
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    ifstream fin("fence8.in");
    ofstream fout("fence8.out");

    fin >> N;
    boards.resize(N);
    for (int i = 0; i < N; ++i) {
        fin >> boards[i];
        total_board_capacity += boards[i];
    }

    fin >> R;
    rails.resize(R);
    for (int i = 0; i < R; ++i) {
        fin >> rails[i];
    }

    // Sort boards and rails
    sort(boards.begin(), boards.end());
    sort(rails.begin(), rails.end());

    // Precompute sums
    prefix_sum_rails.resize(R + 1, 0);
    for (int i = 0; i < R; ++i) {
        prefix_sum_rails[i + 1] = prefix_sum_rails[i] + rails[i];
    }

    // Binary search for the answer K
    // Range [0, R]
    int low = 0, high = R;
    int ans = 0;

    while (low <= high) {
        int mid = low + (high - low) / 2; // Trying to fit first 'mid' rails

        // Optimization: Total length check
        if (mid > 0 && prefix_sum_rails[mid] > total_board_capacity) {
            high = mid - 1;
            continue;
        }

        // Check using DFS
        // We try to fit rails[0...mid-1]. Start DFS from the largest rail (mid-1).
        if (mid == 0 || dfs(mid - 1, 0, 0)) {
            ans = mid;
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }

    fout << ans << endl;

    return 0;
}