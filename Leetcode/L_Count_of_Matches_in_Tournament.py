# Count of Matches in a Tournament
# Backtracking

# Solution 1:
# class Solution:
#     def numberOfMatches(self, n: int) -> int:
#         return n-1

#  Solution 2:
class Solution:
    def numberOfMatches(self, n):
        ans = 0
        while(n != 1):
            if(n % 2 == 0):
                ans += n//2
                n = n//2
            else:
                ans += (n-1)//2
                n = (n-1)//2 + 1
        return ans


X = Solution()
print(X.numberOfMatches(7))
