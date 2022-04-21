# Ones and Zeroes

class Solution:
    def findMaxForm(self, strs, m, n):
        ans = [[0 for j in range(m+1)] for i in range(n+1)]
        for s in strs:
            ones = s.count("1")
            zeroes = s.count("0")
            for i in range(n, ones-1, -1):
                for j in range(m, zeroes-1, -1):
                    ans[i][j] = max(ans[i][j], ans[i-ones][j-zeroes] + 1)
        return ans[n][m]


X = Solution()
print(X.findMaxForm(["10", "0", "1"], 1, 1))
