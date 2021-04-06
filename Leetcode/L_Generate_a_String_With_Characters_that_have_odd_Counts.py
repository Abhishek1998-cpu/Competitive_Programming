# Generate a string with characters that have odd counts

class Solution:
    def generateTheString(self, n):
        s = ""
        if((n % 2) == 0):
            for i in range(0, n-1):
                s += "a"
            s += "b"
            # print(s)
        else:
            for i in range(0, n):
                s += "a"
        return s


X = Solution()
print(X.generateTheString(7))
print(X.generateTheString(2))
print(X.generateTheString(4))
