# Count the Number of Consistent Strings
class Solution:
    def countConsistentStrings(self, allowed, words):
        X = set(list(map(str, allowed)))
        counter = 0
        for i in words:
            Y = set(list(map(str, i)))
            if (Y.issubset(X)):
                counter = counter+1
        return counter


X = Solution()
# print(X.countConsistentStrings(
#     "abc", ["a", "b", "c", "ab", "ac", "bc", "abc"]))
# print(X.countConsistentStrings(
#     "abc", ["a", "b", "c", "ab", "ac", "bc", "abc"]))
print(X.countConsistentStrings(
    "ab", ["ad", "bd", "aaab", "baa", "badab"]))
