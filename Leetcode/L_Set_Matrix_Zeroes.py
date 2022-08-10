class Solution:

    def setMatrixZeroes(self, row, col, matrix):
        for i in range(0, len(matrix)):
            matrix[i][col] = 0
        for i in range(0, len(matrix[0])):
            matrix[row][i] = 0

    def setZeroes(self, matrix):
        zeroes = []
        for i in range(0, len(matrix)):
            print("Hello World")
            for j in range(0, len(matrix[i])):
                if(matrix[i][j] == 0):
                    zeroes.append([i, j])

        for i in range(0, len(zeroes)):
            row = zeroes[i][0]
            col = zeroes[i][1]
            self.setMatrixZeroes(row, col, matrix)
        return matrix


Obj1 = Solution()
print(Obj1.setZeroes([[1, 1, 1], [1, 0, 1], [1, 1, 1]]))
