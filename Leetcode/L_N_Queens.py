# N - Queens
# BackTracking

from collections import defaultdict


class Solution:
    def solveNQueens(self, n: int):
        # def backTrack(i):
        #     if i == n:
        #         ans.append(["".join(row) for row in board])
        #         return
        #     for j in range(n):
        #         if not cols[j] and not diagonals[i + j] and not antiDiagonals[i - j]:
        #             board[i][j] = "Q"
        #             cols[j] = True
        #             diagonals[i + j] = True
        #             antiDiagonals[i + j] = True

        #             backTrack(i + 1)
        #             board[i][j] = "."
        #             cols[j] = False
        #             diagonals[i + j] = False
        #             antiDiagonals[i - j] = False

        # cols = [False] * n
        # diagonals = defaultdict(bool)
        # antiDiagonals = defaultdict(bool)
        # ans = []
        # board = [["."] * n for _ in range(n)]
        # backTrack(0)
        # return ans
        output = []

        def backtracking(queens=[]):
            if len(queens) == n:
                temp = []
                for queen in queens:
                    temp.append("." * queen + "Q" + "." * (n - 1 - queen))
                output.append(temp)
                return
            for queen in getPositions(queens):
                backtracking(queens + [queen])

        def getPositions(queens):
            exclude = set()
            rows = len(queens)
            for row in range(rows):
                queen = queens[row]
                exclude.add(queen)
                exclude.add(queen + rows - row)
                exclude.add(queen - rows + row)
            return set(range(n)) - exclude

        backtracking()
        return output
