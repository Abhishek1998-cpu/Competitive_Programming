# Sorting the Sentence
# String Sorting

class Solution:
    def sortSentence(self, s: str) -> str:
        str1 = ""
        X = list(s.split(" "))
        for i in range(0, len(X)):
            X[i] = X[i][::-1]
        X.sort()
        for i in range(0, len(X)):
            X[i] = X[i][::-1]
            X[i] = ''.join([i for i in X[i] if not i.isdigit()])
        for i in range(0, len(X) - 1):
            X[i] += " "
        for i in range(0, len(X)):
            str1 += X[i]
        return str1


X = Solution()
print(X.sortSentence("is2 sentence4 This1 a3"))
print(X.sortSentence("Myself2 Me1 I4 and3"))
