/*
ID: amolgur1
TASK: window
LANG: C++
*/

#include <bits/stdc++.h>
using namespace std;

struct Rect {
    int x1, y1, x2, y2;
};

map<char, Rect> id_map;
vector<char> windows; // bottom -> top

int area(const Rect &r) {
    return max(0, r.x2 - r.x1) * max(0, r.y2 - r.y1);
}

bool intersect(const Rect &a, const Rect &b, Rect &out) {
    out.x1 = max(a.x1, b.x1);
    out.y1 = max(a.y1, b.y1);
    out.x2 = min(a.x2, b.x2);
    out.y2 = min(a.y2, b.y2);
    return (out.x1 < out.x2 && out.y1 < out.y2);
}

vector<Rect> subtract(const Rect &r, const Rect &cover) {
    vector<Rect> res;
    Rect inter;
    if (!intersect(r, cover, inter)) {
        res.push_back(r);
        return res;
    }

    // left
    if (r.x1 < inter.x1)
        res.push_back({r.x1, r.y1, inter.x1, r.y2});
    // right
    if (inter.x2 < r.x2)
        res.push_back({inter.x2, r.y1, r.x2, r.y2});
    // bottom
    if (r.y1 < inter.y1)
        res.push_back({inter.x1, r.y1, inter.x2, inter.y1});
    // top
    if (inter.y2 < r.y2)
        res.push_back({inter.x1, inter.y2, inter.x2, r.y2});

    return res;
}

int compute_visible(const Rect &rect, const vector<Rect> &covers) {
    vector<Rect> rects = {rect};
    for (auto &c : covers) {
        vector<Rect> newRects;
        for (auto &r : rects) {
            auto parts = subtract(r, c);
            newRects.insert(newRects.end(), parts.begin(), parts.end());
        }
        rects.swap(newRects);
    }
    int total = 0;
    for (auto &r : rects) total += area(r);
    return total;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    freopen("window.in", "r", stdin);
    freopen("window.out", "w", stdout);

    string line;
    while (getline(cin, line)) {
        if (line.empty()) continue;

        if (line[0] == 'w') {
            char id = line[2];
            vector<int> nums;
            string num;
            for (int i = 4; i < (int)line.size(); i++) {
                if (isdigit(line[i])) {
                    num.push_back(line[i]);
                } else if (!num.empty()) {
                    nums.push_back(stoi(num));
                    num.clear();
                }
            }
            int x1 = nums[0], y1 = nums[1], x2 = nums[2], y2 = nums[3];
            Rect r = {min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2)};
            id_map[id] = r;
            windows.push_back(id);

        } else if (line[0] == 't') {
            char id = line[2];
            auto it = find(windows.begin(), windows.end(), id);
            if (it != windows.end()) {
                windows.erase(it);
                windows.push_back(id);
            }

        } else if (line[0] == 'b') {
            char id = line[2];
            auto it = find(windows.begin(), windows.end(), id);
            if (it != windows.end()) {
                windows.erase(it);
                windows.insert(windows.begin(), id);
            }

        } else if (line[0] == 'd') {
            char id = line[2];
            auto it = find(windows.begin(), windows.end(), id);
            if (it != windows.end()) {
                windows.erase(it);
                id_map.erase(id);
            }

        } else if (line[0] == 's') {
            char id = line[2];
            if (!id_map.count(id)) continue;

            Rect r = id_map[id];
            int idx = find(windows.begin(), windows.end(), id) - windows.begin();

            vector<Rect> covers;
            for (int i = idx + 1; i < (int)windows.size(); i++) {
                covers.push_back(id_map[windows[i]]);
            }

            int total = area(r);
            int visible = compute_visible(r, covers);

            double percent = (double)visible * 100.0 / total;
            cout.setf(ios::fixed);
            cout << setprecision(3) << percent << "\n";
        }
    }

    return 0;
}
