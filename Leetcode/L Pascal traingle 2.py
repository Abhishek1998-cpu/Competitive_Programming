class Solution:
    def getRow(self, rowIndex: int):
        result = [1]*(rowIndex + 1)
        for i in range(1, rowIndex):
            for j in range(i, 0, -1):
                result[j] += result[j-1]
        return result
        
        
N = Solution()
print(N.getRow(3))

# This is the solution of the problem Pascal traingle 2 of Leetcode 
