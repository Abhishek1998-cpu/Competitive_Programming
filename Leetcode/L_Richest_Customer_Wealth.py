# Richest Customer Wealth

class Solution:
    def maximumWealth(self, accounts):
        # for i in range(0, len(accounts)):
        #     print(accounts[i])
        Max = 0
        for a in accounts:  # for traversing through the list
            # print(a)
            # print(sum(a))
            # sum(a) will sum the values of list inside list after that we will find the Max number among the parent list
            # Max value is updated after every iteration according to the condition
            Max = max(sum(a), Max)

        return Max


X = Solution()
print(X.maximumWealth([[1, 5], [7, 3], [3, 5]]))
print(X.maximumWealth([[1, 2, 3], [3, 2, 1]]))
