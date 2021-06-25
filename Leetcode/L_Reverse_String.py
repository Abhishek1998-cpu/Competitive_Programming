# Reverse String
# String Array


class Solution:
    def reverseString(self, s) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()


X = Solution()
print(X.reverseString(["h", "e", "l", "l", "o"]))
