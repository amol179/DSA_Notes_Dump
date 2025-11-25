/*
ID: amolgur1
TASK: cryptcow
LANG: C++
*/
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <cstring>

using namespace std;

const string TARGET = "Begin the Escape execution at the Break of Dawn";
const int HASH_SIZE = 999983; // Prime number for hash table

bool visited[HASH_SIZE];
string start_str;
int target_len;

// ELF Hash function to map strings to integers for the visited array
unsigned int elf_hash(const string& s) {
    unsigned int h = 0, g;
    for (char c : s) {
        h = (h << 4) + c;
        g = h & 0xF0000000L;
        if (g) h ^= g >> 24;
        h &= ~g;
    }
    return h % HASH_SIZE;
}

// Check if all non-COW segments in 's' exist in TARGET
// This corresponds to the "check_frags" optimization [cite: 1556]
bool valid_segments(const string& s) {
    int n = s.length();
    int last = 0;
    for (int i = 0; i < n; ++i) {
        if (s[i] == 'C' || s[i] == 'O' || s[i] == 'W') {
            // Check the segment ending here
            if (i > last) {
                string sub = s.substr(last, i - last);
                if (TARGET.find(sub) == string::npos) return false;
            }
            last = i + 1;
        }
    }
    // Check the final segment
    if (last < n) {
        string sub = s.substr(last);
        if (TARGET.find(sub) == string::npos) return false;
    }
    return true;
}

// Recursive search function
bool search(string s) {
    if (s == TARGET) return true;

    // Hash check
    unsigned int h = elf_hash(s);
    if (visited[h]) return false;
    visited[h] = true;

    // Pruning: Valid segments check
    if (!valid_segments(s)) return false;

    // Find positions of C, O, W
    vector<int> C, O, W;
    for (int i = 0; i < s.length(); ++i) {
        if (s[i] == 'C') C.push_back(i);
        else if (s[i] == 'O') O.push_back(i);
        else if (s[i] == 'W') W.push_back(i);
    }

    // Try all valid C...O...W combinations
    // Optimization: Iterate O first, then C (before O), then W (after O)
    for (int o_idx : O) {
        for (int c_idx : C) {
            if (c_idx > o_idx) break; // C must be before O

            for (int w_idx : W) {
                if (w_idx < o_idx) continue; // W must be after O

                // Construct the new string by "undoing" the swap
                // Encrypted:  [Pre] C [Seg1] O [Seg2] W [Post]
                // Decrypted:  [Pre] [Seg2] [Seg1] [Post]
                
                // P1: s[0...c-1]
                // P2: s[c+1...o-1] (Seg1)
                // P3: s[o+1...w-1] (Seg2)
                // P4: s[w+1...end]
                
                // Concatenate: P1 + P3 + P2 + P4
                string next_s = s.substr(0, c_idx) + 
                                s.substr(o_idx + 1, w_idx - o_idx - 1) +
                                s.substr(c_idx + 1, o_idx - c_idx - 1) +
                                s.substr(w_idx + 1);

                if (search(next_s)) return true;
            }
        }
    }
    return false;
}

int main() {
    ifstream fin("cryptcow.in");
    ofstream fout("cryptcow.out");

    if (!fin) return 0;
    getline(fin, start_str);
    
    target_len = TARGET.length();
    int s_len = start_str.length();

    // 1. Length Check 
    if ((s_len - target_len) % 3 != 0) {
        fout << "0 0" << endl;
        return 0;
    }
    
    int num_encryptions = (s_len - target_len) / 3;

    // 2. Character Frequency Check [cite: 1555]
    int s_counts[256] = {0};
    int t_counts[256] = {0};
    for (char c : start_str) s_counts[c]++;
    for (char c : TARGET) t_counts[c]++;

    // C, O, W counts must match number of encryptions
    if (s_counts['C'] != num_encryptions || 
        s_counts['O'] != num_encryptions || 
        s_counts['W'] != num_encryptions) {
        fout << "0 0" << endl;
        return 0;
    }

    // All other characters must match TARGET exactly
    for (int i = 0; i < 256; ++i) {
        if (i != 'C' && i != 'O' && i != 'W') {
            if (s_counts[i] != t_counts[i]) {
                fout << "0 0" << endl;
                return 0;
            }
        }
    }

    // Run DFS
    if (search(start_str)) {
        fout << "1 " << num_encryptions << endl;
    } else {
        fout << "0 0" << endl;
    }

    return 0;
}