/*
TASK: cowxor
LANG: C++
USER: amolgur1
*/



#include <bits/stdc++.h>
using namespace std;

struct TrieNode {
    TrieNode* next[2];
    int index;
    TrieNode() {
        next[0] = next[1] = nullptr;
        index = -1;
    }
};

void insert(TrieNode* root, int num, int idx) {
    TrieNode* cur = root;
    for (int i = 20; i >= 0; i--) {
        int bit = (num >> i) & 1;
        if (cur->next[bit] == nullptr)
            cur->next[bit] = new TrieNode();
        cur = cur->next[bit];
    }
    cur->index = idx;
}

int query(TrieNode* root, int num) {
    TrieNode* cur = root;
    for (int i = 20; i >= 0; i--) {
        int bit = (num >> i) & 1;
        if (cur->next[bit ^ 1] != nullptr)
            cur = cur->next[bit ^ 1];
        else if (cur->next[bit] != nullptr)
            cur = cur->next[bit];
    }
    return cur->index;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    ifstream fin("cowxor.in");
    ofstream fout("cowxor.out");

    int n;
    fin >> n;
    vector<int> prefix(n + 1, 0);

    TrieNode* root = new TrieNode();
    insert(root, 0, 0);

    int ans = 0, l = 1, r = 1;
    for (int i = 1; i <= n; i++) {
        int x;
        fin >> x;
        prefix[i] = prefix[i - 1] ^ x;

        int j = query(root, prefix[i]);
        int curXor = prefix[i] ^ prefix[j];
        if (curXor > ans) {
            ans = curXor;
            l = j + 1;
            r = i;
        }
        insert(root, prefix[i], i);
    }

    fout << ans << " " << l << " " << r << "\n";

    return 0;
}
