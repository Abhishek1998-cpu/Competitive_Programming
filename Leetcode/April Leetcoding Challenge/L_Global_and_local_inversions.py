# Global and Local Inversions
class Solution:
    def isIdealPermutation(self, A):
        N = len(A)
        for i in range(N):
            if abs(i-A[i]) > 1:
                return False
        return True


X = Solution()
print(X.isIdealPermutation([1, 2, 0]))
