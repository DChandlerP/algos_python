# https://leetcode.com/problems/spiral-matrix/

def spiralTraverse(matrix):
    m = len(matrix)
    n = len(matrix[0])
    i, j, di, dj = 0, 0, 0, 1
    res = []
    for _ in range(m * n):
        res.append(matrix[i][j])
        matrix[i][j] = None
        if matrix[(i + di) % m][(j + dj) % n] == None:
            di, dj = dj, -di
        i += di
        j += dj
    return res