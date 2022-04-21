# https://www.geeksforgeeks.org/sum-of-all-odd-length-subarrays/

# Sum of All Odd Length Subarrays
class Solution:
    def sumOddLengthSubarrays(self, arr):
        sum = 0
        l = len(arr)

        for i in range(l):
            for j in range(i, l, 2):
                for k in range(i, j+1, 1):
                    sum += arr[k]
        return sum


X = Solution()
print(X.sumOddLengthSubarrays([1, 4, 2, 5, 3]))
