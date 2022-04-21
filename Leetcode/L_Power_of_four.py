class Solution:
    def isPowerOfFour(self, n):
        if (n == 0):
            return False
        while (n != 1):
            if (n % 4 != 0):
                return False
            n = n // 4  # the floor division // rounds the result down to the nearest whole number

        return True


X = Solution()
print(X.isPowerOfFour(20))

# This is solution of the problem Power of four from Leetcode
