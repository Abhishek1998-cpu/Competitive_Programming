# Maximum Product Difference Between Two Pairs
# Array Sorting

class Solution:
    def maxProductDifference(self, nums) -> int:
        nums.sort()
        X = len(nums)
        ans = (nums[X-1]*nums[X-2])-(nums[0]*nums[1])
        return ans


X = Solution()
print(X.maxProductDifference([5, 6, 2, 7, 4]))
print(X.maxProductDifference([4, 2, 5, 9, 7, 4, 8]))
