# Buddy Strings

class Solution:
    def buddyStrings(self, a: str, b: str) -> bool:
        len1 = len(a)
        len2 = len(b)
        if(len1 != len2):
            return False
        prev = -1
        curr = -1
        count = 0
        i = 0
        while i < len1:
            if(a[i] != b[i]):
                count = count + 1
                if(count > 2):
                    return False
                prev = curr
                curr = i
            i = i + 1
        return (count == 2 and a[prev] == b[curr] and a[curr] == b[prev])


X = Solution()
print(X.buddyStrings("ab", "ba"))
print(X.buddyStrings("aaaaaaabc", "aaaaaaacb"))
