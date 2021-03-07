# Jewels and Stones
class Solution:
    def numJewelsInStones(self, jewels, stones):
        counter = 0
        for i in jewels:
            for j in stones:
                if(i == j):
                    counter = counter + 1
                else:
                    pass

        return counter


X = Solution()
print(X.numJewelsInStones("z", "ZZ"))
