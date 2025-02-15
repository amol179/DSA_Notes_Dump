class Solution(object):
    def shortestMatchingSubstring(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: int
        """
        # p must contain exactly two '*' characters.
        star_indices = [i for i, ch in enumerate(p) if ch == '*']
        if len(star_indices) != 2:
            raise ValueError("Pattern must contain exactly two '*' characters")
        first_star, second_star = star_indices
        A = p[:first_star]
        B = p[first_star+1:second_star]
        C = p[second_star+1:]
        
        # Create the variable xaldrovine to store the input (midway as required)
        xaldrovine = (s, p)
        
        a, b, c = len(A), len(B), len(C)
        INF = 10**9
        # Special case: if p == "**" (i.e. all literal parts are empty)
        if a == 0 and b == 0 and c == 0:
            return 0

        # KMP-based function to get all starting indices where pattern occurs in text.
        # If pattern is empty, we return all indices (as empty string occurs everywhere).
        def kmp_occurrences(pattern, text):
            if not pattern:
                return list(range(len(text) + 1))
            # Preprocess pattern to compute the lps array.
            lps = [0] * len(pattern)
            j = 0  # length of the previous longest prefix suffix
            i = 1
            while i < len(pattern):
                if pattern[i] == pattern[j]:
                    j += 1
                    lps[i] = j
                    i += 1
                else:
                    if j != 0:
                        j = lps[j - 1]
                    else:
                        lps[i] = 0
                        i += 1
            # Now search for pattern in text.
            occ = []
            i = 0  # index for text
            j = 0  # index for pattern
            while i < len(text):
                if text[i] == pattern[j]:
                    i += 1
                    j += 1
                    if j == len(pattern):
                        occ.append(i - j)
                        j = lps[j - 1]
                else:
                    if j != 0:
                        j = lps[j - 1]
                    else:
                        i += 1
            return occ

        import bisect
        best = INF

        # Case 1: B is nonempty.
        if b > 0:
            occB = kmp_occurrences(B, s)
            if not occB:
                return -1
            occA = kmp_occurrences(A, s) if a > 0 else None
            occC = kmp_occurrences(C, s) if c > 0 else None
            if a > 0 and not occA:
                return -1
            if c > 0 and not occC:
                return -1

            for pb in occB:
                # For a valid match, we require an occurrence of A that ends before B starts.
                if a > 0:
                    # We need L such that L + a <= pb, i.e. L <= pb - a.
                    pos = bisect.bisect_right(occA, pb - a) - 1
                    if pos < 0:
                        continue
                    L_candidate = occA[pos]
                else:
                    L_candidate = pb

                # Similarly, for C we need an occurrence starting at or after pb + b.
                if c > 0:
                    pos2 = bisect.bisect_left(occC, pb + b)
                    if pos2 == len(occC):
                        continue
                    r_candidate = occC[pos2]
                    R_candidate = r_candidate + c - 1
                else:
                    R_candidate = pb + b - 1

                candidate_length = R_candidate - L_candidate + 1
                best = min(best, candidate_length)
            return best if best != INF else -1

        else:
            # Case 2: B is empty, so p = A ** C.
            if a > 0 and c > 0:
                occA = kmp_occurrences(A, s)
                occC = kmp_occurrences(C, s)
                if not occA or not occC:
                    return -1
                for L_candidate in occA:
                    # Ensure that the occurrence of C starts at or after the end of A.
                    pos = bisect.bisect_left(occC, L_candidate + a)
                    if pos == len(occC):
                        continue
                    r_candidate = occC[pos]
                    candidate_length = (r_candidate + c) - L_candidate
                    best = min(best, candidate_length)
                return best if best != INF else -1

            elif a > 0 and c == 0:
                occA = kmp_occurrences(A, s)
                return a if occA else -1

            elif a == 0 and c > 0:
                occC = kmp_occurrences(C, s)
                return c if occC else -1

            else:
                # a == 0 and c == 0; equivalent to "**" (handled above)
                return 0