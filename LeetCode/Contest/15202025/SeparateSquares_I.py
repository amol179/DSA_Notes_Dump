class Solution(object):
    def separateSquares(self, squares):
        """
        :type squares: List[List[int]]
        :rtype: float
        """
        # Calculate total area of all squares (each square's area is l^2)
        total_area = sum(l * l for _, y, l in squares)
        target = total_area / 2.0

        # Determine the search range for the horizontal line.
        lo = 0.0
        hi = max(y + l for _, y, l in squares)
        
        # Helper function to compute total area above line y = L.
        def area_above(L):
            total = 0.0
            for _, y, l in squares:
                if L <= y:
                    # Entire square is above the line.
                    total += l * l
                elif L >= y + l:
                    # Entire square is below the line.
                    total += 0.0
                else:
                    # Line cuts the square: only the upper part is above.
                    total += l * (y + l - L)
            return total
        
        # Use binary search to find the minimum y-coordinate L
        # such that area above L equals half of total_area.
        for _ in range(60):  # 60 iterations gives precision within 1e-5.
            mid = (lo + hi) / 2.0
            if area_above(mid) > target:
                # Too much area above the line means L is too low.
                lo = mid
            else:
                hi = mid
        
        return hi