# Monotonic Array
# Array

class Solution:
    def isMonotonic(self, nums):
        # print(nums)
        incFlag = False
        decFlag = False
        for i in range(1, len(nums)):
            if(nums[i] > nums[i - 1]):
                if(decFlag):
                    return False
                incFlag = True
            if(nums[i-1] > nums[i]):
                if(incFlag):
                    return False
                decFlag = True
        return True


X = Solution()
print(X.isMonotonic([1, 2, 2, 3]))
print(X.isMonotonic([6, 5, 4, 4]))
print(X.isMonotonic([1, 3, 2]))
