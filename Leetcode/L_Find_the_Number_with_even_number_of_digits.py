# Find the Numbers with Even Number of Digits

class Solution:
    def findNumbers(self, nums):
        counter = 0
        for i in nums:
            if(len(str(i)) % 2 == 0):
                counter = counter + 1
        return counter


X = Solution()
print(X.findNumbers([12, 345, 2, 6, 7896]))
