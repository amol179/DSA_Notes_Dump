/* ID: <yourid>
   LANG: C++
   PROG: snail
*/
#include <bits/stdc++.h>
using namespace std;

int n, b;
int graphg[130][130];   // 1 = barrier/boundary
bool used[130][130];
int ans = 0;

void dfs(int x, int y, int step) {
    ans = max(ans, step);

    // try move up
    if (graphg[x-1][y] != 1) {
        int t = x-1, z = step;
        while (graphg[t][y] != 1) {
            if (used[t][y]) { ans = max(ans, z); goto fail_up; }
            used[t][y] = true;
            ++z;
            --t;
        }
        dfs(t+1, y, z);
    fail_up:
        for (int i = t+1; i <= x-1; ++i) used[i][y] = false;
    }

    // try move down
    if (graphg[x+1][y] != 1) {
        int t = x+1, z = step;
        while (graphg[t][y] != 1) {
            if (used[t][y]) { ans = max(ans, z); goto fail_down; }
            used[t][y] = true;
            ++z;
            ++t;
        }
        dfs(t-1, y, z);
    fail_down:
        for (int i = x+1; i <= t-1; ++i) used[i][y] = false;
    }

    // try move left
    if (graphg[x][y-1] != 1) {
        int t = y-1, z = step;
        while (graphg[x][t] != 1) {
            if (used[x][t]) { ans = max(ans, z); goto fail_left; }
            used[x][t] = true;
            ++z;
            --t;
        }
        dfs(x, t+1, z);
    fail_left:
        for (int i = t+1; i <= y-1; ++i) used[x][i] = false;
    }

    // try move right
    if (graphg[x][y+1] != 1) {
        int t = y+1, z = step;
        while (graphg[x][t] != 1) {
            if (used[x][t]) { ans = max(ans, z); goto fail_right; }
            used[x][t] = true;
            ++z;
            ++t;
        }
        dfs(x, t-1, z);
    fail_right:
        for (int i = y+1; i <= t-1; ++i) used[x][i] = false;
    }
}

int main() {
    freopen("snail.in", "r", stdin);
    freopen("snail.out", "w", stdout);

    scanf("%d %d", &n, &b);
    // mark barriers, and create boundary padding at 0 and n+1
    for (int i = 0; i <= n+1; ++i) {
        for (int j = 0; j <= n+1; ++j) graphg[i][j] = 0;
    }
    for (int i = 0; i < b; ++i) {
        char s[10];
        scanf("%s", s);
        int col = s[0] - 'A' + 1;
        int row = atoi(s+1); // rows numbered 1..n
        graphg[row][col] = 1;
    }
    for (int i = 0; i <= n+1; ++i) {
        graphg[0][i] = graphg[n+1][i] = 1;
        graphg[i][0] = graphg[i][n+1] = 1;
    }

    memset(used, 0, sizeof(used));
    used[1][1] = true; // start at A1 which we map to (1,1)
    dfs(1, 1, 1);
    printf("%d\n", ans);
    return 0;
}
