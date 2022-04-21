# Determine if string halves are alike

class Solution:
    def halvesAreAlike(self, s):
        n = len(s)
        a = s[0:n//2]
        b = s[n//2:n]
        counter1 = 0
        counter2 = 0
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        for i in a:
            if i in vowels:
                counter1 += 1
        for i in b:
            if i in vowels:
                counter2 += 1
        if counter1 == counter2:
            return True
        else:
            return False


X = Solution()
print(X.halvesAreAlike("book"))
print(X.halvesAreAlike("textbook"))
print(X.halvesAreAlike("MerryChristmas"))
print(X.halvesAreAlike("AbCdEfGh"))
