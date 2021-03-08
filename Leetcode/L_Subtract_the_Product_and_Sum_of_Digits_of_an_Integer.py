# Subtract the Product and Sum of Digits of an Integer
class Solution:
    def subtractProductAndSum(self, n):
        Y = str(n)
        X = len(str(n))
        Sum = 0
        Mul = 1
        i = 0
        while i < X:
            Sum += int(Y[i])
            Mul *= int(Y[i])
            i += 1
        return Mul - Sum


X = Solution()
print(X.subtractProductAndSum(4421))
