# Problem -> How many number are smaller than the current number
class Solution:
    def smallerNumbersThanCurrent(self, nums):

        nums2 = []
        for i in range(0, len(nums)):
            counter = 0
            for j in range(0, len(nums)):
                if(nums[i] > nums[j]):
                    counter = counter + 1
                else:
                    pass
            nums2.append(counter)
        return nums2


X = Solution()
print(X.smallerNumbersThanCurrent([7, 7, 7, 7]))
