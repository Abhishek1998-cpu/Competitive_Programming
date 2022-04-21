# So this is a solution of the Leetcode Problem "Squares of a Sorted Array"
# In this problem we just take an array, square it and sort it then return it

class Solution:
    def sortedSquares(self, nums):
        self.nums = nums
        New = []
        for i in nums:
            New.append(i*i)
        New.sort()
        return New


nums = list(map(int, input().split(" ")))
print(nums)
A = Solution()
B = A.sortedSquares(nums)
print(B)
