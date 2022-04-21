# Remove All Adjacent Duplicates in String 2
class Solution:
    def removeDuplicates(self, s, k):
        stack = []
        for c in s:
            if stack and stack[-1][0] == c and stack[-1][1] + 1 == k:
                stack.pop()
            elif stack and stack[-1][0] == c:
                stack[-1][1] += 1
            else:
                stack.append([c, 1])
        output = ""
        for i in stack:
            output += i[0] * i[1]
        return output


X = Solution()
print(X.removeDuplicates("deeedbbcccbdaa", 3))
