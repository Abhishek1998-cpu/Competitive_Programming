# Letter combination of a Phone Number

# a = ["A", 'B', "C"]
# b = ["X", "Y", "Z"]
# X = []
# for i in range(0, len(a)):
#     for j in range(0, len(b)):
#         Y = a[i] + b[j]
#         X.append(Y)
# print(X)


class Solution:
    def letterCombinations(self, digits):
        res = []
        digitToChar = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
                       "6": "mno", "7": "qprs", "8": "tuv", "9": "wxyz"}

        def backtrack(i, curStr):
            if len(curStr) == len(digits):
                res.append(curStr)
                return
            for c in digitToChar[digits[i]]:
                backtrack(i + 1, curStr + c)
        if digits:
            backtrack(0, "")
        return res


X = Solution()
print(X.letterCombinations("23"))
