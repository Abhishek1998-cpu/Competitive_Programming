# Check if two Strings Arrays are Equivalent or not
# Leetcode
# Day 8 - January Leetcoding Challenge

class Solution:
    def arrayStringsAreEqual(self, word1: [str], word2: [str]) -> bool:
        word = ""
        text = ""
        for i in range(0, len(word1)):
            word += word1[i]
        for j in range(0, len(word2)):
            text += word2[j]
        if (word == text):
            Ans = True
        else:
            Ans = False

        return Ans


A = list(input().split(" "))
B = list(input().split(" "))
# print(A)
# print(B)
X = Solution()
print(X.arrayStringsAreEqual(A, B))
