# Split a String in Balanced Strings
class Solution:
    def balancedStringSplit(self, s):
        left = 0
        right = 0
        out = 0
        if len(s) == 1:
            return 0
        for char in s:
            if (char == "L"):
                left += 1
            else:
                right += 1
            if left == right:
                out += 1
        return out


X = Solution()
print(X.balancedStringSplit("LLLLRRRR"))
