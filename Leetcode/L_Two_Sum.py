# Two Sum

class Solution:
    def twoSum(self, nums, target):
        Y = {}
        X = enumerate(nums)
        # print(list(X))
        for i, j in X:
            if target - j in Y:
                return [Y[target - j], i]
            Y[j] = i


X = Solution()
print(X.twoSum([2, 7, 11, 15], 9))
print(X.twoSum([3, 2, 4], 6))
print(X.twoSum([3, 3], 6))
print(X.twoSum([3, 2, 3], 6))
