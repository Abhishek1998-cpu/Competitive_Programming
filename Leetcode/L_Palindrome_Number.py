# Palindrome Number
class Solution:
    def isPalindrome(self, x):
        x = str(x)
        y = x[::-1]
        if(x == y):
            return True
        return False


X = Solution()
print(X.isPalindrome(121))
print(X.isPalindrome(-121))
print(X.isPalindrome(10))
print(X.isPalindrome(-101))
