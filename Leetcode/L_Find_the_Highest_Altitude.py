# Find the Highest Altitude
class Solution:
    def largestAltitude(self, gain):
        current = 0
        highest = 0
        for x in gain:
            current += x
            highest = max(current, highest)
        return highest


X = Solution()
print(X.largestAltitude([-5, 1, 5, 0, -7]))
