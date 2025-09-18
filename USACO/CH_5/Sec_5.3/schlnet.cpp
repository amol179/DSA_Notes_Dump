/*
ID: amolgur1
TASK: schlnet
LANG: C++
*/

#include <bits/stdc++.h>
using namespace std;

const int MAXN = 105;
vector<int> g[MAXN], rg[MAXN];
bool vis[MAXN];
int comp[MAXN];
vector<int> order, compNodes[MAXN];

void dfs1(int v) {
    vis[v] = true;
    for (int u : g[v]) if (!vis[u]) dfs1(u);
    order.push_back(v);
}

void dfs2(int v, int c) {
    comp[v] = c;
    compNodes[c].push_back(v);
    for (int u : rg[v]) if (comp[u] == -1) dfs2(u, c);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    freopen("schlnet.in", "r", stdin);
    freopen("schlnet.out", "w", stdout);

    int N; cin >> N;
    for (int i = 1; i <= N; i++) {
        int x;
        while (cin >> x && x != 0) {
            g[i].push_back(x);
            rg[x].push_back(i);
        }
    }

    // Kosaraju’s algorithm
    memset(vis, 0, sizeof(vis));
    for (int i = 1; i <= N; i++) if (!vis[i]) dfs1(i);

    memset(comp, -1, sizeof(comp));
    int cid = 0;
    for (int i = N - 1; i >= 0; i--) {
        int v = order[i];
        if (comp[v] == -1) {
            dfs2(v, cid);
            cid++;
        }
    }

    if (cid == 1) {
        // already strongly connected
        cout << 1 << "\n" << 0 << "\n";
        return 0;
    }

    vector<int> indeg(cid, 0), outdeg(cid, 0);
    for (int v = 1; v <= N; v++) {
        for (int u : g[v]) {
            if (comp[v] != comp[u]) {
                outdeg[comp[v]]++;
                indeg[comp[u]]++;
            }
        }
    }

    int sources = 0, sinks = 0;
    for (int i = 0; i < cid; i++) {
        if (indeg[i] == 0) sources++;
        if (outdeg[i] == 0) sinks++;
    }

    cout << sources << "\n" << max(sources, sinks) << "\n";
    return 0;
}
