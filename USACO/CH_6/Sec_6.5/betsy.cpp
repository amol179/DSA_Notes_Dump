/*
ID: amolgur1
LANG: C++11
TASK: betsy
*/

#include <iostream>
#include <vector>

using namespace std;

int N;
long long total_tours = 0;
bool visited[9][9]; // Grid with padding to avoid boundary checks

// Direction arrays: Up, Down, Left, Right
int dr[] = {-1, 1, 0, 0};
int dc[] = {0, 0, -1, 1};

// Helper to calculate the number of valid unvisited neighbors for a cell
int get_degree(int r, int c) {
    int deg = 0;
    for (int i = 0; i < 4; i++) {
        if (!visited[r + dr[i]][c + dc[i]]) {
            deg++;
        }
    }
    return deg;
}

void solve(int r, int c, int count) {
    // Base Case: If we reached the Market (Lower Left)
    if (r == N && c == 1) {
        // Only count if we have visited all N*N squares
        if (count == N * N) {
            total_tours++;
        }
        return;
    }

    // Optimization 1: Wall/Split Check
    // If we have created a barrier such that we can move Left/Right but not Up/Down,
    // we have effectively split the grid. Since we can't be in two places, one side becomes unreachable.
    if (visited[r - 1][c] && visited[r + 1][c] &&
        !visited[r][c - 1] && !visited[r][c + 1])
        return;

    if (visited[r][c - 1] && visited[r][c + 1] &&
        !visited[r - 1][c] && !visited[r + 1][c])
        return;

    // Optimization 2: Lookahead for Dead Ends
    // Check neighbors to see if any are "starving" (have only 1 way in/out)
    int forced_dir = -1;
    int num_dead_ends = 0;

    for (int i = 0; i < 4; i++) {
        int nr = r + dr[i];
        int nc = c + dc[i];
        
        // Only check unvisited, valid cells
        if (!visited[nr][nc]) {
            int deg = get_degree(nr, nc);
            
            // If a cell has 0 neighbors, it's unreachable (unless it's the current target at the very end, 
            // but strict topological check usually catches this as 1 before 0)
            if (deg == 0) return; 
            
            // If a cell has 1 neighbor, we MUST visit it next.
            // Exception: The Target (N, 1) usually has degree 1 right before we finish.
            // If we are not finishing, and target has degree 1, we must go there (and fail count check).
            if (deg == 1) {
                num_dead_ends++;
                forced_dir = i;
            }
        }
    }

    // If more than one neighbor requires immediate attention, we fail.
    if (num_dead_ends > 1) return;

    visited[r][c] = true;

    if (num_dead_ends == 1) {
        // Forced move: We must go to the neighbor with degree 1
        solve(r + dr[forced_dir], c + dc[forced_dir], count + 1);
    } else {
        // Standard DFS: Try all valid directions
        for (int i = 0; i < 4; i++) {
            if (!visited[r + dr[i]][c + dc[i]]) {
                solve(r + dr[i], c + dc[i], count + 1);
            }
        }
    }

    visited[r][c] = false; // Backtrack
}

int main() {
    // Optimize I/O operations
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    freopen("betsy.in", "r", stdin);
    freopen("betsy.out", "w", stdout);

    if (!(cin >> N)) return 0;

    // Initialize the visited array with a boundary of 'true' (walls)
    // The actual grid is 1..N, so 0 and N+1 are walls.
    for (int i = 0; i <= N + 1; i++) {
        for (int j = 0; j <= N + 1; j++) {
            visited[i][j] = true; 
        }
    }

    // clear the interior to 'false' (unvisited)
    for (int i = 1; i <= N; i++) {
        for (int j = 1; j <= N; j++) {
            visited[i][j] = false;
        }
    }

    // Start DFS from Farm (1, 1) with step count 1
    solve(1, 1, 1);

    cout << total_tours << endl;

    return 0;
}