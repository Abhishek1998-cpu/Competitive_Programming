# Replace All Digits with Characters
# String Array

class Solution:
    def replaceDigits(self, s: str) -> str:
        X = ""
        for i in range(0, len(s)):
            if((i % 2) != 0):
                Ans = self.shift(s[i-1], int(s[i]))
                X = X + Ans
            else:
                X = X + s[i]
        return X

    def shift(self, c, x):
        alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        indexOfc = alpha.index(c)
        c = alpha[indexOfc + x]
        return c


X = Solution()
print(X.replaceDigits("a1c1e1"))
print(X.replaceDigits("a1b2c3d4e"))
