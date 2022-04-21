# Longest Valid Parenthesis

class Solution:
    def longestValidParentheses(self, s):
        dp = [0 for x in s]
        for i in range(len(s)):
            if s[i] == "(":
                pass
            if s[i] == ")":
                if i-1 < 0:
                    continue
                if s[i-1] == "(":
                    dp[i] = dp[i-2]+2
                    continue
                if i-dp[i-1]-1 < 0:
                    continue
                if s[i-dp[i-1]-1] == "(":
                    dp[i] = dp[i-1] + 2 + dp[i-dp[i-1]-2]
        if len(dp) == 0:
            return 0
        return max(dp)


X = Solution()
print(X.longestValidParentheses("(()"))
