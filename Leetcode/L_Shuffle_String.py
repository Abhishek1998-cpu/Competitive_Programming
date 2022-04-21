# Shuffle String
class Solution:
    def restoreString(self, s, indices):
        N = len(s)
        a = [""]*N
        for i, x in enumerate(indices):
            a[x] = s[i]
        return "".join(a)


X = Solution()
print(X.restoreString("codeleet", [4, 5, 6, 7, 0, 2, 1, 3]))
