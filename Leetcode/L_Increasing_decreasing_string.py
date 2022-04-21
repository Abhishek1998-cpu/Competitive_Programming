# Increasing Decreasing String
# Important Questions asked in Geekster Admission Assessment
class Solution:
    def sortString(self, s):
        self.s = s
        d = {}
        tot = len(s)
        for i in s:
            if i not in d:
                d[i] = 1
                print(d[i])
            else:
                d[i] += 1
                # print(d[i])
        res = ""
        t = sorted(list(set(s)))
        print(t)
        while tot > 0:
            for j in range(len(t)):
                if d[t[j]] > 0:
                    res += t[j]
                    tot -= 1
                    d[t[j]] -= 1
                    if tot == 0:
                        break
            for j in range(len(t) - 1, -1, -1):
                if d[t[j]] > 0:
                    res += t[j]
                    tot -= 1
                    d[t[j]] -= 1
                    if tot == 0:
                        break
        return res


X = Solution()
print(X.sortString("rat"))
print(X.sortString("aaaabbbbcccc"))
