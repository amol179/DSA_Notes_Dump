/*
ID: amolgur1
LANG: C++
TASK: picture
*/
#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <cmath>

using namespace std;

// Event for the plane sweep. `coord` is the axis we sweep along.
struct Event {
    int coord;
    int p1, p2; // The range on the sweep line
    int type;   // +1 for start, -1 for end

    // Sort events by their primary coordinate
    bool operator<(const Event& other) const {
        return coord < other.coord;
    }
};

// This function performs one complete sweep (e.g., a horizontal sweep) to find
// the perimeter contribution from the other dimension (e.g., vertical).
long long solve_component(vector<Event>& events, set<int>& p_coords_set) {
    if (events.empty()) {
        return 0;
    }

    // Create a sorted list of unique coordinates for the sweep line and a map for lookup
    vector<int> p_coords(p_coords_set.begin(), p_coords_set.end());
    map<int, int> p_to_idx;
    for (size_t i = 0; i < p_coords.size(); ++i) {
        p_to_idx[p_coords[i]] = i;
    }

    int n_p = p_coords.size();
    if (n_p < 2) return 0;

    // cover[k] counts rectangles over interval [p_coords[k], p_coords[k+1]]
    vector<int> cover(n_p, 0);
    long long perimeter = 0;

    sort(events.begin(), events.end());

    for (size_t i = 0; i < events.size(); ) {
        int current_coord = events[i].coord;

        // 1. Get covered intervals and length BEFORE updates
        vector<bool> covered_before(n_p - 1, false);
        long long old_len = 0;
        for (int k = 0; k < n_p - 1; ++k) {
            if (cover[k] > 0) {
                covered_before[k] = true;
                old_len += p_coords[k + 1] - p_coords[k];
            }
        }

        // 2. Process ALL events at current_coord
        int j = i;
        while (j < events.size() && events[j].coord == current_coord) {
            int p1_idx = p_to_idx[events[j].p1];
            int p2_idx = p_to_idx[events[j].p2];
            // Apply the event's type (+1 or -1) to all elementary intervals it covers
            for (int k = p1_idx; k < p2_idx; ++k) {
                cover[k] += events[j].type;
            }
            j++;
        }

        // 3. Get length AFTER updates and calculate length of intersection
        long long new_len = 0;
        long long intersection_len = 0;
        for (int k = 0; k < n_p - 1; ++k) {
            if (cover[k] > 0) {
                new_len += p_coords[k + 1] - p_coords[k];
                if (covered_before[k]) {
                    intersection_len += p_coords[k + 1] - p_coords[k];
                }
            }
        }

        // 4. Add the length of the symmetric difference to the perimeter
        perimeter += (old_len + new_len - 2 * intersection_len);

        i = j;
    }
    return perimeter;
}

int main() {
    ifstream fin("picture.in");
    ofstream fout("picture.out");

    int N;
    fin >> N;

    vector<Event> events_x, events_y;
    set<int> x_coords_set, y_coords_set;

    for (int i = 0; i < N; ++i) {
        int x1, y1, x2, y2;
        fin >> x1 >> y1 >> x2 >> y2;
        
        // Events for horizontal sweep (to find vertical perimeter)
        events_x.push_back({x1, y1, y2, 1});
        events_x.push_back({x2, y1, y2, -1});
        y_coords_set.insert(y1);
        y_coords_set.insert(y2);

        // Events for vertical sweep (to find horizontal perimeter)
        events_y.push_back({y1, x1, x2, 1});
        events_y.push_back({y2, x1, x2, -1});
        x_coords_set.insert(x1);
        x_coords_set.insert(x2);
    }
    
    long long vertical_perimeter = solve_component(events_x, y_coords_set);
    long long horizontal_perimeter = solve_component(events_y, x_coords_set);

    fout << vertical_perimeter + horizontal_perimeter << endl;

    return 0;
}