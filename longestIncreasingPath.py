def longestIncreasingPath(matrix):
    if not matrix or not matrix[0]:
        return 0

    rows, cols = len(matrix), len(matrix[0])
    dp = [[-1] * cols for _ in range(rows)]

    def dfs(r, c):
        if dp[r][c] != -1:
            return dp[r][c]

        max_len = 1
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] > matrix[r][c]:
                max_len = max(max_len, 1 + dfs(nr, nc))

        dp[r][c] = max_len
        return dp[r][c]

    return max(dfs(r, c) for r in range(rows) for c in range(cols))
