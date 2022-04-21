# Non decreasing Array

class Solution:
    def checkPossibility(self, nums):
        N = len(nums)
        mx, mn = float("-inf"), float("inf")
        n, m = 0, 0
        for i in range(N):
            if nums[i] < mx:
                n += 1
            mx = max(mx, nums[i])
        for i in range(N-1, -1, -1):
            if nums[i] > mn:
                m += 1
            mn = min(mn, nums[i])
        return n <= 1 or m <= 1


X = Solution()
print(X.checkPossibility([4, 2, 3]))
