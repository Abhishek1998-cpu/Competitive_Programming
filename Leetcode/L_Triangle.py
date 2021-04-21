# Traingle
class Solution:
    def minimumTotal(self, triangle):
        def helper(row):
            if len(row) == 1:
                return row[0]
            next_row = triangle.pop()
            for i in range(len(next_row)):
                next_row[i] += min(row[i], row[i+1])
            return helper(next_row)
        return helper(triangle.pop())


X = Solution()
print(X.minimumTotal([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]))
print(X.minimumTotal([[-10]]))
print(X.minimumTotal([[-1], [2, 3], [1, -1, -3]]))
