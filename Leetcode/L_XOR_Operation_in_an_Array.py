# XOR Operation in Array
class Solution:
    def xorOperation(self, n, start):
        counter = 0
        nums = []
        for i in range(0, n):
            # print(i)
            nums.append(start + 2*i)
        for i in range(0, n):
            counter = counter ^ nums[i]
        return counter


X = Solution()
print(X.xorOperation(10, 5))
