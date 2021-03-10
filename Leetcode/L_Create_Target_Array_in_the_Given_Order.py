# Create Target Array in the Given Order
class Solution:
    def createTargetArray(self, nums, index):
        new = tuple(zip(index, nums))
        # print(new)
        r = []
        for i, j in new:
            # print(i,j)
            r.insert(i, j)
        return r


X = Solution()
print(X.createTargetArray([0, 1, 2, 3, 4], [0, 1, 2, 2, 1]))
