/*
ID: amolgur1
TASK: tour
LANG: C++
*/

#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <algorithm>
#include <cstdio> // Required for freopen

using namespace std;

int main() {
    // Redirect standard input and output to the required files
    freopen("tour.in", "r", stdin);
    freopen("tour.out", "w", stdout);

    int n, v;
    cin >> n >> v;

    if (n <= 1) {
        cout << 1 << endl;
        return 0;
    }

    map<string, int> city_to_id;
    for (int i = 0; i < n; ++i) {
        string city_name;
        cin >> city_name;
        city_to_id[city_name] = i;
    }

    vector<vector<bool>> adj(n, vector<bool>(n, false));
    for (int i = 0; i < v; ++i) {
        string u_str, v_str;
        cin >> u_str >> v_str;
        int u = city_to_id[u_str];
        int v_id = city_to_id[v_str];
        adj[u][v_id] = true;
        adj[v_id][u] = true;
    }

    vector<vector<int>> dp(n, vector<int>(n, 0));

    // **FIX 1: Robust Base Case Initialization**
    // A path can start from city 0 to any connected city j.
    // The state dp[0][j] represents two paths: a trivial one at city 0,
    // and one from 0 to j. The cities visited are {0, j}, so the count is 2.
    for (int j = 1; j < n; ++j) {
        if (adj[0][j]) {
            dp[0][j] = 2;
        }
    }

    // Fill the DP table
    for (int j = 1; j < n; ++j) {
        for (int i = 0; i < j; ++i) {
            if (dp[i][j] > 0) {
                // Extend paths to a new city k > j
                for (int k = j + 1; k < n; ++k) {
                    // Extend path ending at j with flight j -> k
                    if (adj[j][k]) {
                        dp[i][k] = max(dp[i][k], dp[i][j] + 1);
                    }
                    // Extend path ending at i with flight i -> k
                    if (adj[i][k]) {
                        dp[j][k] = max(dp[j][k], dp[i][j] + 1);
                    }
                }
            }
        }
    }

    // **FIX 2: Correct Final Answer Calculation**
    int max_cities = 0;
    int best_prev_len = 0;

    // Iterate over all possible pairs of cities (i, j) that could be the
    // penultimate stops before the final city (n-1).
    for (int i = 0; i < n - 1; ++i) {
        for (int j = i + 1; j < n - 1; ++j) {
            // Check if both i and j have a flight to the final city
            if (adj[i][n - 1] && adj[j][n - 1]) {
                if (dp[i][j] > 0) {
                    best_prev_len = max(best_prev_len, dp[i][j]);
                }
            }
        }
    }

    if (best_prev_len > 0) {
        max_cities = best_prev_len + 1; // Add the final city to the count
    }

    // Handle the edge case of a simple start -> end -> start trip
    if (max_cities == 0 && adj[0][n - 1]) {
        max_cities = 2;
    }

    // If no tour is possible at all, the answer is 1 (the starting city)
    if (max_cities == 0) {
        max_cities = 1;
    }

    cout << max_cities << endl;

    return 0;
}