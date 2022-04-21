# Roman to Integer

class Solution:
    def romanToInt(self, s):
        Map = {"I": 1,
               "V": 5,
               "X": 10,
               "L": 50,
               "C": 100,
               "D": 500,
               "M": 1000}
        N = len(s)
        i = N-1
        output = 0
        while i >= 0:
            if i < N-1 and Map[s[i]] < Map[s[i+1]]:
                output -= Map[s[i]]
            else:
                output += Map[s[i]]
            i = i - 1
        return output


X = Solution()
print(X.romanToInt("III"))
print(X.romanToInt("LVIII"))
print(X.romanToInt("IX"))
