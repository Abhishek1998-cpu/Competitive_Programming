# Third Maximum Number

class Solution:
    def thirdMax(self, nums) -> int:
        if(len(nums) < 3):
            return max(nums)
        nums = list(set(nums))
        nums = sorted(nums, reverse=True)
        if(len(nums) < 3):
            return max(nums)
        return nums[2]


X = Solution()
print(X.thirdMax([2, 2, 3, 1]))
print(X.thirdMax([1, 2]))
print(X.thirdMax([3, 2, 1]))
