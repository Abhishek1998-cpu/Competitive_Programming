# Count Number of Pairs With Absolute Difference K
# Array

class Solution(object):
    def countKDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        counter = 0
        for i in range(0, len(nums)):
            for j in range(0, len(nums)):
                if((i < j) and (abs(nums[i] - nums[j]) == k)):
                    counter += 1
        return counter


X = Solution()
print(X.countKDifference([1, 2, 2, 1], 1))
print(X.countKDifference([1, 3], 3))
print(X.countKDifference([3, 2, 1, 5, 4], 2))
