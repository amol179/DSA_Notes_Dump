/*
ID: amolgur1
LANG: C++11
TASK: fence4
*/

#include <bits/stdc++.h>
using namespace std;

struct Pt {
    double x, y;
};

static const double EPS = 1e-9;

// cross product of (b-a) x (c-a)
static double cross(const Pt &a, const Pt &b, const Pt &c) {
    return (b.x - a.x) * (c.y - a.y) - (b.y - a.y) * (c.x - a.x);
}

static bool onSegment(const Pt &p, const Pt &a, const Pt &b) {
    return min(a.x, b.x) - EPS <= p.x && p.x <= max(a.x, b.x) + EPS &&
           min(a.y, b.y) - EPS <= p.y && p.y <= max(a.y, b.y) + EPS;
}

// Check if two segments intersect (including endpoints)
static bool segIntersect(const Pt &p1, const Pt &p2, const Pt &p3, const Pt &p4) {
    double d1 = cross(p3, p4, p1);
    double d2 = cross(p3, p4, p2);
    double d3 = cross(p1, p2, p3);
    double d4 = cross(p1, p2, p4);

    if ((d1 > EPS && d2 < -EPS) || (d1 < -EPS && d2 > EPS))
        if ((d3 > EPS && d4 < -EPS) || (d3 < -EPS && d4 > EPS))
            return true;

    if (fabs(d1) <= EPS && onSegment(p1, p3, p4)) return true;
    if (fabs(d2) <= EPS && onSegment(p2, p3, p4)) return true;
    if (fabs(d3) <= EPS && onSegment(p3, p1, p2)) return true;
    if (fabs(d4) <= EPS && onSegment(p4, p1, p2)) return true;
    return false;
}

struct Edge {
    Pt a, b;
    int idx; // 0-based
};

// Ray origin p, direction r (non-zero). Segment q->s. Returns t (distance multiplier on r) or +inf if none
static double raySegDist(const Pt &p, const Pt &r, const Pt &q, const Pt &s) {
    double den = r.x * s.y - r.y * s.x; // cross(r, s)
    if (fabs(den) < EPS) return numeric_limits<double>::infinity(); // parallel

    double t = ((q.x - p.x) * s.y - (q.y - p.y) * s.x) / den; // cross(q-p, s)/den
    double u = ((q.x - p.x) * r.y - (q.y - p.y) * r.x) / den; // cross(q-p, r)/den

    if (t > EPS && u > -EPS && u < 1 + EPS) return t;
    return numeric_limits<double>::infinity();
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    freopen("fence4.in", "r", stdin);
    freopen("fence4.out", "w", stdout);

    int N;
    if (!(cin >> N)) return 0;
    Pt obs; cin >> obs.x >> obs.y;
    vector<Pt> v(N);
    for (int i = 0; i < N; ++i) cin >> v[i].x >> v[i].y;

    vector<Edge> edges;
    edges.reserve(N);
    for (int i = 0; i < N; ++i) {
        edges.push_back({v[i], v[(i + 1) % N], i});
    }

    // Validate non-crossing (excluding adjacent edges that share a vertex)
    for (int i = 0; i < N; ++i) {
        for (int j = i + 1; j < N; ++j) {
            if (j == i + 1 || (i == 0 && j == N - 1)) continue; // adjacent
            if (segIntersect(edges[i].a, edges[i].b, edges[j].a, edges[j].b)) {
                cout << "NOFENCE\n";
                return 0;
            }
        }
    }

    // Build rays: for every vertex angle, shoot angle-eps and angle+eps
    const double ANG_EPS = 1e-7;
    vector<pair<double,double>> dirs; // (cos, sin)
    dirs.reserve(2 * N);
    for (const Pt &p : v) {
        double ang = atan2(p.y - obs.y, p.x - obs.x);
        dirs.push_back({cos(ang - ANG_EPS), sin(ang - ANG_EPS)});
        dirs.push_back({cos(ang + ANG_EPS), sin(ang + ANG_EPS)});
    }

    vector<int> visible(N, 0);

    for (auto [cx, sy] : dirs) {
        Pt r{cx, sy};
        double best = numeric_limits<double>::infinity();
        int bestEdge = -1;
        for (const auto &e : edges) {
            Pt s{e.b.x - e.a.x, e.b.y - e.a.y};
            double t = raySegDist(obs, r, e.a, s);
            if (t < best) {
                best = t;
                bestEdge = e.idx;
            }
        }
        if (bestEdge != -1) visible[bestEdge] = 1;
    }

    // Collect output with required ordering
    struct Out { string text; int endIdx; int startIdx; };
    vector<Out> out;
    for (int i = 0; i < N; ++i) if (visible[i]) {
        int aIdx = i + 1;               // 1-based
        int bIdx = (i + 1) % N + 1;
        Pt a = v[i];
        Pt b = v[(i + 1) % N];
        if (aIdx > bIdx) { swap(aIdx, bIdx); swap(a, b); }
        out.push_back({to_string((int)a.x) + " " + to_string((int)a.y) + " " + to_string((int)b.x) + " " + to_string((int)b.y), bIdx, aIdx});
    }

    sort(out.begin(), out.end(), [](const Out &u, const Out &v){
        if (u.endIdx != v.endIdx) return u.endIdx < v.endIdx;
        return u.startIdx < v.startIdx;
    });

    cout << out.size() << "\n";
    for (auto &o : out) cout << o.text << "\n";
    return 0;
}
