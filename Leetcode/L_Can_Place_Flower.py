# Can Place Flower
class Solution:
    def canPlaceFlowers(self, flowerbed, n: int) -> bool:
        total = 0
        N = len(flowerbed)
        for i in range(N):
            # print(i)
            if i - 1 >= 0 and flowerbed[i - 1] == 1:
                continue
            if flowerbed[i] == 1:
                continue
            if i + 1 < N and flowerbed[i + 1] == 1:
                continue
            flowerbed[i] = 1
            total += 1
        return total >= n


X = Solution()
print(X.canPlaceFlowers([1, 0, 0, 0, 1], 1))
