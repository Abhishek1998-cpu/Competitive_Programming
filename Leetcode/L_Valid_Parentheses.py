# Valid Parentheses

class Solution:
    def isValid(self, s):
        X = []
        Y = {")": "(", "}": "{", "]": "["}
        for i in s:
            if i in Y.values():
                X.append(i)
            elif X and Y[i] == X[-1]:
                X.pop()
            else:
                return False

        return X == []


X = Solution()
print(X.isValid("()"))
print(X.isValid("()[]{}"))
print(X.isValid("(]"))
print(X.isValid("(([)]"))
print(X.isValid("{[]}"))

# X = {"(": ")", "{": "}", "[": "]", "A": "B"}
# print(X.values()) It will print all different values of the Dictionary.
# "Key": "Values"
# X.values() will return the list having all different Values
