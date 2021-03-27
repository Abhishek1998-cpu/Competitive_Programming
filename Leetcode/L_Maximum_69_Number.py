# Maximum 69 Number
class Solution:
    def maximum69Number(self, num):
        return int(str(num).replace("6", "9", 1))


X = Solution()
print(X.maximum69Number(9996))
print(X.maximum69Number(9669))
