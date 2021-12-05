# Maximum Number of Coins You Can Get
# Array Math Greedy Sorting

class Solution:
    def maxCoins(self, piles) -> int:
        piles = sorted(piles)
        start = len(piles) // 3
        ans = 0

        while start < len(piles):
            ans += piles[start]
            start += 2

        return ans


X = Solution()
print(X.maxCoins([2, 4, 1, 2, 7, 8]))
