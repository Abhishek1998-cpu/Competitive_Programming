# Truncate Sentence
# String and Array

class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        s = list(s.split(" "))
        s = s[0:k]
        s = " ".join(s)
        return s


X = Solution()
print(X.truncateSentence("Hello how are you Contestant", 4))
print(X.truncateSentence("What is the solution to this problem", 4))
print(X.truncateSentence("chopper is not a tanuki", 5))
