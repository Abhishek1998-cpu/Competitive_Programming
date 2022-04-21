# Number of Different Integers in a String
# String

class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        X = []
        for i in word:
            if((i.isalpha()) == True):
                word = word.replace(i, " ")
        word = word.split()
        for i in word:
            X.append(i.lstrip("0"))
        X = list(set(X))
        return len(X)


X = Solution()
print(X.numDifferentIntegers("a123bc34d8ef34"))
print(X.numDifferentIntegers("leet1234code234"))
print(X.numDifferentIntegers("a1b01c001"))
