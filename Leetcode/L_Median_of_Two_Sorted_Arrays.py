# Median of Two Sorted Arrays

import math


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        X = []
        for i in range(0, len(nums1)):
            X.append(nums1[i])
        for i in range(0, len(nums2)):
            X.append(nums2[i])
        X.sort()
        Y = len(X)
        if ((Y % 2) != 0):
            A = float(X[(math.floor(Y//2))])
            B = float("%.5f" % A)
            return B
        else:
            C = float((X[(Y//2)] + X[(Y//2) - 1]) / 2)
            D = float("%.5f" % C)
            return D


X = Solution()
print(type(X.findMedianSortedArrays([1, 3], [2])))
print(X.findMedianSortedArrays([1, 2], [3, 4]))
print(X.findMedianSortedArrays([0, 0], [0, 0]))
print(X.findMedianSortedArrays([], [1]))
print(X.findMedianSortedArrays([2], []))
