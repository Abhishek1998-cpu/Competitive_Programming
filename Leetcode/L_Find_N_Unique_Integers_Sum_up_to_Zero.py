# Find N Unique integers Sum up to Zero

class Solution:
    def sumZero(self, n):
        X = []
        if(n % 2 == 0):
            for i in range(1, (n//2)+1):
                X.append(i)
                X.append(-(i))
        else:
            for i in range(1, (n//2)+1):
                X.append(i)
                X.append(-(i))
            X.append(0)
        return X

        # return n


X = Solution()
print(X.sumZero(1))
