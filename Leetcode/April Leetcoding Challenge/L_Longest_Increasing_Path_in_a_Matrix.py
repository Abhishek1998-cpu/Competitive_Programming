# Longest Increasing path in a Matrix

class Solution:
    def longestIncreasingPath(self, matrix):
        if not matrix:
            return 0
        m, n = len(matrix), len(matrix[0])
        memo = [[0]*n for _ in range(m)]

        def longest_path(i, j):
            if not memo[i][j]:
                adj_paths = []
                for x, y in ((i, j-1), (i-1, j), (i, j+1), (i+1, j)):
                    if 0 <= x < m and 0 <= y < n and matrix[x][y] > matrix[i][j]:
                        adj_paths.append(longest_path(x, y))
                memo[i][j] = 1 + max(adj_paths, default=0)
            return memo[i][j]
        return max(longest_path(i, j) for i in range(m) for j in range(n))


X = Solution()
print(X.longestIncreasingPath([[3, 4, 5], [3, 2, 6], [2, 2, 1]]))
