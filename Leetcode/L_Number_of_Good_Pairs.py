# Number of Good Pairs
class Solution:
    def numIdenticalPairs(self, nums):
        counter = 0
        for i in range(0, len(nums)):
            for j in range(0, len(nums)):
                if(i < j):
                    if(nums[i] == nums[j]):
                        counter = counter + 1
                    else:
                        pass
                else:
                    pass

        return counter


X = Solution()
print(X.numIdenticalPairs([1, 2, 3]))
