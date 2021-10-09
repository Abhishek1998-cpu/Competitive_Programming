# Find Center of the Star Graph
# Array Graph

class Solution:
    def findCenter(self, edges) -> int:
        E1, E2 = edges[0], edges[1]
        e1E1, e2E1, e1E2, e2E2 = E1[0], E1[1], E2[0], E2[1]
        if(e1E1 == e1E2 or e1E1 == e2E2):
            ans = e1E1
        if(e2E1 == e1E2 or e2E1 == e2E2):
            ans = e2E1
        return ans


X = Solution()
print(X.findCenter([[1, 2], [2, 3], [4, 2]]))
print(X.findCenter([[1, 2], [5, 1], [1, 3], [1, 4]]))
