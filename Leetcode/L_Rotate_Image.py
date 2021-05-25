# Rotate Image

class Solution:
    def rotate(self, matrix) -> None:
        n = len(matrix[0])
        for row in range(n):
            for col in range(row, n):
                matrix[col][row], matrix[row][col] = matrix[row][col], matrix[col][row]
        for i in range(n):
            matrix[i].reverse()
        """
        Do not return anything, modify matrix in-place instead.
        """


X = Solution()
print(X.rotate([[5, 1, 9, 11], [2, 4, 8, 10],
                [13, 3, 6, 7], [15, 14, 12, 16]]))
