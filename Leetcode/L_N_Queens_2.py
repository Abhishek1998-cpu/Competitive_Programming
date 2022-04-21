# N-Queens 2

class Solution:
    def totalNQueens(self, n: int) -> int:
        self.output = 0

        def dfs(row, ex):
            if row < n:
                for col in range(n):
                    if (row, col) in ex:
                        continue
                    ex_sub = set()
                    r1 = r2 = r3 = row
                    c1 = c2 = c3 = col
                    while r1 < n:
                        r1 += 1
                        ex_sub.add((r1, c1))
                    while c2 < n:
                        c2 += 1
                        r2 += 1
                        ex_sub.add((r2, c2))
                    while c3 > 0:
                        c3 -= 1
                        r3 += 1
                        ex_sub.add((r3, c3))
                    dfs(row + 1, ex | ex_sub)
            else:
                self.output += 1
        dfs(0, set())
        return self.output


X = Solution()
print(X.totalNQueens(4))
