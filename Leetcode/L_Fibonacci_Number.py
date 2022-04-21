# Fibonacci Number

class Solution:
    def fib(self, n):
        self.n = n
        X = 0
        Y = 1
        Arr = [0, 1]
        for i in range(0, n):
            Z = X + Y
            Arr.append(Z)
            X = Y
            Y = Z
        return Arr[n]


X = Solution()
print(X.fib(4))
