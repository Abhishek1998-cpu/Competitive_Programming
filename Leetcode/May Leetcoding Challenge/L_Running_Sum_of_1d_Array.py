# Running Sum of 1d Array

class Solution:
    def runningSum(self, nums):
        Y = 0
        X = []
        for i in nums:
            Y = Y + i
            X.append(Y)

        # print(nums)
        return X


X = Solution()
print(X.runningSum([1, 2, 3, 4]))
