# Check if one string swap can make strings equal

# Approach: First omit the elements which are the same and have the same index in both the strings. Then if the new strings are of length two and both the elements in each string are the same then only the swap is possible.
from collections import Counter


class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        # print(len(s1))
        # if(s1 == s2):
        #     return True
        # s = " "
        # for i in range(0, len(s1)):
        #     print(s1[i])
        # if (s1[i] == s2[i]):
        #     # s1[i] = s
        #     # s2[i] = s
        # s1 = s1.replace(s1[i], s)
        # s2 = s2.replace(s2[i], s)
        # print(S1)
        # print(S2)

        # print(s1)
        # S1 = s1.replace(" ", "")
        # S2 = s2.replace(" ", "")
        # print(S1)
        # print(S2)
        # print(set(S1) == set(S2))
        # if(len(S1) and len(S2) == 2):
        #     if ((S1) == (S2)):
        #         return True
        #     return False
        # return False

        if Counter(s1) != Counter(s2):
            return False
        if s1 == s2:
            return True
        diff = 0
        for x, y in zip(s1, s2):
            if x != y:
                diff += 1
        return diff == 2


X = Solution()
print(X.areAlmostEqual("bank", "kanb"))
print(X.areAlmostEqual("attack", "defend"))
print(X.areAlmostEqual("kelb", "kelb"))
print(X.areAlmostEqual("abcd", "dcba"))
print(X.areAlmostEqual("siyolsdcjthwsiplccjbuceoxmpjgrauocx",
                       "siyolsdcjthwsiplccpbuceoxmjjgrauocx"))
