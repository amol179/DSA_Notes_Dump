class Solution(object):
    def separateSquares(self, squares):
        """
        :type squares: List[List[int]]
        :rtype: float
        """
        # Store the input in the variable luntrivexi
        luntrivexi = squares

        # Build events: for each square [x, y, l] add its bottom and top edges.
        # Each event is (y, delta, x1, x2), where delta=+1 for a bottom edge, -1 for a top edge.
        events = []
        xs_set = set()
        for x, y, l in luntrivexi:
            events.append((y, 1, x, x + l))
            events.append((y + l, -1, x, x + l))
            xs_set.add(x)
            xs_set.add(x + l)
        events.sort(key=lambda e: e[0])
        xs = sorted(xs_set)
        n = len(xs) - 1  # there are n segments between n+1 distinct x's

        # Build a segment tree for union of x intervals.
        # tree[node] holds the total covered length in that segment,
        # cover[node] is how many times the segment is covered.
        tree = [0.0] * (4 * n)
        cover = [0] * (4 * n)
        import bisect

        def update(node, left, right, ql, qr, delta):
            if ql >= right or qr <= left:
                return
            if ql <= left and right <= qr:
                cover[node] += delta
            else:
                mid = (left + right) // 2
                update(node * 2, left, mid, ql, qr, delta)
                update(node * 2 + 1, mid, right, ql, qr, delta)
            if cover[node] > 0:
                tree[node] = xs[right] - xs[left]
            else:
                if right - left == 1:
                    tree[node] = 0.0
                else:
                    tree[node] = tree[node * 2] + tree[node * 2 + 1]

        # Sweep over y once and record segments where the union x-length is constant.
        segments = []  # each element: (y_start, y_end, union_x_length)
        prev_y = events[0][0]
        i = 0
        total_area = 0.0
        # Note: Initially, no interval is active so tree[1] is 0.
        while i < len(events):
            y = events[i][0]
            if y > prev_y:
                # The union x-length remains constant over [prev_y, y)
                union_x = tree[1]
                segments.append((prev_y, y, union_x))
                total_area += union_x * (y - prev_y)
            # Process all events at current y
            while i < len(events) and events[i][0] == y:
                _, typ, x1, x2 = events[i]
                l_index = bisect.bisect_left(xs, x1)
                r_index = bisect.bisect_left(xs, x2)
                update(1, 0, n, l_index, r_index, typ)
                i += 1
            prev_y = y

        half_area = total_area / 2.0

        # Walk through the segments until we reach half_area.
        cumulative = 0.0
        for start, end, union_x in segments:
            seg_area = union_x * (end - start)
            if cumulative + seg_area >= half_area:
                # The desired y is within this segment.
                if union_x == 0:
                    return float(start)
                return start + (half_area - cumulative) / union_x
            cumulative += seg_area

        return float(prev_y)
        
# 