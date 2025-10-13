

/*
ID: amolgur1
PROG: charrec
LANG: C++
*/
#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>

// Global data structures to hold font and input image data
std::vector<std::vector<std::string>> font(27, std::vector<std::string>(20));
std::vector<std::string> input_lines;
int n_input;

const int INF = 1e9; // A large value representing infinity for costs
const int MAX_ERROR = 120; // 30% of 400 bits, the maximum allowed corruption

// A struct to hold the result of matching a segment to a font character
struct MatchResult {
    int cost = INF;
    char character = '?';
};

// Function to compare two 20-character lines and return the number of different bits.
int compare_lines(const std::string& s1, const std::string& s2) {
    int diff = 0;
    for (int i = 0; i < 20; ++i) {
        if (s1[i] != s2[i]) {
            diff++;
        }
    }
    return diff;
}

// Calculates the minimum corruption cost for a 19-line segment (missing line).
// It efficiently calculates costs by updating the previous cost iteratively.
int calculate_cost_19(int start_idx, int char_idx) {
    const auto& font_char = font[char_idx];
    
    // Initial cost assuming the first font line (index 0) is missing
    int current_cost = 0;
    for (int j = 0; j < 19; ++j) {
        current_cost += compare_lines(input_lines[start_idx + j], font_char[j + 1]);
    }

    int min_cost = current_cost;

    // Use a recurrence to find costs for missing lines 1 through 19
    for (int k = 0; k < 19; ++k) {
        // C(k+1) = C(k) + compare(input[k], font[k]) - compare(input[k], font[k+1])
        current_cost += compare_lines(input_lines[start_idx + k], font_char[k]);
        current_cost -= compare_lines(input_lines[start_idx + k], font_char[k + 1]);
        min_cost = std::min(min_cost, current_cost);
    }
    return min_cost;
}

// Calculates the corruption cost for a normal 20-line segment.
int calculate_cost_20(int start_idx, int char_idx) {
    const auto& font_char = font[char_idx];
    int total_cost = 0;
    for (int i = 0; i < 20; ++i) {
        total_cost += compare_lines(input_lines[start_idx + i], font_char[i]);
    }
    return total_cost;
}

// Calculates the minimum corruption cost for a 21-line segment (duplicated line).
// It also uses an efficient iterative approach.
int calculate_cost_21(int start_idx, int char_idx) {
    const auto& font_char = font[char_idx];

    // Initial cost assuming the first font line (index 0) is duplicated
    int m_k = std::min(
        compare_lines(input_lines[start_idx], font_char[0]),
        compare_lines(input_lines[start_idx + 1], font_char[0])
    );
    int current_cost = m_k;
    for (int j = 1; j < 20; ++j) {
        current_cost += compare_lines(input_lines[start_idx + j + 1], font_char[j]);
    }
    
    int min_cost = current_cost;

    // Use a recurrence to find costs for duplicated lines 1 through 19
    for (int k = 0; k < 19; ++k) {
        int m_k_plus_1 = std::min(
            compare_lines(input_lines[start_idx + k + 1], font_char[k + 1]),
            compare_lines(input_lines[start_idx + k + 2], font_char[k + 1])
        );
        
        current_cost = current_cost - m_k 
                     + compare_lines(input_lines[start_idx + k], font_char[k])
                     + m_k_plus_1
                     - compare_lines(input_lines[start_idx + k + 2], font_char[k + 1]);

        min_cost = std::min(min_cost, current_cost);
        m_k = m_k_plus_1;
    }
    return min_cost;
}


// Finds the best matching character for a segment of input lines of a given length.
MatchResult find_best_match(int start_idx, int len) {
    MatchResult best_match;
    std::string char_map = " abcdefghijklmnopqrstuvwxyz";

    // Iterate through all 27 possible characters to find the one with the minimum cost
    for (int char_idx = 0; char_idx < 27; ++char_idx) {
        int current_cost;
        if (len == 19) {
            current_cost = calculate_cost_19(start_idx, char_idx);
        } else if (len == 20) {
            current_cost = calculate_cost_20(start_idx, char_idx);
        } else { // len == 21
            current_cost = calculate_cost_21(start_idx, char_idx);
        }
        
        if (current_cost < best_match.cost) {
            best_match.cost = current_cost;
            best_match.character = char_map[char_idx];
        }
    }
    
    // If the best match is still too corrupted, mark it as unrecognized ('?')
    if (best_match.cost > MAX_ERROR) {
        best_match.character = '?';
    }

    return best_match;
}

int main() {
    std::ofstream fout("charrec.out");
    std::ifstream fin("charrec.in");
    std::ifstream ffont("font.in");
    
    // Read font data from font.in
    int n_font;
    ffont >> n_font;
    for (int i = 0; i < 27; ++i) {
        for (int j = 0; j < 20; ++j) {
            ffont >> font[i][j];
        }
    }

    // Read input image data from charrec.in
    fin >> n_input;
    input_lines.resize(n_input);
    for (int i = 0; i < n_input; ++i) {
        fin >> input_lines[i];
    }
    
    // DP state: dp[i] = minimum cost to recognize the first i lines of the input.
    std::vector<int> dp(n_input + 1, INF);
    std::vector<int> parent(n_input + 1, 0); // To reconstruct the path
    std::vector<char> recognized_char(n_input + 1, ' '); // To store the recognized char for each step
    dp[0] = 0;

    // Fill the DP table
    for (int i = 1; i <= n_input; ++i) {
        // Option 1: The last character was 19 lines long
        if (i >= 19) {
            MatchResult match = find_best_match(i - 19, 19);
            if (dp[i - 19] != INF && dp[i - 19] + match.cost < dp[i]) {
                dp[i] = dp[i - 19] + match.cost;
                parent[i] = i - 19;
                recognized_char[i] = match.character;
            }
        }
        // Option 2: The last character was 20 lines long
        if (i >= 20) {
            MatchResult match = find_best_match(i - 20, 20);
            if (dp[i - 20] != INF && dp[i - 20] + match.cost < dp[i]) {
                dp[i] = dp[i - 20] + match.cost;
                parent[i] = i - 20;
                recognized_char[i] = match.character;
            }
        }
        // Option 3: The last character was 21 lines long
        if (i >= 21) {
            MatchResult match = find_best_match(i - 21, 21);
            if (dp[i - 21] != INF && dp[i - 21] + match.cost < dp[i]) {
                dp[i] = dp[i - 21] + match.cost;
                parent[i] = i - 21;
                recognized_char[i] = match.character;
            }
        }
    }

    // Reconstruct the result string by backtracking through the parent pointers
    std::string result = "";
    int current = n_input;
    while (current > 0) {
        result += recognized_char[current];
        current = parent[current];
    }
    std::reverse(result.begin(), result.end());

    fout << result << std::endl;

    return 0;
}
