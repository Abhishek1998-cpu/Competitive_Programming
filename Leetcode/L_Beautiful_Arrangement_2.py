# Beautiful Arrangement 2

class Solution:
    def constructArray(self, n, k):
        r = []
        for x in range(n - k):
            r.append(x+1)
        front = n - k + 1
        back = n
        while len(r) < n:
            r.append(back)
            back -= 1
            if len(r) < n:
                r.append(front)
                front += 1
        return r


X = Solution()
print(X.constructArray(3, 1))
