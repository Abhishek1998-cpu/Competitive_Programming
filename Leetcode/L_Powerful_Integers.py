# Powerful Integers
# Concepts = Math, HashMap

class Solution:
    def powerfulIntegers(self, x, y, bound):
        # This Solution exceeds time limit and will provide bad performance
        # X = []
        # for i in range(bound):
        #     for j in range(bound):
        #         if ((pow(x, i) + pow(y, j)) <= bound):
        #             X.append((pow(x, i) + pow(y, j)))

        # return list(set(sorted(X)))

        ans = []
        if y < x:
            x, y = y, x
        if x == 1 and y == 1:
            if bound >= 2:
                ans.append(2)
            return ans
        if x == 1:
            y1 = 1
            while y1 + 1 <= bound:
                ans.append(y1 + 1)
                y1 *= y
            return ans
        s = set()
        x1 = 1
        while x1 <= bound:
            y1 = 1
            while x1 + y1 <= bound:
                s.add(x1 + y1)
                y1 *= y
            x1 *= x
        return list(s)


X = Solution()
print(X.powerfulIntegers(2, 3, 10))
print(X.powerfulIntegers(3, 5, 15))
print(X.powerfulIntegers(81, 21, 900000))
