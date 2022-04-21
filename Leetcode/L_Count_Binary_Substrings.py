# Count Binary SubStrings

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        ans = 0
        preCnt = 0
        n = len(s)
        i = 0
        while i < n:
            curCnt = 1
            while i < n-1 and s[i] == s[i+1]:
                curCnt += 1
                i += 1

            if preCnt > 0:
                ans += min(preCnt, curCnt)
            preCnt = curCnt
            i += 1
        return ans


X = Solution()
print(X.countBinarySubstrings("00110011"))
print(X.countBinarySubstrings("10101"))
