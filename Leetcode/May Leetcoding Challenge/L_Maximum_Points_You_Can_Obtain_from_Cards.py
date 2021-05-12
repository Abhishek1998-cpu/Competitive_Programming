import sys


class Solution:
    def maxScore(self, cardPoints, k: int) -> int:
        n = len(cardPoints)
        running_sum = 0
        left = right = 0
        min_array_sum = sys.maxsize
        for right, num in enumerate(cardPoints):
            running_sum += num
            if right - left > n-k-1:
                running_sum -= cardPoints[left]
                left += 1
            if right - left == n-k-1:
                min_array_sum = min(min_array_sum, running_sum)
        return sum(cardPoints) - min_array_sum


X = Solution()
print(X.maxScore([9, 7, 7, 9, 7, 7, 9], 7))
