# Remove Outermost Parentheses

class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        from collections import deque
        stack = deque()
        temp = ""
        arr = []
        for i in range(len(S)):
            if S[i] == "(":
                stack.append(S[i])
            else:
                stack.pop()
            temp += S[i]
            if len(stack) == 0:
                temp = temp[1:-1]
                arr.append(temp)
                temp = ""
        return "".join(arr)


X = Solution()
print(X.removeOuterParentheses("(()())(())"))
