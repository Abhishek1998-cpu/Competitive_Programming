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
