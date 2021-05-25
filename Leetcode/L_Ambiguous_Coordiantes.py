# Ambiguous Coordinates


class Solution:
    def ambiguousCoordinates(self, s: str):
        s = s[1:-1]
        N = len(s)
        output = []

        def unpack(x):
            tmp = []
            N = len(x)
            if x[0] != "0" or x == "0":
                tmp.append(x)
            for i in range(1, N):
                if (x[:i] == "0" or x[0] != "0") and x[-1] != "0":
                    cand = x[:i]+"."+x[i:]
                    tmp.append(cand)
            return tmp
        for i in range(1, N):
            a = s[:i]
            b = s[i:]
            for first in unpack(a):
                for second in unpack(b):
                    output.append("({}, {})".format(first, second))
        return output


X = Solution()
print(X.ambiguousCoordinates("(123)"
                             ))
