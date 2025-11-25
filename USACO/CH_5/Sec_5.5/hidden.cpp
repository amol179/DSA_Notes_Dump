/*
ID: amolgur1
LANG: C++
TASK: hidden
*/

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>

int main() {
    std::ifstream fin("hidden.in");
    std::ofstream fout("hidden.out");

    int l;
    fin >> l; // Read the total length

    // --- Corrected Input Logic ---
    std::string s, temp;
    fin >> s; // Read the first part of the string (up to the first newline)
    while (fin >> temp) { // Loop to read subsequent parts
        s += temp;      // and append them to the main string.
    }
    // ----------------------------

    // Double the string to easily handle cyclic shifts
    s += s;

    int i = 0; // Candidate 1
    int j = 1; // Candidate 2
    int k = 0; // Common prefix length

    while (i < l && j < l && k < l) {
        char char_i = s[i + k];
        char char_j = s[j + k];

        if (char_i == char_j) {
            k++;
        } else {
            if (char_i > char_j) {
                i = i + k + 1;
            } else {
                j = j + k + 1;
            }
            k = 0;

            if (i == j) {
                j++;
            }
        }
    }

    fout << std::min(i, j) << std::endl;

    fin.close();
    fout.close();

    return 0;
}