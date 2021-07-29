# Concatenation of Array
# Array

class Solution:
    def getConcatenation(self, nums):
        for i in range(0, len(nums)):
            nums.append(nums[i])
        return nums


X = Solution()
print(X.getConcatenation([1, 2, 1]))
print(X.getConcatenation([1, 3, 2, 1]))
