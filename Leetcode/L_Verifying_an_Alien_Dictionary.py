# Verifying an Alien Dictionary


class Solution:
    def isAlienSorted(self, words, order):
        dict = {}
        for x, y in enumerate(order):
            dict[y] = x
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i+1]
            for i in range(min(len(word1), len(word2))):
                if word1[i] != word2[i]:
                    if dict[word1[i]] > dict[word2[i]]:
                        return False
                    break
            else:
                if len(word1) > len(word2):
                    return False
        return True


X = Solution()
print(X.isAlienSorted(["hello", "leetcode"],  "hlabcdefgijkmnopqrstuvwxyz"))
print(X.isAlienSorted(["word", "world", "row"],  "worldabcefghijkmnpqstuvxyz"))
