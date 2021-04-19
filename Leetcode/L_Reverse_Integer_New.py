# Reverse Integer New
class Solution:
    def reverse(self, x: int) -> int:
        if(x < 0):
            x = -(x)
            y = 0
            while(x > 0):
                z = x % 10
                y = y * 10 + z
                x = x // 10
            if(-(y) < -2147483648):
                return 0
            else:
                return -(y)
        else:
            y = 0
            while(x > 0):
                z = x % 10
                y = y * 10 + z
                x = x // 10
            if((y) > 2147483647):
                return 0
            else:
                return (y)


X = Solution()
# print(X.reverse(564))
# print(X.reverse(-123))
print(X.reverse(1534236469))
