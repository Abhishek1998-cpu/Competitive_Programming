# Maximum Product of Two Elements in an Array


class Solution:
    def maxProduct(self, nums):
        # nums2 = []
        # for i in range(0, len(nums)):
        #     for j in range(0, len(nums)):
        #         if (i != j):
        #             nums2.append((nums[i] - 1) * (nums[j] - 1))
        # return max(nums2)
        # The Approach above is slower - O(n^2)

        nums.sort()
        return (nums[-1]-1)*(nums[-2]-1)


X = Solution()
print(X.maxProduct([3, 4, 5, 2]))
print(X.maxProduct([1, 5, 4, 5]))
print(X.maxProduct([3, 7]))
