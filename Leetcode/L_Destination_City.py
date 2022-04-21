# Destination City


class Solution:
    def destCity(self, paths):
        start = set([path[0] for path in paths])
        end = set([path[1] for path in paths])
        return list((end - start))[0]


X = Solution()
print(X.destCity([["London", "New York"], [
      "New York", "Lima"], ["Lima", "Sao Paulo"]]))
