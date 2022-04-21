# Shuffle the Array
# Hint - > Use two pointers to create the new array of 2n elements. The first starting at the beginning and the other starting at (n+1)th position. Alternate between them and create the new array.


class Solution:
    def shuffle(self, nums, n):
        ans = []
        N = len(nums)
        for i in range(N//2):
            ans.append(nums[i])
            ans.append(nums[i-N//2])
        return ans


X = Solution()
Arr = [10, 10, 20, 304]
print(X.shuffle(Arr, 2))
