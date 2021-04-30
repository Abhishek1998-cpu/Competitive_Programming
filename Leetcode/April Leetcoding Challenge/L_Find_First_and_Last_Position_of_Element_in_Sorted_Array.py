# Find First and Last Position of Element in a Sorted Array


class Solution:
    def searchRange(self, nums, target: int):
        if target not in nums:
            return [-1, -1]
        X = nums.index(target)
        Y = len(nums) - 1 - nums[::-1].index(target)
        return [X, Y]


X = Solution()
print(X.searchRange([1], 1))
print(X.searchRange([5, 7, 7, 8, 8, 10], 6))
print(X.searchRange([5, 7, 7, 8, 8, 10], 8))
print(X.searchRange([],  0))
