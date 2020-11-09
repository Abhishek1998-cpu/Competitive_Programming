# My Solution of the leetcode Detect capital problem

X = input()
if(X.isupper() == True):
    print("True")
elif(X.islower() == True):
    print("True")
elif(X.istitle() == True):
    print("True")
else:
    print("False")


# Accepted Solution of the leetcode Detect capital problem

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word) < 2:
            return True
        if word[0].isupper() and word[1].isupper():
            for i in range(2, len(word)):
                if word[i].islower():
                    return False
        else:
            for i in range(1, len(word)):
                if word[i].isupper():
                    return False
        return True
