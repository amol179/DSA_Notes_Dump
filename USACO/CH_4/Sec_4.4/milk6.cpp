/*
ID: amolgur1
TASK: milk6
LANG: C++
*/

#include <bits/stdc++.h>
using namespace std;
using ll = long long;

struct Edge {
    int to, rev;
    ll cap;
    Edge(int t, ll c, int r) : to(t), cap(c), rev(r) {}
};

struct Dinic {
    int n;
    vector<vector<Edge>> g;
    vector<int> level, it;
    Dinic(int n=0){ init(n); }
    void init(int _n){
        n=_n;
        g.assign(n,{});
        level.resize(n);
        it.resize(n);
    }
    void add_edge(int u,int v,ll c){
        g[u].emplace_back(v,c,(int)g[v].size());
        g[v].emplace_back(u,0,(int)g[u].size()-1);
    }
    bool bfs(int s,int t){
        fill(level.begin(), level.end(), -1);
        queue<int> q;
        level[s]=0; q.push(s);
        while(!q.empty()){
            int u=q.front(); q.pop();
            for(auto &e:g[u]){
                if(e.cap>0 && level[e.to]==-1){
                    level[e.to]=level[u]+1;
                    q.push(e.to);
                }
            }
        }
        return level[t]!=-1;
    }
    ll dfs(int u,int t,ll f){
        if(u==t) return f;
        for(int &i=it[u]; i<(int)g[u].size(); i++){
            Edge &e=g[u][i];
            if(e.cap>0 && level[e.to]==level[u]+1){
                ll pushed=dfs(e.to,t,min(f,e.cap));
                if(pushed>0){
                    e.cap-=pushed;
                    g[e.to][e.rev].cap+=pushed;
                    return pushed;
                }
            }
        }
        return 0;
    }
    ll maxflow(int s,int t){
        ll flow=0, INF=4e18;
        while(bfs(s,t)){
            fill(it.begin(), it.end(), 0);
            while(true){
                ll pushed=dfs(s,t,INF);
                if(pushed==0) break;
                flow+=pushed;
            }
        }
        return flow;
    }
};

struct E{int u,v; ll c;};

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    freopen("milk6.in","r",stdin);
    freopen("milk6.out","w",stdout);

    int N,M; cin>>N>>M;
    vector<E> edges(M);
    for(int i=0;i<M;i++){
        int s,e; ll c; cin>>s>>e>>c;
        edges[i]={s-1,e-1,c};
    }

    ll mult=(ll)M+1;
    vector<ll> caps(M);
    for(int i=0; i<M; i++){
        caps[i] = edges[i].c * mult + 1;
    }

    // 1. Calculate initial max flow on the full graph
    Dinic D_full(N);
    for(int i=0; i<M; i++){
        D_full.add_edge(edges[i].u, edges[i].v, caps[i]);
    }
    ll F_max = D_full.maxflow(0, N-1);

    // 2. Iteratively build the lexicographically smallest cut
    vector<int> cut;
    vector<bool> edge_active(M, true); // To keep track of the current graph

    for (int i = 0; i < M; i++) {
        // 3. Temporarily remove edge i and calculate new max flow
        edge_active[i] = false;

        Dinic D_temp(N);
        for (int j = 0; j < M; j++) {
            if (edge_active[j]) {
                D_temp.add_edge(edges[j].u, edges[j].v, caps[j]);
            }
        }
        ll F_prime = D_temp.maxflow(0, N-1);

        // 4. Check if we can greedily take this edge
        if (F_prime + caps[i] == F_max) {
            cut.push_back(i + 1);
            F_max = F_prime; // Commit to this choice
        } else {
            // Edge i is not in the cut, put it back for future checks
            edge_active[i] = true;
        }
    }

    // Output the result
    ll total_cost = 0;
    for(int idx : cut){
        total_cost += edges[idx-1].c;
    }

    cout << total_cost << " " << cut.size() << "\n";
    for(int idx : cut) {
        cout << idx << "\n";
    }

    return 0;
}