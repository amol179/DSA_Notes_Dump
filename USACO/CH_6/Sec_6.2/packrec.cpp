/*
TASK: packrec
LANG: C++
USER: amolgur1
*/


#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <set>

using namespace std;

struct Rect {
    int w, h;
};

// Global variables to store the best results
int min_area = 9999999;
set<pair<int, int>> solutions;

// Helper to record a valid enclosing rectangle
void record(int w, int h) {
    int area = w * h;
    if (area < min_area) {
        min_area = area;
        solutions.clear();
    }
    if (area == min_area) {
        // Store smaller dimension first to handle p <= q requirement and duplicates
        solutions.insert({min(w, h), max(w, h)});
    }
}

// Check all 6 Layouts for a specific permutation and rotation
// Logic derived from the provided source text [cite: 721-743]
void check_layouts(const vector<Rect>& r) {
    int w, h;

    // Layout 1: All 4 in a row
    w = r[0].w + r[1].w + r[2].w + r[3].w;
    h = max({r[0].h, r[1].h, r[2].h, r[3].h});
    record(w, h);

    // Layout 2: 0, 1, 2 in a row; 3 on top
    w = max(r[0].w + r[1].w + r[2].w, r[3].w);
    h = max({r[0].h, r[1].h, r[2].h}) + r[3].h;
    record(w, h);

    // Layout 3: 0, 1 in a row; 2 on top; 3 to the side
    w = max(r[0].w + r[1].w, r[2].w) + r[3].w;
    h = max(max(r[0].h, r[1].h) + r[2].h, r[3].h);
    record(w, h);

    // Layout 4 & 5: 0 and 1 in a row; 2 and 3 stacked to the side
    // (The source combines these into one logic block)
    w = r[0].w + max(r[1].w, r[2].w) + r[3].w;
    h = max({r[0].h, r[1].h + r[2].h, r[3].h});
    record(w, h);

    // Layout 6: The "Windmill" (interlocked)
    // 0 and 1 on bottom row, 2 on top of 0, 3 on top of 1
    // This requires careful collision detection 
    h = max(r[0].h + r[2].h, r[1].h + r[3].h);
    w = r[0].w + r[1].w;

    // Check for overlaps
    if (r[0].h < r[1].h) 
        w = max(w, r[2].w + r[1].w);
    
    if (r[0].h + r[2].h > r[1].h) 
        w = max(w, r[2].w + r[3].w);
    
    if (r[1].h < r[0].h) 
        w = max(w, r[0].w + r[3].w);

    // Ensure top blocks fit individually
    w = max(w, r[2].w);
    w = max(w, r[3].w);

    record(w, h);
}

int main() {
    // USACO standard file I/O
    freopen("packrec.in", "r", stdin);
    freopen("packrec.out", "w", stdout);

    vector<Rect> rects(4);
    for (int i = 0; i < 4; i++) {
        cin >> rects[i].w >> rects[i].h;
    }

    // Sort indices to iterate through all permutations
    vector<int> p = {0, 1, 2, 3};

    do {
        // Iterate through all 16 rotation combinations
        // Bitmask i represents which rectangles are rotated (swapped w/h)
        for (int i = 0; i < 16; i++) {
            vector<Rect> current_r;
            for (int j = 0; j < 4; j++) {
                Rect r = rects[p[j]];
                if ((i >> j) & 1) {
                    current_r.push_back({r.h, r.w}); // Rotated
                } else {
                    current_r.push_back(r); // Original
                }
            }
            check_layouts(current_r);
        }
    } while (next_permutation(p.begin(), p.end()));

    // Output results
    cout << min_area << endl;
    for (auto sol : solutions) {
        cout << sol.first << " " << sol.second << endl;
    }

    return 0;
}