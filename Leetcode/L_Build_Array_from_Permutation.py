# Build Array from Permutation


class Solution:
    def buildArray(self, nums):
        print(nums)
        ans = []
        for i in range(0, len(nums)):
            ans.append(nums[nums[i]])
        return ans
