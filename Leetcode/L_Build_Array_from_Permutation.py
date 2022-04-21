# Build Array from Permutation

# Solution 1
# class Solution:
#     def buildArray(self, nums):
#         print(nums)
#         ans = []
#         for i in range(0, len(nums)):
#             ans.append(nums[nums[i]])
#         return ans


# Solution 2
class Solution:
    def buildArray(self, nums):
        arr = [nums[x] for x in nums]
        return arr
