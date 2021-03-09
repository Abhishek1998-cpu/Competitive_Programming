# Decompress Run-Length Encoded List
class Solution:
    def decompressRLElist(self, nums):
        X = []
        i = 0
        while(i < len(nums)):
            for j in range(nums[i]):
                j = j  # No use
                X.append(nums[i+1])
            i += 2
        return X


A = Solution()
print(A.decompressRLElist([1, 2, 3, 4]))
