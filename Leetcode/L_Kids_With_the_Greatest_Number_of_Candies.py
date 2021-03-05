# Kids With the Greatest Number of Candies
class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        Max = max(candies)
        candies2 = []
        candies3 = []
        for i in range(0, len(candies)):
            candies2.append(candies[i] + extraCandies)
        for i in range(0, len(candies2)):
            if(candies2[i] >= Max):
                candies3.append(True)
            else:
                candies3.append(False)
        return candies3


A = Solution()
print(A.kidsWithCandies([4, 2, 1, 1, 2], 1))
