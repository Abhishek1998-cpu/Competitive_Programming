# Both the solution are using the same approach
# Solution 1 - Simple without OOP
# X = list(map(int, input().split(" ")))
# Y = len(X)
# Z = []  # New list for Output
# a = 0
# for i in X:
#     a = i + a
#     Z.append(a)
# print(Z)


# Accepted Solution -- We have to use OOP for providing acceptance
class Solution:
    def runningSum(self, nums):
        Z = []  # New list for Output
        a = 0
        for i in nums:
            a = i + a
            Z.append(a)
        return(Z)
