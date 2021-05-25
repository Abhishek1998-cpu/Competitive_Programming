# Super Palindrome

import math


class Solution:
    def superpalindromesInRange(self, left: str, right: str) -> int:
        # X = []
        # for i in range(int(left), int(right) + 1):
        #     i = str(i)
        #     if (i == i[::-1]):
        #         sr = math.sqrt(int(i))
        #         if((sr) == int(sr)):
        #             sr = int(sr)
        #             sr = str(sr)
        #             if(sr == sr[::-1]):
        #                 X.append(i)
        # return len(X)

        # ans = 0
        # l = int(left)
        # r = int(right)
        # # Odd Case
        # for i in range(10**5):
        #     s1 = str(i)
        #     s2 = s1[-2::-1]
        #     s = s1 + s2
        #     num = int(s) ** 2
        #     if num > r:
        #         break
        #     if num >= 1 and str(num) == str(num)[::-1]:
        #         ans += 1

        # # Even Case
        # for i in range(10**5):
        #     s1 = str(i)
        #     s2 = s1[::-1]
        #     s = s1 + s2
        #     num = int(s) ** 2
        #     if num > r:
        #         break

        #     if num >= l and str(num) == str(num)[::-1]:
        #         ans += 1
        # return ans

        left = int(left)
        right = int(right)
        count = 0
        current = 1
        while True:

            c = str(current)
            p = int(c + c[:-1][::-1])
            if left <= (x := p * p) <= right and ((s := str(x)) == s[::-1]):
                count += 1
            if x > right:
                break
            c = str(current)
            p = int(c + c[::-1])
            if left <= (x := p * p) <= right and ((s := str(x)) == s[::-1]):
                count += 1
            current += 1
        return count


X = Solution()
print(X.superpalindromesInRange(4, 1000))
print(X.superpalindromesInRange(40000000000000000, 50000000000000000))


# Leading Zeroes - Zero that comes before the Non Zero Digits
