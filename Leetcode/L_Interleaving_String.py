# Interleaving String
# Topics - String, Dynamic Programming


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        N = len(s3)
        A, B = len(s1), len(s2)
        if A+B != N:
            return False
        dp = [False]*(B + 1)
        for i in range(A + 1):
            for j in range(B + 1):
                if i == 0 and j == 0:
                    dp[j] = True
                elif i == 0:
                    dp[j] = dp[j-1] and s2[j-1] == s3[i + j - 1]
                elif j == 0:
                    dp[j] = dp[j] and s1[i - 1] == s3[i + j - 1]
                else:
                    dp[j] = (dp[j - 1] and s2[j - 1] == s3[i + j - 1]
                             ) or (dp[j] and s1[i - 1] == s3[i + j - 1])
        return dp[-1]


X = Solution()
print(X.isInterleave("aabcc", "dbbca", "aadbbcbcac"))
