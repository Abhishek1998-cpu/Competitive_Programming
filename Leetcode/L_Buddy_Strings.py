# Buddy Strings
# Important Question of String
# Asked in Google

class Solution:
    def buddyStrings(self, a: str, b: str) -> bool:
        differences = []
        len1 = len(a)
        len2 = len(b)
        if(len1 != len2):
            return False
        if(a == b and len(set(a)) < len(a)):
            return True
        for x in range(len(b)):
            if a[x] != b[x]:
                differences.append([a[x], b[x]])
        # print(differences)
        # print(differences[0])
        # print(differences[-1][::-1])
        if len(differences) == 2 and differences[0] == differences[-1][::-1]:
            return True
        return False


X = Solution()
print(X.buddyStrings("ab", "ba"))
print(X.buddyStrings("aaaaaaabc", "aaaaaaacb"))
print(X.buddyStrings("aa", "aa"))
