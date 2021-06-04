# Construct Target Array with Multiple Sums
# Array Greedy

import heapq


# class Solution:
#     def isPossible(self, target) -> bool:
#         h = [-n for n in target]
#         total = sum(target)
#         heapq.heapify(h)
#         while h[0] != -1:
#             cand = -heapq.heappop(h)
#             rest_of = total - cand
#             if rest_of <= 0 or cand <= rest_of:
#                 return False
#             prev = cand % rest_of
#             heapq.heappush(h, -prev)
#             total -= cand
#             total += prev
#         return True

# class Solution:
#     def isPossible(self, target) -> bool:
#         N = len(target)
#         target = sorted(x - 1 for x in target if x > 1)
#         if not(all(x % (N - 1) == 0 for x in target) and len(set(target)) == len(target)):
#             return False
#         currentSum = 0
#         for x in target:
#             if currentSum + N > x + 1:
#                 return False
#             currentSum += x
#         return True

class Solution:
    def isPossible(self, target) -> bool:
        tot = sum(target)
        end = len(target)

        while tot != end:
            maxIndex = target.index(max(target))
            rest = tot - target[maxIndex]

            if rest == 0 or rest >= target[maxIndex]:
                return False

            tmp = target[maxIndex]

            if target[maxIndex] % rest == 0:
                target[maxIndex] = rest
            else:
                target[maxIndex] = target[maxIndex] % rest
            tot = tot - tmp + target[maxIndex]

        return True


X = Solution()
print(X.isPossible([9, 3, 5]))
