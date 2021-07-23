#: https://leetcode.com/problems/max-points-on-a-line/

def maxPoints(points):
    p_len = len(points)
    if p_len <= 2:
        return p_len
    res = 0
    for i in range(p_len - 1):
        curr, overlap, lines = 0, 0, {}
        for j in range(i + 1, p_len):
            dx, dy = points[i][0] - points[j][0], points[i][1] - points[j][1]
            if dx == dy == 0:
                overlap += 1
                continue
            key = None if dx == 0 else 10.0 * dy / dx
            lines[key] = lines.get(key, 0) + 1
            curr = max(curr, lines[key])
        res = max(res, curr + overlap)
    return res + 1