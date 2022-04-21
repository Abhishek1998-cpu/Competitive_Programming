# Merge String Alternatively

class Solution:
    def mergeAlternately(self, word1, word2):
        w1 = collections.deque(word1)
        w2 = collections.deque(word2)
        ans = []
        while len(w1) > 0 and len(w2) > 0:
            ans.append(w1.popleft())
            ans.append(w2.popleft())
        while len(w1) > 0:
            ans.append(w1.popleft())
        while len(w2) > 0:
            ans.append(w2.popleft())
        return "".join(ans)


X = Solution()
print(X.mergeAlternately("abc", "pqr"))
