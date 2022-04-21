# Find and Replace Pattern

class Solution:
    def findAndReplacePattern(self, words, pattern: str):
        def check(s, p):
            m1, m2 = {}, {}
            for a, b in zip(s, p):
                if a not in m1:
                    m1[a] = b
                if b not in m2:
                    m2[b] = a
                if a != m2[b] or b != m1[a]:
                    return False
            return True
        output = []
        for word in words:
            if check(word, pattern):
                output.append(word)
        return output


X = Solution()
print(X.findAndReplacePattern(
    ["abc", "deq", "mee", "aqq", "dkd", "ccc"], "abb"))
