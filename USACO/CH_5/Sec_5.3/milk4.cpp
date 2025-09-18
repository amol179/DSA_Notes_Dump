/*
ID: amolgur1
TASK: milk4
LANG: C++
*/

#include <bits/stdc++.h>
using namespace std;

int Q, P;
vector<int> pails;
vector<int> best; // best solution found

// DP check if current subset can measure Q
bool canMeasure(const vector<int>& subset) {
    vector<bool> reachable(Q + 1, false);
    reachable[0] = true;
    for (int x = 0; x <= Q; ++x) {
        if (reachable[x]) {
            for (int p : subset) {
                if (x + p <= Q) reachable[x + p] = true;
            }
        }
    }
    return reachable[Q];
}

// DFS to try all subsets of given size in lex order
bool dfs(int start, vector<int>& chosen, int size) {
    if ((int)chosen.size() == size) {
        if (canMeasure(chosen)) {
            best = chosen;
            return true;
        }
        return false;
    }
    for (int i = start; i < P; ++i) {
        chosen.push_back(pails[i]);
        if (dfs(i + 1, chosen, size)) return true;
        chosen.pop_back();
    }
    return false;
}

int main() {
    freopen("milk4.in", "r", stdin);
    freopen("milk4.out", "w", stdout);

    cin >> Q >> P;
    pails.resize(P);
    for (int i = 0; i < P; ++i) cin >> pails[i];
    sort(pails.begin(), pails.end());

    // Try subsets of size 1..P
    for (int size = 1; size <= P; ++size) {
        vector<int> chosen;
        if (dfs(0, chosen, size)) break; // stop at first valid minimal set
    }

    cout << best.size();
    for (int p : best) cout << " " << p;
    cout << endl;

    return 0;
}
