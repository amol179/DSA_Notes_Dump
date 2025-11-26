/*
ID: amolgur1
TASK: fence3
LANG: C++
*/
#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <iomanip>

using namespace std;

struct Fence {
    double x1, y1, x2, y2;
};

int F;
vector<Fence> fences;

// Helper: Distance between two points
double dist_sq(double x1, double y1, double x2, double y2) {
    return (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2);
}

// Calculate shortest distance from point (px, py) to a specific fence segment
double dist_to_segment(double px, double py, const Fence& f) {
    // Since fences are axis-parallel, we handle Horizontal and Vertical separately
    // But a generic approach works too and handles potential point-fences easily
    
    double l2 = dist_sq(f.x1, f.y1, f.x2, f.y2);
    if (l2 == 0) return sqrt(dist_sq(px, py, f.x1, f.y1)); // Fence is a point

    // Projection scalar t
    double t = ((px - f.x1) * (f.x2 - f.x1) + (py - f.y1) * (f.y2 - f.y1)) / l2;
    
    // Clamp t to segment [0, 1]
    t = max(0.0, min(1.0, t));
    
    // Closest point on segment
    double proj_x = f.x1 + t * (f.x2 - f.x1);
    double proj_y = f.y1 + t * (f.y2 - f.y1);
    
    return sqrt(dist_sq(px, py, proj_x, proj_y));
}

// Calculate total wire length needed for source at (x, y)
double total_wire_len(double x, double y) {
    double sum = 0;
    for (const auto& f : fences) {
        sum += dist_to_segment(x, y, f);
    }
    return sum;
}

int main() {
    ifstream fin("fence3.in");
    ofstream fout("fence3.out");

    fin >> F;
    double start_x = 0, start_y = 0;
    for (int i = 0; i < F; ++i) {
        Fence f;
        fin >> f.x1 >> f.y1 >> f.x2 >> f.y2;
        // Standardize: x1 <= x2, y1 <= y2
        if (f.x1 > f.x2) swap(f.x1, f.x2);
        if (f.y1 > f.y2) swap(f.y1, f.y2);
        fences.push_back(f);
        start_x += (f.x1 + f.x2) / 2.0;
        start_y += (f.y1 + f.y2) / 2.0;
    }
    
    // Start search at the centroid of the fences
    double cx = start_x / F;
    double cy = start_y / F;
    double min_dist = total_wire_len(cx, cy);
    
    // Step-wise optimization (Hill Climbing)
    // Start with a large step and refine it
    double step = 50.0; 
    
    while (step > 0.00001) {
        bool improved = false;
        // Try moving in 4 directions
        // dx, dy pairs: (0,1), (0,-1), (1,0), (-1,0)
        double dirs[4][2] = {{0, step}, {0, -step}, {step, 0}, {-step, 0}};
        
        for (int i = 0; i < 4; ++i) {
            double nx = cx + dirs[i][0];
            double ny = cy + dirs[i][1];
            
            double d = total_wire_len(nx, ny);
            if (d < min_dist) {
                min_dist = d;
                cx = nx;
                cy = ny;
                improved = true;
                // Greedy choice: take the first improvement found in this step cycle
                // Alternatively, check all 4 and pick best. Both converge.
                break; 
            }
        }
        
        // If we didn't improve, we are likely close to optimum for this resolution.
        // Decrease step size to refine search.
        if (!improved) {
            step /= 2.0;
        }
    }

    fout << fixed << setprecision(1) << cx << " " << cy << " " << min_dist << endl;

    return 0;
}