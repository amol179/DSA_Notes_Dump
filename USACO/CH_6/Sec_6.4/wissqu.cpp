/*
ID: amolgur1
TASK: wissqu
LANG: C++
*/
#include <iostream>
#include <vector>
#include <string>
#include <fstream>

using namespace std;

// Grid dimensions
const int N = 4;

// Global state
char grid[N][N];
bool visited[N][N]; // Tracks if a cell has been replaced
int herds[5];       // Counts of new herds: A=0, B=1, C=2, D=3, E=4
char types[5] = {'A', 'B', 'C', 'D', 'E'};

// Output variables
struct Step {
    char type;
    int r, c;
};
vector<Step> current_path;
vector<Step> best_path;
long long solution_count = 0;
bool found_first = false;

// Helper to check if placing 'type' at (r, c) is valid
bool isValid(int r, int c, char type) {
    // Constraint 1: Cannot place on a square occupied by same type
    if (grid[r][c] == type) return false;

    // Constraint 2: Cannot be adjacent to same type
    for (int dr = -1; dr <= 1; dr++) {
        for (int dc = -1; dc <= 1; dc++) {
            if (dr == 0 && dc == 0) continue;
            
            int nr = r + dr;
            int nc = c + dc;
            
            // Check bounds
            if (nr >= 0 && nr < N && nc >= 0 && nc < N) {
                if (grid[nr][nc] == type) return false;
            }
        }
    }
    return true;
}

void dfs(int depth) {
    // Base case: All 16 herds placed
    if (depth == 16) {
        if (!found_first) {
            best_path = current_path;
            found_first = true;
        }
        solution_count++;
        return;
    }

    // Determine loop bounds for Herd Type
    // Depth 0 must be 'D' (index 3). Others can be A-E (indices 0-4).
    int startT = 0, endT = 4;
    if (depth == 0) {
        startT = 3; 
        endT = 3;
    }

    // Lexicographical order: Type -> Row -> Col
    for (int t = startT; t <= endT; t++) {
        if (herds[t] > 0) {
            char typeChar = types[t];
            
            for (int r = 0; r < N; r++) {
                for (int c = 0; c < N; c++) {
                    // Only place in unvisited cells
                    if (!visited[r][c]) {
                        if (isValid(r, c, typeChar)) {
                            // Save state
                            char oldVal = grid[r][c];
                            
                            // Apply move
                            grid[r][c] = typeChar;
                            visited[r][c] = true;
                            herds[t]--;
                            current_path.push_back({typeChar, r + 1, c + 1});

                            // Recurse
                            dfs(depth + 1);

                            // Backtrack
                            current_path.pop_back();
                            herds[t]++;
                            visited[r][c] = false;
                            grid[r][c] = oldVal;
                        }
                    }
                }
            }
        }
    }
}

int main() {
    ifstream fin("wissqu.in");
    ofstream fout("wissqu.out");

    // Read Initial Grid
    for (int i = 0; i < N; i++) {
        string row;
        fin >> row;
        for (int j = 0; j < N; j++) {
            grid[i][j] = row[j];
            visited[i][j] = false;
        }
    }

    // Initialize herd counts to place: 3A, 3B, 3C, 4D, 3E
    herds[0] = 3; // A
    herds[1] = 3; // B
    herds[2] = 3; // C
    herds[3] = 4; // D
    herds[4] = 3; // E

    // Start Search
    dfs(0);

    // Output results
    for (const auto& step : best_path) {
        fout << step.type << " " << step.r << " " << step.c << endl;
    }
    fout << solution_count << endl;

    return 0;
}