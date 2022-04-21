# Minimum Operations to Make Array Equal
class Solution:
    def minOperations(self, n):
        Arr = []
        for i in range(0, n):
            Arr.append((2*i) + 1)
        Avg = sum(Arr) // n
        count = 0
        for x in range(n):
            count += abs(Arr[x] - Avg)
        return count//2


X = Solution()
print(X.minOperations(3))
print(X.minOperations(6))
