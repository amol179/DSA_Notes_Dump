
/*
ID: amolgur1
PROG: telecow
LANG: C++
*/

#include <iostream>
#include <fstream>
#include <vector>
#include <queue>
#include <algorithm>
#include <cstring>

// Constants for graph dimensions and infinite capacity
const int MAX_N = 101;
const int MAX_NODES = 2 * MAX_N + 2;
const int INF = 1e9;

// Global variables
int N, M, C1, C2;
int capacity[MAX_NODES][MAX_NODES];
int original_capacity[MAX_NODES][MAX_NODES];
int parent[MAX_NODES];

// BFS to find an augmenting path in the residual graph
bool bfs(int s, int t, int current_capacity[][MAX_NODES]) {
    std::fill(parent, parent + 2 * N + 1, -1);
    std::queue<int> q;
    q.push(s);
    parent[s] = s;

    while (!q.empty()) {
        int u = q.front();
        q.pop();

        for (int v = 1; v <= 2 * N; ++v) {
            if (parent[v] == -1 && current_capacity[u][v] > 0) {
                parent[v] = u;
                if (v == t) return true;
                q.push(v);
            }
        }
    }
    return false;
}

// Edmonds-Karp algorithm to calculate max flow
int calculate_max_flow(int s, int t, int base_capacity[][MAX_NODES]) {
    int temp_capacity[MAX_NODES][MAX_NODES];
    memcpy(temp_capacity, base_capacity, sizeof(temp_capacity));
    
    int flow = 0;
    
    while (bfs(s, t, temp_capacity)) {
        int path_flow = INF;
        for (int v = t; v != s; v = parent[v]) {
            int u = parent[v];
            path_flow = std::min(path_flow, temp_capacity[u][v]);
        }
        
        for (int v = t; v != s; v = parent[v]) {
            int u = parent[v];
            temp_capacity[u][v] -= path_flow;
            temp_capacity[v][u] += path_flow;
        }
        flow += path_flow;
    }
    return flow;
}

int main() {
    std::ifstream fin("telecow.in");
    std::ofstream fout("telecow.out");

    fin >> N >> M >> C1 >> C2;

    // Node mapping: v_in -> v, v_out -> v + N
    int source = C1 + N;
    int sink = C2;

    // Build the initial capacity matrix for the transformed graph
    memset(original_capacity, 0, sizeof(original_capacity));

    // Add vertex-split edges with capacity 1 (or INF for c1, c2)
    for (int i = 1; i <= N; ++i) {
        if (i == C1 || i == C2) {
            original_capacity[i][i + N] = INF;
        } else {
            original_capacity[i][i + N] = 1;
        }
    }

    // Add original connection edges with infinite capacity
    for (int i = 0; i < M; ++i) {
        int u, v;
        fin >> u >> v;
        original_capacity[u + N][v] = INF; // u_out -> v_in
        original_capacity[v + N][u] = INF; // v_out -> u_in
    }

    // Calculate initial max flow, which equals the min cut size
    int min_cut_size = calculate_max_flow(source, sink, original_capacity);
    fout << min_cut_size << std::endl;

    if (min_cut_size == 0) {
        fout << std::endl;
        return 0;
    }

    // Greedily find the lexicographically smallest cut set
    std::vector<int> cut_nodes;
    int working_capacity[MAX_NODES][MAX_NODES];
    memcpy(working_capacity, original_capacity, sizeof(working_capacity));
    int current_max_flow = min_cut_size;

    for (int i = 1; i <= N; ++i) {
        if (i == C1 || i == C2) continue;
        if (cut_nodes.size() == min_cut_size) break;

        int saved_cap = working_capacity[i][i + N];
        if (saved_cap == 0) continue; 
        
        // Tentatively remove node i and check the impact on the flow
        working_capacity[i][i + N] = 0;
        int new_flow = calculate_max_flow(source, sink, working_capacity);
        
        if (current_max_flow - new_flow == 1) {
            // If flow drops by 1, i must be in the lexico. smallest cut.
            // Make the removal permanent for future iterations.
            cut_nodes.push_back(i);
            current_max_flow = new_flow;
        } else {
            // Otherwise, restore the node. It's not in our desired cut.
            working_capacity[i][i + N] = saved_cap;
        }
    }
    
    // Output the resulting set of nodes
    for (size_t i = 0; i < cut_nodes.size(); ++i) {
        fout << cut_nodes[i] << (i == cut_nodes.size() - 1 ? "" : " ");
    }
    fout << std::endl;

    return 0;
}